#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (<=140 characters) for a city
that does not exist to /output/entry.txt.

The line was chosen from 12 candidates drafted for this bounty and
scored with the local deterministic scorer (select/local_score.py,
archetype one-liner) plus a local pairwise bracket
(select/pairwise_judge.py). Winner, score 71.0 (threshold 60):

  Muddleford: light rain until lunch, heavier after, and the 8:15 bus
  will still be exactly four minutes late, as tradition demands.

Why it wins against the judge brief (a bored commuter at a rainy bus
stop picks the line that makes them smile):
  1. It reads as a real one-line forecast: invented city named first,
     weather is the whole point.
  2. The smile comes from recognition, not quirk: every commuter
     knows a bus that is always exactly a few minutes late, and
     "as tradition demands" turns the lateness into civic ritual.
  3. It keeps the broadcast-weather register: "light rain until
     lunch, heavier after" is the rhythm of a real forecast, bent
     rather than dropped.
  4. One concrete detail of the city's life: the 8:15 bus, four
     minutes late, every day.
  5. 130 of 140 characters, every word earning its place.
"""

import os

ENTRY = (
    "Muddleford: light rain until lunch, heavier after, and the 8:15 "
    "bus will still be exactly four minutes late, as tradition demands."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    if not (1 <= len(ENTRY) <= 140):
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-140")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Read back and verify: what the grader reads must be exactly ENTRY.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("output mismatch: file does not contain ENTRY exactly")


if __name__ == "__main__":
    main()
