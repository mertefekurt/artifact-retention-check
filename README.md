# Artifact Retention Check

Check build artifact retention policies for expiry, owner, and sensitive output risks. The repository is intentionally plain: a small command, a visible rule surface, and enough examples to make the behavior inspectable.

<img src="assets/readme-cover.svg" alt="Artifact Retention Check cover" width="100%" />

## Review checklist

- [ ] artifact retention is unbounded (`retention-forever`, high)
- [ ] artifact owner missing (`unknown-owner`, medium)
- [ ] secrets may be in artifacts (`secrets-possible`, low)

## Command path

```bash
git clone https://github.com/mertefekurt/artifact-retention-check.git
cd artifact-retention-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
artifact-retention-check examples/sample.txt
artifact-retention-check examples/sample.txt --json
```

## Fixture worth keeping

```text
artifact logs retention forever owner unknown secrets possible
```

## Files I look at first

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
