# spark-pipeline

Minimal data-processing pipeline run on demand via GitHub Actions.

- `process_data.py` — computes count, total, average, min, max and sorted values.
- Run locally: `python process_data.py`
- Run in CI: **Actions → Scheduled Cloud Data Pipeline → Run workflow** (result uploaded as an artifact).

## Pull requests

Pull requests run the unit tests and Python syntax checks in **Pull Request Checks**.
**Queue Approved Pull Requests** queues squash auto-merge only after a non-author,
non-bot reviewer has approved. GitHub completes the merge when its required rules
are satisfied.

To make this safe and active, enable **Allow auto-merge** in repository settings,
and protect the target branch by requiring the `validate` status check, at least
one approving review, and dismissal of stale approvals. Configure these under
**Settings → General** and **Settings → Branches** (or the repository's rulesets).
The workflow does not perform AI/LLM review; connecting review models requires
selecting a provider and configuring its credentials as repository secrets.

“Cross-platform app” means a separate product that runs from shared application
code on web browsers, Android, and iOS. Safari is a browser target; publishing
an iOS app to the App Store additionally requires an iOS build, Apple developer
signing, and App Store review. This repository is currently a Python pipeline,
not a mobile or web app.
