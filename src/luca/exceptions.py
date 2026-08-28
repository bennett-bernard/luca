"""Domain errors raised by Luca's service and repository interfaces."""

from uuid import UUID


class LucaError(Exception):
    """Base class for expected errors raised by Luca."""


class RecordNotFoundError(LucaError):
    """Raised when a record cannot be found by its identifier."""

    def __init__(self, record_type: str, record_id: UUID) -> None:
        self.record_type = record_type
        self.record_id = record_id
        super().__init__(f"{record_type} record {record_id} was not found")


class DuplicateRecordError(LucaError):
    """Raised when creating a record whose identifier already exists."""

    def __init__(self, record_type: str, record_id: UUID) -> None:
        self.record_type = record_type
        self.record_id = record_id
        super().__init__(f"{record_type} record {record_id} already exists")


class InvalidUpdateError(LucaError):
    """Raised when an update attempts to change Luca-managed fields."""

    def __init__(self, fields: set[str]) -> None:
        self.fields = frozenset(fields)
        names = ", ".join(sorted(fields))
        super().__init__(f"update cannot change Luca-managed fields: {names}")
