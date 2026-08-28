# Luca

Luca is an open-source framework for representing accounting transactions in a
minimal form while enforcing strong data validation.

The project aims to provide low-level scaffolding for defining basic
transactions using the lowest common denominator of accounting data. Its
simplicity is intentional: Luca is designed to be easy to understand, extend,
and adapt without forcing every use case into a complex accounting system.

Luca's code and data structures are intended to be readable by both people and
AI agents. This gives accounting professionals a foundation for building
bespoke tools and systems without repeatedly reinventing core transaction
types.

## Core principles

### Data

- Provide a strongly validated core data model built with Pydantic classes.
- Keep common workflows simple by default while allowing additional complexity
  when a use case requires it.

### Reporting

- Provide ORM-based persistence for databases such as SQLite, PostgreSQL,
  MariaDB, and others.
- Make it easy to write data to common file formats, including plain text,
  JSON, and CSV.
- Include a built-in web interface for browsing and sharing data.

### Governance

- Offer effective, straightforward user management.
- Make audit trails part of the core data model through events.

### Experience

- Include a CLI designed for convenient use by people and AI agents alike.

## Project status

Luca is in early development. The first core slice currently provides:

- Validated models for accounts, journals, monetary values, journal lines, and
  journal entries.
- Double-entry validation that balances debits and credits independently for
  each currency.
- Stable record identifiers, timezone-aware timestamps, descriptive generated
  schemas, and JSON serialization.
- Storage-neutral CRUD contracts with an in-memory implementation suitable for
  tests and lightweight workflows.

Database persistence, reporting, governance, the web interface, and the CLI
remain planned capabilities rather than stable public APIs.

## Core model example

```python
from datetime import date
from decimal import Decimal
from uuid import uuid4

from luca import EntrySide, JournalEntry, JournalLine, Money

cash_account_id = uuid4()
revenue_account_id = uuid4()

entry = JournalEntry(
    journal_id=uuid4(),
    transaction_date=date(2026, 8, 22),
    description="Record a cash sale",
    lines=(
        JournalLine(
            account_id=cash_account_id,
            side=EntrySide.DEBIT,
            amount=Money(amount=Decimal("125.00"), currency="USD"),
        ),
        JournalLine(
            account_id=revenue_account_id,
            side=EntrySide.CREDIT,
            amount=Money(amount=Decimal("125.00"), currency="USD"),
        ),
    ),
)
```

Unbalanced entries, zero-value lines, invalid currency codes, unknown fields,
and naive audit timestamps are rejected during validation.

## Development

Install the locked development environment and run the quality checks with
`uv`:

```console
uv sync
uv run ruff check .
uv run mypy src
uv run pytest
uv build
```

## License

Luca is available under the [MIT License](LICENSE).
