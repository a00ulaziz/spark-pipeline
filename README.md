# spark-pipeline

Minimal data-processing pipeline run on demand via GitHub Actions.

- `process_data.py` — computes count, total, average, min, max and sorted values.
- Run locally: `python process_data.py`
- Run in CI: **Actions → Scheduled Cloud Data Pipeline → Run workflow** (result uploaded as an artifact).
