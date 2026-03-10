import random

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creature_templates = [
            ("Fire Dragon", 5, "Legendary", 7, 5),
            ("Goblin Warrior", 2, "Common", 2, 2),
        ]
        self._spell_templates = [
            ("Lightning Bolt", 3, "Rare", "damage"),
            ("Frost Shield", 2, "Common", "buff"),
        ]
        self._artifact_templates = [
            ("Mana Ring", 2, "Rare", 3, "+1 mana per turn"),
            ("Ancient Staff", 4, "Legendary", 4, "+2 spell damage"),
        ]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            return CreatureCard(
                name="Custom Beast",
                cost=max(1, name_or_power // 2),
                rarity="Rare",
                attack=max(1, name_or_power),
                health=max(1, name_or_power + 1),
            )
        if isinstance(name_or_power, str):
            for template in self._creature_templates:
                if name_or_power.lower() in template[0].lower():
                    return CreatureCard(*template)

        selected = random.choice(self._creature_templates)
        return CreatureCard(*selected)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            return SpellCard(
                name="Arcane Burst",
                cost=max(1, name_or_power // 2),
                rarity="Rare",
                effect_type="damage",
            )
        if isinstance(name_or_power, str):
            for template in self._spell_templates:
                if name_or_power.lower() in template[0].lower():
                    return SpellCard(*template)

        selected = random.choice(self._spell_templates)
        return SpellCard(*selected)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            return ArtifactCard(
                name="Runed Totem",
                cost=max(1, name_or_power // 2),
                rarity="Rare",
                durability=max(1, name_or_power),
                effect="+1 attack to all creatures",
            )
        if isinstance(name_or_power, str):
            for template in self._artifact_templates:
                if name_or_power.lower() in template[0].lower():
                    return ArtifactCard(*template)

        selected = random.choice(self._artifact_templates)
        return ArtifactCard(*selected)

    def create_themed_deck(self, size: int) -> dict:
        if size <= 0:
            return {"theme": "fantasy", "cards": [], "size": 0}

        cards = []
        for _ in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                cards.append(self.create_creature())
            elif card_type == "spell":
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())

        return {"theme": "fantasy", "cards": cards, "size": len(cards)}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "lightning", "frost"],
            "artifacts": ["mana_ring", "ancient_staff"],
        }
