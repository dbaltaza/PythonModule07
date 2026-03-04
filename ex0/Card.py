from abc import ABC, abstractmethod
from typing import Any


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if cost < 0:
            raise ValueError("Cost must be a non-negative int")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Apply the card effect to the in-memory game state."""

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
