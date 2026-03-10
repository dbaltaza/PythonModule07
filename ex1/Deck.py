import random

from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card instances can be added to the deck")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for index, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(index)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Cannot draw from an empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.cards:
            total_cost += card.cost
            card_type = card.get_card_info().get("type")
            if card_type == "Creature":
                creatures += 1
            elif card_type == "Spell":
                spells += 1
            elif card_type == "Artifact":
                artifacts += 1

        avg_cost = total_cost / total_cards if total_cards else 0.0
        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 2),
        }
