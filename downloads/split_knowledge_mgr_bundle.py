#!/usr/bin/env python3
"""Validate and split concatenated KnowledgeMgr knowledge stanzas."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_FORMAT = HERE / "aix73_tech_format_definition.txt"
DEFAULT_BUNDLE = HERE / "aix73_tech_knowledge_bundle.txt"
DEFAULT_OUTPUT = HERE / "out"
VALID_FIELD_TYPES = {"単一行", "複数行", "日付", "選択"}
SYSTEM_KEYS = ("KnowledgeNo", "FormatID", "CreatedAt", "UpdatedAt")
HEADER = re.compile(r"^###([^#\r\n]+)###$")


@dataclass(frozen=True)
class Field:
    name: str
    field_type: str
    required: bool


@dataclass(frozen=True)
class FormatDefinition:
    format_id: str
    format_name: str
    fields: tuple[Field, ...]


def read_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig"), "utf-8-sig"
    for encoding in ("utf-8", "cp932"):
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            pass
    raise ValueError(f"UTF-8またはCP932として読めません: {path}")


def normalized_lines(text: str) -> list[str]:
    return text.replace("\r\n", "\n").replace("\r", "\n").split("\n")


def parse_format(path: Path) -> tuple[FormatDefinition, str]:
    text, encoding = read_text(path)
    sections: list[tuple[str, dict[str, str]]] = []
    section_name = ""
    values: dict[str, str] = {}

    def finish() -> None:
        nonlocal section_name, values
        if section_name:
            sections.append((section_name, values))
        section_name = ""
        values = {}

    for number, raw_line in enumerate(normalized_lines(text), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line == "===":
            finish()
            continue
        if line.startswith("[") and line.endswith("]"):
            finish()
            section_name = line[1:-1]
            continue
        if "=" not in raw_line or not section_name:
            raise ValueError(f"フォーマット構文エラー: {path}:{number}")
        key, value = raw_line.split("=", 1)
        key = key.strip()
        if key in values:
            raise ValueError(f"フォーマット内の重複キー: {key} ({path}:{number})")
        values[key] = value
    finish()

    formats = [values for name, values in sections if name == "FORMAT"]
    fields = [values for name, values in sections if name == "FIELD"]
    unknown = [name for name, _ in sections if name not in {"FORMAT", "FIELD"}]
    if len(formats) != 1 or not fields or unknown:
        raise ValueError(
            f"[FORMAT]は1個、[FIELD]は1個以上、未知セクションなしが必要です: "
            f"FORMAT={len(formats)} FIELD={len(fields)} unknown={unknown}"
        )
    fmt = formats[0]
    format_id = fmt.get("FormatID") or fmt.get("FormatId") or ""
    format_name = fmt.get("FormatName", "")
    if not format_id or not format_name:
        raise ValueError("FormatIDとFormatNameは必須です")

    parsed_fields: list[Field] = []
    names: set[str] = set()
    for index, values in enumerate(fields, 1):
        name = values.get("FieldName", "").strip()
        field_type = values.get("FieldType", "").strip()
        required_text = values.get("Required", "").strip().lower()
        if not name or field_type not in VALID_FIELD_TYPES:
            raise ValueError(
                f"FIELD {index}のFieldNameまたはFieldTypeが不正です: "
                f"{name!r}/{field_type!r}"
            )
        if name in names or name in SYSTEM_KEYS:
            raise ValueError(f"重複または予約済みFieldNameです: {name}")
        if required_text not in {"true", "false"}:
            raise ValueError(f"RequiredはTrue/Falseで指定します: {name}")
        if field_type == "選択" and not values.get("DropdownOptions", "").strip():
            raise ValueError(f"選択フィールドにはDropdownOptionsが必要です: {name}")
        names.add(name)
        parsed_fields.append(Field(name, field_type, required_text == "true"))
    return FormatDefinition(format_id, format_name, tuple(parsed_fields)), encoding


def split_record_texts(text: str) -> list[str]:
    lines = normalized_lines(text)
    starts = [index for index, line in enumerate(lines) if line == "###KnowledgeNo###"]
    if not starts:
        raise ValueError("###KnowledgeNo### で始まるレコードがありません")
    if any(line.strip() for line in lines[: starts[0]]):
        raise ValueError("先頭レコードの前にデータがあります")
    records: list[str] = []
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(lines)
        record = "\n".join(lines[start:end]).rstrip("\n")
        if record:
            records.append(record)
    return records


def parse_record(text: str, ordinal: int) -> dict[str, str]:
    values: dict[str, str] = {}
    key = ""
    body: list[str] = []

    def finish() -> None:
        nonlocal key, body
        if not key:
            return
        if key in values:
            raise ValueError(f"レコード{ordinal}: 重複キー {key}")
        values[key] = "\n".join(body).rstrip("\n")
        key = ""
        body = []

    for line in normalized_lines(text):
        match = HEADER.fullmatch(line)
        if match:
            finish()
            key = match.group(1)
        elif key:
            body.append(line)
        elif line.strip():
            raise ValueError(f"レコード{ordinal}: ヘッダー前に値があります")
    finish()
    return values


def validate_record(
    values: dict[str, str],
    definition: FormatDefinition,
    ordinal: int,
) -> tuple[str, str]:
    field_names = {field.name for field in definition.fields}
    allowed = set(SYSTEM_KEYS) | field_names
    unknown = set(values) - allowed
    missing_system = [key for key in SYSTEM_KEYS if not values.get(key, "").strip()]
    missing_fields = [
        field.name
        for field in definition.fields
        if field.required and not values.get(field.name, "").strip()
    ]
    if unknown or missing_system or missing_fields:
        raise ValueError(
            f"レコード{ordinal}: unknown={sorted(unknown)} "
            f"missing_system={missing_system} missing_required={missing_fields}"
        )
    if values["FormatID"].strip() != definition.format_id:
        raise ValueError(
            f"レコード{ordinal}: FormatIDが不一致です "
            f"({values['FormatID']!r} != {definition.format_id!r})"
        )
    knowledge_no = values["KnowledgeNo"].strip()
    expected = re.compile(
        rf"^{re.escape(definition.format_id)}-\d{{4}}-\d{{4}}$",
        re.IGNORECASE,
    )
    if not expected.fullmatch(knowledge_no):
        raise ValueError(f"レコード{ordinal}: KnowledgeNoが不正です: {knowledge_no}")
    for key, value in values.items():
        try:
            value.encode("cp932")
        except UnicodeEncodeError as exc:
            raise ValueError(
                f"レコード{ordinal}/{key}: CP932へ変換できない文字があります"
            ) from exc
    return knowledge_no, values["FormatID"].strip()


def to_cp932_crlf(text: str) -> bytes:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n")
    return (normalized.replace("\n", "\r\n") + "\r\n").encode("cp932")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="KnowledgeMgr連結ナレッジを検査し、1件1ファイルへ分解します。"
    )
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--format-definition", type=Path, default=DEFAULT_FORMAT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="検査のみ。書き込みません。")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="既存の同名ナレッジを上書きします。",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    definition, format_encoding = parse_format(args.format_definition)
    bundle_text, bundle_encoding = read_text(args.bundle)
    record_texts = split_record_texts(bundle_text)

    outputs: list[tuple[Path, bytes]] = []
    seen: set[str] = set()
    for ordinal, record_text in enumerate(record_texts, 1):
        values = parse_record(record_text, ordinal)
        knowledge_no, format_id = validate_record(values, definition, ordinal)
        key = knowledge_no.lower()
        if key in seen:
            raise ValueError(f"KnowledgeNoが重複しています: {knowledge_no}")
        seen.add(key)
        target = args.output / format_id / f"{knowledge_no}.txt"
        outputs.append((target, to_cp932_crlf(record_text)))

    print(
        f"PASS format={definition.format_id} fields={len(definition.fields)} "
        f"records={len(outputs)} format_encoding={format_encoding} "
        f"bundle_encoding={bundle_encoding} output=CP932/CRLF"
    )
    if args.check:
        print("CHECK ONLY: ファイルは書き込んでいません。")
        return 0

    collisions = [path for path, _ in outputs if path.exists()]
    if collisions and not args.overwrite:
        names = ", ".join(str(path) for path in collisions)
        raise FileExistsError(
            f"既存ファイルがあるため停止しました。上書きする場合は --overwrite: {names}"
        )
    for path, content in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        print(f"WROTE {path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        raise SystemExit(1)
