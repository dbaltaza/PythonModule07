from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        rating: int = 1200,
    ) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if health <= 0:
            raise ValueError("Health must be a positive integer")
        if rating <= 0:
            raise ValueError("Rating must be a positive integer")

        self.attack_points = attack
        self.health = health
        self.wins = 0
        self.losses = 0
        self.base_rating = rating
        self.rating = rating

    def play(self, game_state: dict) -> dict[str, Any]:
        current_mana = game_state.get("current_mana", 0)
        if not isinstance(current_mana, int):
            return {"error": "current_mana must be an integer"}
        if not self.is_playable(current_mana):
            return {"error": "Not enough mana to play this card"}

        game_state["current_mana"] = current_mana - self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters battle",
        }

    def attack(self, target) -> dict[str, Any]:
        target_name = getattr(target, "name", str(target))
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_points,
            "combat_type": "tournament",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        if incoming_damage < 0:
            return {"error": "incoming_damage cannot be negative"}

        blocked = min(2, incoming_damage)
        damage_taken = incoming_damage - blocked
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {"attack": self.attack_points, "health": self.health}

    def calculate_rating(self) -> int:
        calculated = self.base_rating + (self.wins * 16) - (self.losses * 16)
        return max(100, calculated)

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            raise ValueError("wins cannot be negative")
        self.wins += wins
        self.rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            raise ValueError("losses cannot be negative")
        self.losses += losses
        self.rating = self.calculate_rating()

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        info = self.get_card_info()
        info.update(self.get_rank_info())
        info.update(self.get_combat_stats())
        info["record"] = f"{self.wins}-{self.losses}"
        return info
