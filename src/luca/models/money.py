"""Validated monetary values used throughout Luca."""

from decimal import Decimal
from typing import Annotated

from pydantic import Field, StringConstraints, field_validator

from luca.models.base import LucaModel

CurrencyCode = Annotated[
    str,
    StringConstraints(
        min_length=3,
        max_length=3,
        pattern=r"^[A-Z]{3}$",
        strip_whitespace=True,
    ),
]


class Money(LucaModel):
    """A non-negative decimal amount denominated in one currency."""

    amount: Decimal = Field(
        ge=0,
        description=(
            "Non-negative monetary quantity represented as a decimal value. String or "
            "Decimal inputs are recommended when exact precision matters."
        ),
        examples=["1250.00"],
    )
    currency: CurrencyCode = Field(
        description=(
            "Three-letter uppercase currency code, normally an ISO 4217 code such as "
            "USD, EUR, or GBP."
        ),
        examples=["USD"],
    )

    @field_validator("currency", mode="before")
    @classmethod
    def normalize_currency(cls, value: object) -> object:
        """Accept human-friendly lowercase codes while storing a canonical value."""

        if isinstance(value, str):
            return value.strip().upper()
        return value
