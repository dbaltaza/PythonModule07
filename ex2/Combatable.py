from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> dict:
        """Attack a target and return combat results."""

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage and return defense results."""

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return combat-related stats."""
