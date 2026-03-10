from abc import ABC, abstractmethod


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute one turn based on the strategy."""

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return strategy display name."""

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Order targets according to strategy rules."""
