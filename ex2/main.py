from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")

    elite_card = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Legendary",
        attack=5,
        health=10,
        defense=3,
        mana_pool=8,
    )

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {elite_card.name} (Elite Card):")
    game_state = {"battlefield": [], "current_mana": 7}
    print("Play result:", elite_card.play(game_state))

    print("\nCombat phase:")
    print("Attack result:", elite_card.attack("Enemy"))
    print("Defense result:", elite_card.defend(5))

    print("\nMagic phase:")
    print(
        "Spell cast:",
        elite_card.cast_spell("Fireball", ["Enemy1", "Enemy2"]),
    )
    print("Mana channel:", elite_card.channel_mana(3))

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
