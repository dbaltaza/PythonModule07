import random

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    random.seed(4)
    platform = TournamentPlatform()

    fire_dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=6,
        rating=1200,
    )
    ice_wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity="Rare",
        attack=5,
        health=5,
        rating=1150,
    )

    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)

    print(f"{fire_dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {fire_dragon.rating}")
    print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}")

    print(f"{ice_wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {ice_wizard.rating}")
    print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print("Match result:", match_result)

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']} - "
            f"Rating: {entry['rating']} ({entry['record']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
