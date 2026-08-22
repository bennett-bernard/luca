# Repository Guidelines

## Project Structure & Module Organization

This repository is currently a bootstrap project: the only existing project file is the root-level `LICENSE`. Keep repository-wide files such as `README.md`, build manifests, and configuration at the root. When implementation begins, prefer a conventional layout: application code in `src/`, automated tests in `tests/` (or beside source files when the chosen framework expects that), and static resources in `assets/`. Keep generated output, dependency caches, and local environment files out of version control.

## Build, Test, and Development Commands

No build system, package manager, or test runner is configured yet. These commands are useful for validating changes now:

- `git status --short` — review staged, unstaged, and untracked files.
- `git diff --check` — detect whitespace errors before committing.
- `rg --files` — list tracked and unignored project files quickly.

When adding tooling, expose predictable commands such as `npm run build`, `npm test`, or `make test`, and document them in both this file and the project README.

## Coding Style & Naming Conventions

Follow the standard formatter and linter for the language introduced; commit their configuration with the first source files. Use UTF-8, LF line endings, and a trailing newline. Prefer descriptive names: `snake_case` for files unless an ecosystem convention differs, and verbs for functions that perform actions. Keep modules focused and avoid committing generated files unless they are required release artifacts.

## Testing Guidelines

There is currently no test framework or coverage threshold. New features should include automated tests once a framework is selected, and bug fixes should include a regression test. Mirror source structure under `tests/` and use recognizable names such as `test_<feature>.py` or `<feature>.test.ts`. Ensure the full test command passes locally before opening a pull request.

## Commit & Pull Request Guidelines

Git history currently contains only `Initial commit`, so no formal convention is established. Use concise, imperative, sentence-case subjects (for example, `Add configuration loader`) and keep each commit focused. Pull requests should explain what changed and why, list validation performed, and link relevant issues. Include screenshots or terminal output when behavior or user-facing output changes.

## Security & Configuration

Never commit credentials, tokens, private keys, or populated environment files. Add local configuration patterns to `.gitignore` before introducing them, and provide sanitized examples such as `.env.example` when configuration becomes necessary.
