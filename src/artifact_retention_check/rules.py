from __future__ import annotations

from artifact_retention_check.models import Rule

PROJECT_NAME = 'artifact-retention-check'
SUMMARY = (
              'Check build artifact retention policies for expiry, owner, and sensitive'
              ' output risks.'
          )
SAMPLE_RISK = 'artifact logs retention forever owner unknown secrets possible'
SAMPLE_CLEAN = 'artifact logs retention 14d owner devex secrets none'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='retention-forever',
        severity='high',
        pattern='retention\\s+forever',
        message='artifact retention is unbounded',
        recommendation='set retention window',
    ),
    Rule(
        code='unknown-owner',
        severity='medium',
        pattern='owner\\s+(unknown|none|missing)',
        message='artifact owner missing',
        recommendation='assign artifact owner',
    ),
    Rule(
        code='secrets-possible',
        severity='low',
        pattern='secrets\\s+possible',
        message='secrets may be in artifacts',
        recommendation='scan and redact artifacts',
    ),
)
