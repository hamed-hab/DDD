# Dataset description (Simulation dataset: 300 records)

This repository includes the simulation dataset used in the thesis appendix (300 observations).

## File
- `data/simulation_dataset_300.csv`

## Columns
- `Attack Type` : Attack scenario (e.g., Brute Force, SQL Injection, Lateral Movement)
- `System` : Evaluated system (`ELK` vs `Proposed`)
- `Run` : Independent run index (1–50 per scenario/system pair)
- `MTTR` : Mean Time To Respond **(minutes)**
- `AET` : Average Engagement Time **(minutes)**
- `AICR` : Attack Impact Containment Ratio (0–1)
- `VISR` : Vulnerability Identification Success Rate (0–1)
- `FPR` : False Positive Rate (0–1)

## Notes
- The dataset is arranged so that for each Attack Type, both systems (ELK and Proposed) have comparable runs.
- Summary results in the thesis can be reproduced by aggregating metrics by (`System`, `Attack Type`).
