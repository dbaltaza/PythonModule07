from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:\n")
    try:
        creature = CreatureCard(
            "Fire Dragon",
            cost=5,
            rarity="Legendary",
            attack=7,
            health=5,
        )
        combat_c = CreatureCard(
            "Goblin Warrior",
            cost=5,
            rarity="Rare",
            attack=1,
            health=5,
        )
    except (TypeError, ValueError) as e:
        print(f"ERROR: {e}!")
        return

    game_state = {"battlefield": [], "current_mana": 6}

    print("CreatureCard Info:")
    print(creature.get_card_info())

    print(f"\nPlaying {creature.name} with "
          f"{game_state['current_mana']} mana available:")
    print("Playable:", creature.is_playable(game_state["current_mana"]))
    print("Play result:", creature.play(game_state))

    print(f"\n{creature.name} attacks {combat_c.name}:")
    print("Attack result:", creature.attack_target(combat_c))

    game_state_test = {"battlefield": [], "current_mana": 3}
    print(f"\nTesting insufficient mana "
          f"({game_state_test['current_mana']} available)")
    print("Playable:", creature.is_playable(game_state_test["current_mana"]))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
