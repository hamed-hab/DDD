# Dataset description (Simulation outputs)

This document describes the simulation outputs used in the thesis evaluation of DDD-SOAR.

## Scenarios
The repository includes outputs for the following simulated attack scenarios:
- Brute Force
- SQL Injection
- Lateral Movement

(Adjust the list based on your actual files.)

## File naming convention
Files are stored under `data/` and are named to reflect the scenario and/or the metric.
Example patterns:
- `bruteforce_*.csv`
- `sqlinjection_*.csv`
- `lateralmovement_*.csv`

(Adjust these patterns to match your actual filenames.)

## Common columns (template)
Below is a template. Replace/extend it based on your real columns.

- `system` : The evaluated system (e.g., `ELK-SOAR`, `Proposed/DDD-SOAR`)
- `scenario` : Attack scenario name
- `run_id` : Simulation run identifier
- `episode` : Episode index (if RL episodes are used)
- `timestamp` : Time index (if applicable)
- `metric_*` : Reported metrics

## Metrics and units (template)
Replace with your exact definitions:

- `MTTR` : Mean Time To Respond (unit: seconds or minutes)
- `AET`  : Average Engagement Time (unit: seconds or minutes)
- `VISR` : Vulnerability Identification Success Rate (unit: percentage)
- `AICR` : (define exactly; unit: …)

## Notes on aggregation
- Per-run results are computed for each `run_id`.
- Reported summary values (means, comparisons) are obtained by aggregating across runs.
- If smoothing is used for learning curves, the window size is documented in the thesis text and/or `docs/REPRODUCIBILITY.md`.
