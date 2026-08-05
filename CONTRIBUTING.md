# Contributing

Thank you for helping improve Cloud GPU Workstation Lab.

## Principles

- Prefer provider-neutral architecture where practical.
- Do not publish credentials, personal data, billing identifiers, or private access details.
- Do not present changing prices as permanent facts.
- Use primary official documentation for technical claims.
- Keep scripts repeatable and fail with useful messages.
- Maintain backward compatibility unless a pull request justifies a breaking change.
- Separate documentation, infrastructure, and functional changes when they can be reviewed independently.

## Pull request workflow

1. Open an issue for a material change.
2. Create one focused branch, for example `docs/cost-control` or `fix/windows-driver-check`.
3. Add or update unit and integration tests when code changes.
4. Update affected documentation.
5. Run local checks.
6. Open one pull request for one logical change.
7. Explain purpose, risk, compatibility, and verification.
8. Merge only after CI is green.

## Local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
bash -n scripts/linux/check-gpu.sh
```

PowerShell scripts should also be reviewed or tested on a supported Windows environment.

## Commit and PR quality

Use clear, imperative commit messages. Pull requests should include:

- the problem being solved,
- a concise list of changes,
- cost, security, and compatibility risks,
- test evidence,
- documentation impact,
- rollback notes when the change affects infrastructure.
