# Security

Pre-alpha scaffold; not reviewed for production use. Use synthetic data only.
Do not put tokens, candidate records, CVs or exploit details in public issues.
No security-reporting address is configured yet: establish a private reporting
channel before any public release. Never claim a security audit from lint results.

Runtime dependency auditing, Bandit, typed code and a private-key pre-commit
check are configured. These do not detect every secret or vulnerability.
Future integration must restrict scopes, organizations, fields, pagination and
response sizes; redact errors; bound retries; treat API content as untrusted.
Local STDIO does not stop data returned to an assistant reaching its AI provider.
