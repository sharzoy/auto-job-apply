#!/usr/bin/env python3
"""Summarize applications/log.md (markdown table) or log.jsonl.

Usage:
  python scripts/stats_log.py
  python scripts/stats_log.py --log applications/log.md
  python scripts/stats_log.py --jsonl applications/log.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

REPLY_MARKERS = ("已回复", "面试", "约面", "已读", "offer")


def _is_sep_row(cells: list[str]) -> bool:
    if not cells:
        return True
    if cells[0] in ("date", "----", "---"):
        return True
    return bool(re.match(r"^[-:]+$", cells[0].replace(" ", "")))


def parse_md_table(text: str) -> list[dict]:
    """Supports:
    date | company | role | platform | score | grade | status | url | notes
    date | company | role | platform | score | status | url | notes  (legacy)
    """
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 6 or _is_sep_row(cells):
            continue

        # Heuristic: grade is a single letter A/B/C in column 5
        has_grade = len(cells) >= 7 and cells[5].upper() in ("A", "B", "C")
        if has_grade:
            while len(cells) < 9:
                cells.append("")
            rows.append(
                {
                    "date": cells[0],
                    "company": cells[1],
                    "role": cells[2],
                    "platform": cells[3],
                    "score": cells[4],
                    "grade": cells[5].upper(),
                    "status": cells[6],
                    "url": cells[7],
                    "notes": cells[8],
                }
            )
        else:
            while len(cells) < 8:
                cells.append("")
            score = cells[4]
            grade = ""
            try:
                s = float(str(score).strip())
                grade = "A" if s >= 90 else "B" if s >= 60 else "C"
            except ValueError:
                pass
            rows.append(
                {
                    "date": cells[0],
                    "company": cells[1],
                    "role": cells[2],
                    "platform": cells[3],
                    "score": score,
                    "grade": grade,
                    "status": cells[5],
                    "url": cells[6],
                    "notes": cells[7],
                }
            )
    return rows


def parse_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def summarize(rows: list[dict]) -> None:
    if not rows:
        print("No rows found.")
        return

    status = Counter(r.get("status", "") for r in rows)
    platforms = Counter(r.get("platform", "") for r in rows)
    grades = Counter(r.get("grade", "") or "?" for r in rows)

    scores = []
    for r in rows:
        try:
            scores.append(float(str(r.get("score", "")).strip()))
        except ValueError:
            pass

    submitted = [r for r in rows if r.get("status") == "submitted"]
    replied = [
        r
        for r in submitted
        if any(m in str(r.get("notes", "")) for m in REPLY_MARKERS)
    ]

    print(f"Total rows:     {len(rows)}")
    print(f"By status:      {dict(status)}")
    print(f"By platform:    {dict(platforms)}")
    print(f"By grade:       {dict(grades)}")
    if scores:
        print(
            f"Score avg/min/max: "
            f"{sum(scores)/len(scores):.1f} / {min(scores):.0f} / {max(scores):.0f}"
        )
    print(f"Submitted:      {len(submitted)}")
    if submitted:
        rate = 100.0 * len(replied) / len(submitted)
        print(
            f"Reply-ish rate: {len(replied)}/{len(submitted)} = {rate:.1f}% "
            f"(notes contain {REPLY_MARKERS})"
        )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", type=Path, default=root / "applications" / "log.md")
    ap.add_argument("--jsonl", type=Path, default=None)
    args = ap.parse_args()

    if args.jsonl and args.jsonl.exists():
        rows = parse_jsonl(args.jsonl)
    elif args.log.exists():
        rows = parse_md_table(args.log.read_text(encoding="utf-8"))
    else:
        example = root / "applications" / "log.example.md"
        print(f"No log at {args.log}; using example {example}")
        rows = parse_md_table(example.read_text(encoding="utf-8"))

    summarize(rows)


if __name__ == "__main__":
    main()
