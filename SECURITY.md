# Security policy

## Reporting a vulnerability

Do not open a public issue containing credentials, private IP addresses, billing information, access tokens, exploitable configuration details, or personal data.

Report security concerns privately to **kontakt@teslaeco.pl** with:

- the affected file or workflow,
- the potential impact,
- safe reproduction steps,
- any suggested mitigation.

Do not include active secrets. Revoke or rotate exposed credentials before sending a report.

## When a secret is exposed

1. Revoke or rotate it immediately.
2. Remove it from active systems.
3. Audit access logs and billing.
4. Purge it from Git history when required.
5. Document the incident without republishing the secret.

## Supported versions

Security fixes target the current `main` branch. Older snapshots may not receive backports.
