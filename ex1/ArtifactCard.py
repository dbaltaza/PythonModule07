from typing import Any

from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive int")
        if not isinstance(effect, str) or not effect:
            raise ValueError("Effect must be a non-empty string")

        self.durability = durability
        self.effect = effect

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

        artifacts = game_state.setdefault("artifacts", [])
        artifacts.append(self)

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict[str, Any]:
        if self.durability <= 0:
            return {"error": "Artifact is destroyed"}

        self.durability -= 1
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_remaining": self.durability,
        }

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Artifact",
            "durability": self.durability,
            "effect": self.effect,
        }
