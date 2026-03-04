from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if cost < 0:
            raise ValueError("Cost must be a non-negative int")
        if rarity not in {item.value for item in Rarity}:
            raise ValueError(f"Invalid rarity: {rarity}")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Apply the card effect to the in-memory game state."""

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
