import random

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(
        CreatureCard("Fire Dragon", 5, "Legendary", attack=7, health=5)
    )
    deck.add_card(SpellCard("Lightning Bolt", 3, "Rare", effect_type="damage"))
    deck.add_card(
        ArtifactCard(
            "Mana Crystal",
            2,
            "Common",
            durability=3,
            effect="+1 mana per turn",
        )
    )

    print("Deck stats:", deck.get_deck_stats())

    random.seed(10)
    deck.shuffle()

    game_state = {"current_mana": 10, "battlefield": [], "artifacts": []}

    print("\nDrawing and playing cards:")
    while True:
        try:
            card = deck.draw_card()
        except IndexError:
            break
        card_type = card.get_card_info().get("type", "Unknown")
        print(f"Drew: {card.name} ({card_type})")
        print("Play result:", card.play(game_state))

    print(
        "\nPolymorphism in action: "
        "Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
