"""
Reproduce basic summaries from the thesis simulation dataset.

Input:
- ../data/simulation_dataset_300.csv

Expected columns:
- Attack Type, System, Run, MTTR, AET, AICR, VISR, FPR

Units:
- MTTR: minutes
- AET: minutes
- AICR/VISR/FPR: proportions in [0, 1]

Output:
- code/output/summary_by_system_scenario.csv
"""

from __future__ import annotations
import os
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "simulation_dataset_300.csv")
OUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUT_DIR, exist_ok=True)

REQUIRED = ["Attack Type", "System", "Run", "MTTR", "AET", "AICR", "VISR", "FPR"]

def main() -> None:
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Missing dataset: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Dataset missing columns: {missing}")

    # Ensure numeric types
    for c in ["Run","MTTR","AET","AICR","VISR","FPR"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    summary = (
        df.groupby(["System", "Attack Type"])
          .agg(
              runs=("Run", "nunique"),
              n=("Run", "size"),
              mttr_mean=("MTTR", "mean"),
              mttr_std=("MTTR", "std"),
              aet_mean=("AET", "mean"),
              aet_std=("AET", "std"),
              aicr_mean=("AICR", "mean"),
              aicr_std=("AICR", "std"),
              visr_mean=("VISR", "mean"),
              visr_std=("VISR", "std"),
              fpr_mean=("FPR", "mean"),
              fpr_std=("FPR", "std"),
          )
          .reset_index()
    )

    out_path = os.path.join(OUT_DIR, "summary_by_system_scenario.csv")
    summary.to_csv(out_path, index=False)

    print(f"Saved: {out_path}")
    print(summary.to_string(index=False))

if __name__ == "__main__":
    main()
