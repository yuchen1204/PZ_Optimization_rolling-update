#!/usr/bin/env python3
"""Fail when a .lua under src/lua carries a raw non-ASCII character in a code line.

The game's Lua lexer (B42 org.luaj.kahluafork.compiler.LexState.save) stores each character of a
string literal as its single LOW BYTE (char & 0xFF) and re-decodes the buffer as UTF-8, so a raw
"卸" compiles as "x" — every hand-written Chinese string is mojibake in game. The generated data
file (scripts/i18n-build.py) pre-escapes its strings as \\ddd byte sequences; hand-written sources
must too (scripts/escape-cjk.py rewrites a file in place). Whole-line comments are allowed: the
lexer skips them. 2026-10-09, the Chinese options tab rendered mojibake everywhere.

Usage: python3 scripts/raw-cjk-gate.py [file.lua ...]  (default: all *.lua under src/lua)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def offenders(path):
    src = Path(path).read_text(encoding="utf-8", errors="replace")
    bad = []
    for i, line in enumerate(src.splitlines(), 1):
        # everything from a -- comment on is skipped by the lexer: only the code part matters
        code = line.split("--", 1)[0]
        if not any(ord(c) > 0x7F for c in code):
            continue
        col = next(j for j, ch in enumerate(code) if ord(ch) > 0x7F)
        bad.append((i, col + 1, line.strip()[:70]))
    return bad


def main():
    files = [Path(a) for a in sys.argv[1:]] or sorted((ROOT / "src/lua").rglob("*.lua"))
    failed = 0
    for f in files:
        bad = offenders(f)
        if bad:
            failed += 1
            rel = f.relative_to(ROOT) if f.is_relative_to(ROOT) else f
            print(f"RAW NON-ASCII in {rel}: the game's lexer takes each string literal character's"
                  f" low byte and re-decodes as UTF-8 — mojibake in game."
                  f" Run scripts/escape-cjk.py on the file (it escapes the strings, keeps comments):",
                  file=sys.stderr)
            for ln, col, text in bad[:5]:
                print(f"  line {ln} col {col}: {text}", file=sys.stderr)
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
