# Architecture

Community is an independent Apache-2.0 Python package. A separate proprietary
repository may depend on its versioned public interfaces. Community must never
import Enterprise or require private package credentials. Shared fixes belong here.

`server.py` owns MCP schemas and annotations; `cli.py` owns STDIO startup.
Empty package boundaries reserve `adapters`, `services`, `config` and `secrets`.
No HTTP adapter or credential backend is implemented yet. Add an asynchronous
HTTP client only when implementing verified official API endpoints; add an OS
keyring backend when implementing human-only credential setup.

Planned API base: `https://www.welcomekit.co/api/v1/external/`.
Begin with `organizations_r` and `jobs_r`; add `candidates_r` and `moves_r`
only with corresponding delivered features. Bound pagination, timeouts, retries
and output size; show collection time, scope and partial-result status.

Never store candidate records by default. Untrusted job/candidate text is data,
not instructions. Returned data can be sent by the client to its AI provider.
Never expose arbitrary URLs, credential administration or approval bypass tools.

## Client setup after `make bootstrap`

A generic MCP client can launch the installed absolute console path:

```json
{
  "mcpServers": {
    "junglebridge": {
      "command": "/absolute/path/to/junglebridge-mcp/.venv/bin/junglebridge-mcp",
      "args": []
    }
  }
}
```

Replace the absolute path with your checkout. Inside the devcontainer the
executable is `/home/vscode/.venv-junglebridge/bin/junglebridge-mcp`.
No token belongs in client configuration. The automated test uses a real
MCP client against the installed console script over STDIO.
