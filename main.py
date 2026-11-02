"""Build a shift-handover note in Markdown from an open-ticket CSV.

Usage: python3 main.py tickets.csv [--output handover.md]
CSV columns: ticket,priority,status,summary
Only open tickets appear; P1 first, then P2, P3, P4. If an output file
is given it is written, otherwise the note goes to stdout.
"""
import argparse, csv, sys

ORDER = {"P1": 0, "P2": 1, "P3": 2, "P4": 3}


def build(rows):
    open_tickets = [r for r in rows if r["status"].strip().lower() != "closed"]
    open_tickets.sort(key=lambda r: ORDER.get(r["priority"].strip(), 9))
    lines = ["# Shift handover", "", f"Open tickets: {len(open_tickets)}", ""]
    for row in open_tickets:
        lines.append(f"- **{row['ticket']}** [{row['priority']}] {row['summary']}")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--output", default=None)
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        note = build(list(csv.DictReader(f)))
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(note)
    else:
        print(note, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
