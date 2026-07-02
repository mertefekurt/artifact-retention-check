# artifact-retention-check

> Check build artifact retention policies for expiry, owner, and sensitive output risks.

## Risk note Overview

Check build artifact retention policies for expiry, owner, and sensitive output risks. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts artifact retention policy. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
artifact-retention-check examples/sample.txt
artifact-retention-check examples/sample.txt --json --fail-on medium
python -m artifact_retention_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `retention-forever` | high | artifact retention is unbounded |
| `unknown-owner` | medium | artifact owner missing |
| `secrets-possible` | low | secrets may be in artifacts |

## Validation Notes

```bash
ruff check .
pytest
python -m artifact_retention_check --help
```

Example risky input:

```text
artifact logs retention forever owner unknown secrets possible
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
