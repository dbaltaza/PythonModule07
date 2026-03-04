from typing import Any

from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive int")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive int")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict[str, Any]:
        try:
            battlefield = game_state["battlefield"]
            current_mana = game_state["current_mana"]
        except KeyError as exc:
            return {"error": f"Missing game state key: {exc.args[0]}"}

        if not isinstance(battlefield, list):
            return {"error": "battlefield must be a list"}
        if not isinstance(current_mana, int):
            return {"error": "current_mana must be an int"}
        if not self.is_playable(current_mana):
            return {"error": "Not enough mana to play this card"}

        battlefield.append(self)
        game_state["current_mana"] = current_mana - self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: "CreatureCard") -> dict[str, Any]:
        if not isinstance(target, CreatureCard):
            return {"error": "Target must be a CreatureCard"}
        target.health -= self.attack

        combat_resolved = target.health <= 0
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": combat_resolved,
        }

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health,
        }

    def is_playable(self, available_mana: int) -> bool:
        return super().is_playable(available_mana)
