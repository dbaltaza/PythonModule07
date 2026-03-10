from abc import ABC, abstractmethod


class Rankable(ABC):
    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the current rating."""

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update wins and rating."""

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update losses and rating."""

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return ranking metadata."""
