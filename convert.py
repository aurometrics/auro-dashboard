#!/usr/bin/env python3
"""
Ando Dashboard — Daily CSV converter
Usage: python3 convert.py your_file.csv
Outputs: data/YYYY-MM-DD.json  (ready to commit to GitHub)
"""
import sys, json, pandas as pd
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python3 convert.py <path_to_csv>")
    sys.exit(1)

src = Path(sys.argv[1])
df = pd.read_csv(src)
df.columns = [c.strip().rstrip('.') for c in df.columns]
df['Brand Name'] = df['Brand Name'].str.strip().str.rstrip('.')
df['Delivery Channel'] = df['Delivery Channel'].str.strip().str.rstrip('.')

date = df['Order Date'].iloc[0]
out = Path('data') / f"{date}.json"
out.parent.mkdir(exist_ok=True)
df.to_json(out, orient='records', indent=2)
print(f"✓ Written {len(df)} records → {out}")
