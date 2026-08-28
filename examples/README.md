# Runnable examples

Run these scripts from the repository root after `uv sync --all-groups`:

```console
uv run python examples/01_accounting_flow.py
uv run python examples/02_validation_errors.py
uv run python examples/03_delete_audit.py
uv run python examples/04_custom_account.py
```

Each example is independent and uses in-memory storage, so it does not create a
database or leave application data behind.
