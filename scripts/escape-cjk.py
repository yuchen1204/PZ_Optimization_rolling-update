#!/usr/bin/env python3
r"""Escape every non-ASCII character inside string literals of a .lua source as \ddd escapes.

The game's Lua lexer (B42 org.luaj.kahluafork.compiler.LexState.save) stores each character of a
string literal as its single LOW BYTE (char & 0xFF) and re-decodes the buffer as UTF-8, so a raw
non-ASCII character ("卸" -> 0x78 'x') compiles into mojibake at runtime. Same convention as the
generated data files (scripts/i18n-build.py): every non-ASCII character goes out as UTF-8 \ddd
byte escapes, which the lexer stores byte-exact and the UTF-8 re-decode rebuilds.
Comments are left as they are (the lexer skips them). build.sh's raw-cjk gate verifies no
un-escaped literal remains hand-written into a code line.
"""
import sys
from pathlib import Path


def escape_body(val):
    out = []
    for ch in val:
        if ord(ch) < 0x80:
            out.append(ch)
        else:
            for b in ch.encode("utf-8"):
                out.append(f"\\{b:03d}")
    return "".join(out)


def scan(line):
    """Yield (kind, start, end_inclusive): kind 'str' for literals, 'comment' for -- comments."""
    i, n = 0, len(line)
    while i < n:
        ch = line[i]
        if ch == '"':
            j = i + 1
            while j < n:
                if line[j] == "\\":
                    j += 2
                    continue
                if line[j] == '"':
                    break
                j += 1
            yield ("str", i, j)
            i = j + 1
        elif ch == "'":
            j = i + 1
            while j < n:
                if line[j] == "\\":
                    j += 2
                    continue
                if line[j] == "'":
                    break
                j += 1
            yield ("str", i, j)
            i = j + 1
        elif line[i:i + 2] == "--":
            if i + 4 <= n and line[i + 2:i + 4] == "[[":
                yield ("comment", i, n - 1)
                i = n
            else:
                yield ("comment", i, n - 1)
                i = n
        else:
            i += 1


def process(path):
    p = Path(path)
    src = p.read_text(encoding="utf-8")
    out_lines = []
    for line in src.split("\n"):
        if not any(ord(c) > 0x7F for c in line):
            out_lines.append(line)
            continue
        if line.lstrip().startswith("--"):
            out_lines.append(line)  # whole-line comment: keep readable
            continue
        pieces = []
        pos = 0
        for kind, a, b in scan(line):
            pieces.append(line[pos:a])
            inner = line[a:b + 1]
            if kind == "comment" or not any(ord(c) > 0x7F for c in inner):
                pieces.append(inner)
            else:
                quote = inner[0]
                body = inner[1:-1]
                pieces.append(quote + escape_body(body) + quote)
            pos = b + 1
        pieces.append(line[pos:])
        out_lines.append("".join(pieces))
    p.write_text("\n".join(out_lines), encoding="utf-8")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        process(arg)
        print(f"escaped string literals: {arg}")
