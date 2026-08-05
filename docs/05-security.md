# Security

Cloud GPU systems are expensive and attractive targets.

## Minimum controls

1. Enable MFA on cloud, GitHub, email, and provider accounts.
2. Use unique passwords and a password manager.
3. Restrict RDP and SSH firewall rules to trusted sources.
4. Avoid exposing RDP or SSH to `0.0.0.0/0`.
5. Use least-privilege IAM roles.
6. Keep API keys outside the repository.
7. Rotate exposed credentials immediately.
8. Patch the operating system and drivers.
9. Keep source-code backups outside the VM.
10. Review audit logs and billing anomalies.

## Never commit

- service-account files,
- SSH private keys,
- Windows passwords,
- API tokens,
- payment data,
- Epic or cloud credentials,
- affiliate dashboard credentials.

## Recovery model

The project must survive total loss of the workstation. Source code belongs in remote Git. Large assets and checkpoints belong in durable, versioned storage. Restoration should be tested before an emergency.
