from typing import Any

from ex0.Card import Card


VALID_EFFECT_TYPES = {"damage", "heal", "buff", "debuff"}


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        super().__init__(name, cost, rarity)

        if effect_type not in VALID_EFFECT_TYPES:
            raise ValueError(
                f"Invalid effect_type: {effect_type}. "
                f"Must be one of {VALID_EFFECT_TYPES}"
            )

        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict[str, Any]:
        try:
            current_mana = game_state["current_mana"]
        except KeyError as exc:
            return {"error": f"Missing game state key: {exc.args[0]}"}

        if not isinstance(current_mana, int):
            return {"error": "current_mana must be an int"}
        if not self.is_playable(current_mana):
            return {"error": "Not enough mana to play this card"}

        game_state["current_mana"] = current_mana - self.cost

        effect_messages = {
            "damage": f"Deal {self.cost} damage to target",
            "heal": f"Restore {self.cost} health to target",
            "buff": f"Buff target with +{self.cost} power",
            "debuff": f"Debuff target with -{self.cost} power",
        }

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_messages[self.effect_type],
        }

    def resolve_effect(self, targets: list) -> dict[str, Any]:
        if not targets:
            return {"error": "No targets provided"}

        resolved: list[str] = []
        for target in targets:
            resolved.append(
                f"{self.effect_type} applied to {target}"
            )

        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets_affected": len(targets),
            "results": resolved,
        }

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Spell",
            "effect_type": self.effect_type,
        }
