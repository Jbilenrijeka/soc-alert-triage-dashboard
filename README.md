# SOC Alert Triage Summary

## Objective
Generate a small self-contained HTML report from sample alert data using only Python's standard library.

## Run
```bash
python build_report.py data/alerts.csv
```
Then open `triage_report.html` in a browser.

## What it demonstrates
- CSV data handling
- Grouping alert counts by severity and status
- Generating a readable report
- Separating alert status from conclusions

No external packages or live integrations are required.
