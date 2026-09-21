.PHONY: bootstrap check lint format typecheck security test audit build
bootstrap:
	uv sync --locked
	uv run --no-sync pre-commit install
lint:
	uv run --no-sync ruff check .
	uv run --no-sync ruff format --check .
format:
	uv run --no-sync ruff check --fix .
	uv run --no-sync ruff format .
typecheck:
	uv run --no-sync mypy
security:
	uv run --no-sync bandit -c pyproject.toml -r src
test:
	uv run --no-sync pytest
check: lint typecheck security test
audit:
	@set -eu; audit_dir=$$(mktemp -d); trap 'rm -rf "$$audit_dir"' EXIT; \
	uv export --locked --no-dev --no-emit-project --format requirements-txt --output-file "$$audit_dir/requirements.txt" >/dev/null; \
	uv run --no-sync pip-audit --require-hashes --disable-pip -r "$$audit_dir/requirements.txt"
build:
	uv build
