from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on the provided targets."""

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel mana and return updated mana state."""

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return magic-related stats."""
