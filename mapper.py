#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if not line or line.startswith("date,"):
        continue

    fields = line.split(",")

    if len(fields) != 4:
        continue

    date, household, hour, consumption = fields

    print(f"{household}\t{consumption}")
