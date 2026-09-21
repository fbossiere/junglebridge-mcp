# JungleBridge MCP

Your Welcome to the Jungle recruitment workflows, in your AI assistant.

**Development scaffold — the WTTJ integration is not implemented yet.**
This repository provides a working local FastMCP STDIO server and a reproducible
Python development environment. Its only tool, `get_connection_status`, returns
`not_implemented`; it makes no API request and reads no credentials.

## Development

Open this repository in VS Code and choose **Dev Containers: Reopen in Container**.
Python, uv and Claude Code are included. Run `claude` inside the container to sign in.

Or install uv locally:

```sh
make bootstrap
make check
make audit
make build
uv run --no-sync junglebridge-mcp
```

The last command waits for a client speaking MCP over STDIO; it is not a chat CLI.
See the [French development guide](docs/development.md),
[architecture](docs/architecture.md), [capability matrix](docs/capabilities.md)
and [security notes](SECURITY.md).

## Roadmap

Read-only organization, job, candidate and movement tools, then bounded recruitment
summaries. API access and scopes must be confirmed before a private pilot.
No automated candidate ranking, hiring decisions, emails or job publication.
No affiliation or partnership with Welcome to the Jungle is claimed.

## License

Apache-2.0. Community is independent and intended for self-managed professional use.
Optional proprietary enterprise extensions will live in a separate repository.
No commercial Community quota is planned; upstream and technical limits will apply.
