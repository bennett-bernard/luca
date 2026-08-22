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

Luca is currently in its initial bootstrap stage. The principles above describe
the intended direction of the framework; the implementation and its public API
are still to be developed.

## License

Luca is available under the [MIT License](LICENSE).
