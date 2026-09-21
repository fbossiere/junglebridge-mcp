FROM node:25-bookworm-slim AS node
FROM ghcr.io/astral-sh/uv:0.12.17 AS uv
FROM mcr.microsoft.com/devcontainers/python:1-3.13-bookworm

COPY --from=uv /uv /uvx /usr/local/bin/
COPY --from=node /usr/local/bin/node /usr/local/bin/node
COPY --from=node /usr/local/lib/node_modules/npm /usr/local/lib/node_modules/npm
ARG CLAUDE_CODE_VERSION=2.1.278
RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
    && ln -s /usr/local/lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx \
    && npm install -g "@anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}" \
    && npm cache clean --force \
    && rm -f /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends ripgrep make \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /home/vscode/.claude \
    && chown vscode:vscode /home/vscode/.claude
USER vscode
