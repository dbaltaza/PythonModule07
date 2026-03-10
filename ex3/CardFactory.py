from abc import ABC, abstractmethod

from ex0.Card import Card


class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a creature card."""

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a spell card."""

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create and return an artifact card."""

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck."""

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Return supported card type definitions."""
