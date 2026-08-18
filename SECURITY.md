# Security Policy

## Reporting a Vulnerability

Do not publish sensitive security issues, credentials, tokens, private keys, or personal data in public issues.

Security vulnerabilities should be reported privately to the project maintainers.

## Secrets

The repository must never contain:

- Passwords
- API keys
- Access tokens
- Private keys
- Production credentials
- Database credentials
- Other sensitive secrets

Use environment variables and secure secret-management mechanisms instead.

## Verification Requirement

Security checks are part of the NIDDE verification process.

A file containing exposed secrets is BLOCKED until the issue is removed and the file is re-verified.
