#!/usr/bin/env python3
import sys

current_household = None
total = 0.0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    household, consumption = line.split("\t")

    if current_household == household:
        total += float(consumption)
    else:
        if current_household is not None:
            print(f"{current_household}\t{total:.2f}")

        current_household = household
        total = float(consumption)

if current_household is not None:
    print(f"{current_household}\t{total:.2f}")
