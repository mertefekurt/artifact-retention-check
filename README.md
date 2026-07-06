<img src="assets/readme-cover.svg" alt="Artifact Retention Check cover" width="100%" />

# Artifact Retention Check

Check build artifact retention policies for expiry, owner, and sensitive output risks.

![stack](https://img.shields.io/badge/stack-Python-dc2626?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-7c3aed?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-0891b2?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-b45309?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `artifact-retention-check` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `retention-forever` | high | artifact retention is unbounded |
| `unknown-owner` | medium | artifact owner missing |
| `secrets-possible` | low | secrets may be in artifacts |

## Command line

```bash
python -m pip install -e ".[dev]"
artifact-retention-check examples/sample.txt
artifact-retention-check examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
artifact logs retention forever owner unknown secrets possible
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
