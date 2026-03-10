from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        defense: int,
        mana_pool: int = 0,
    ) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if health <= 0:
            raise ValueError("Health must be a positive integer")
        if defense < 0:
            raise ValueError("Defense cannot be negative")
        if mana_pool < 0:
            raise ValueError("Mana pool cannot be negative")

        self.attack_points = attack
        self.health = health
        self.defense = defense
        self.mana_pool = mana_pool

    def play(self, game_state: dict) -> dict[str, Any]:
        try:
            battlefield = game_state["battlefield"]
            current_mana = game_state["current_mana"]
        except KeyError as exc:
            return {"error": f"Missing game state key: {exc.args[0]}"}

        if not isinstance(battlefield, list):
            return {"error": "battlefield must be a list"}
        if not isinstance(current_mana, int):
            return {"error": "current_mana must be an integer"}
        if not self.is_playable(current_mana):
            return {"error": "Not enough mana to play this card"}

        battlefield.append(self)
        game_state["current_mana"] = current_mana - self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed to battlefield",
        }

    def attack(self, target) -> dict[str, Any]:
        target_name = getattr(target, "name", str(target))
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_points,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        if incoming_damage < 0:
            return {"error": "incoming_damage cannot be negative"}

        damage_blocked = min(self.defense, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            "attack": self.attack_points,
            "defense": self.defense,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict[str, Any]:
        if not spell_name:
            return {"error": "spell_name cannot be empty"}
        if not targets:
            return {"error": "targets cannot be empty"}

        spell_costs = {"Fireball": 4, "Arcane Blast": 3, "Barrier": 2}
        mana_cost = spell_costs.get(spell_name, 2)
        if self.mana_pool < mana_cost:
            return {
                "error": "Not enough mana to cast spell",
                "required": mana_cost,
                "available": self.mana_pool,
            }

        self.mana_pool -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        if amount <= 0:
            return {"error": "Channel amount must be positive"}
        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            "mana_pool": self.mana_pool,
            "known_spells": ["Fireball", "Arcane Blast", "Barrier"],
        }

    def get_card_info(self) -> dict[str, Any]:
        base_info = super().get_card_info()
        base_info.update(
            {
                "type": "Elite",
                "attack": self.attack_points,
                "health": self.health,
                "defense": self.defense,
                "mana_pool": self.mana_pool,
            }
        )
        return base_info
