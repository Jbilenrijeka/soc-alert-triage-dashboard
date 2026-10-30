import csv
import html
import sys
from collections import Counter
from pathlib import Path

def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/alerts.csv")
    with source.open(newline="", encoding="utf-8") as f:
        alerts = list(csv.DictReader(f))
    severity_counts = Counter(a["severity"] for a in alerts)
    status_counts = Counter(a["status"] for a in alerts)

    rows = []
    for a in alerts:
        rows.append("<tr>" + "".join(
            f"<td>{html.escape(a.get(k, ''))}</td>"
            for k in ("alert_id", "timestamp_utc", "alert_name", "severity", "status", "analyst_note")
        ) + "</tr>")

    summary = "".join(f"<li>{html.escape(k)}: {v}</li>" for k, v in sorted(severity_counts.items()))
    statuses = "".join(f"<li>{html.escape(k)}: {v}</li>" for k, v in sorted(status_counts.items()))
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>SOC Alert Triage Report</title>
<style>body{{font:16px system-ui;max-width:1100px;margin:2rem auto;padding:0 1rem;color:#222}}
table{{border-collapse:collapse;width:100%;font-size:14px}}th,td{{border:1px solid #ddd;padding:.55rem;text-align:left}}
th{{background:#f3f3f3}}code{{background:#eee;padding:.15rem .3rem}}</style></head>
<body><h1>SOC Alert Triage Report</h1>
<p><strong>Training data only.</strong> This report summarizes alert records; it does not confirm malicious activity.</p>
<h2>Counts by severity</h2><ul>{summary}</ul><h2>Counts by status</h2><ul>{statuses}</ul>
<h2>Alerts</h2><table><thead><tr><th>ID</th><th>Timestamp UTC</th><th>Alert</th><th>Severity</th><th>Status</th><th>Analyst note</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table></body></html>'''
    out = Path("triage_report.html")
    out.write_text(page, encoding="utf-8")
    print(f"Wrote {out.resolve()}")

if __name__ == "__main__":
    main()
