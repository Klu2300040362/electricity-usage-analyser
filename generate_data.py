import pandas as pd
import numpy as np

np.random.seed(42)

rows = []

for household in range(1, 11):
    for day in pd.date_range("2026-01-01", periods=30):
        for hour in range(24):

            usage = np.random.uniform(0.1, 0.5)

            if 6 <= hour <= 9 or 18 <= hour <= 22:
                usage += np.random.uniform(0.5, 1.5)

            if np.random.random() < 0.02:
                usage *= 3

            rows.append([
                day.strftime("%Y-%m-%d"),
                f"H{household:03d}",
                hour,
                round(usage, 2)
            ])

df = pd.DataFrame(
    rows,
    columns=["date", "household_id", "hour", "consumption_kwh"]
)

df.to_csv("data/electricity.csv", index=False)

print("Dataset generated successfully!")
print("Total records:", len(df))
print(df.head())



