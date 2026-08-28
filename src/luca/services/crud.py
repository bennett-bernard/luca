"""Application-level CRUD operations for Luca records."""

from uuid import UUID

from luca.models.base import RecordModel
from luca.repositories.base import RecordChanges, Repository


class CrudService[RecordT: RecordModel]:
    """Expose consistent record operations independently of storage technology."""

    def __init__(self, repository: Repository[RecordT]) -> None:
        self._repository = repository

    def create(self, record: RecordT) -> RecordT:
        """Create a validated record."""

        return self._repository.create(record)

    def retrieve(self, record_id: UUID) -> RecordT:
        """Retrieve a record by its stable identifier."""

        return self._repository.retrieve(record_id)

    def list(self) -> tuple[RecordT, ...]:
        """List all records available to this service."""

        return self._repository.list()

    def update(self, record_id: UUID, changes: RecordChanges) -> RecordT:
        """Apply a validated partial update to a record."""

        return self._repository.update(record_id, changes)

    def delete(self, record_id: UUID) -> RecordT:
        """Delete and return a record."""

        return self._repository.delete(record_id)
