"""Repository contracts and built-in adapters."""

from luca.repositories.base import RecordChanges, Repository
from luca.repositories.memory import InMemoryRepository

__all__ = ["InMemoryRepository", "RecordChanges", "Repository"]
