from ex0.CreatureCard import CreatureCard

def main():
    creature = CreatureCard("Dragon", cost=5, rarity="Rare", attack=7, health=6)

    # Test the methods
    print(creature.get_card_info())
    print(f"Playable with 5 mana: {creature.is_playable(5)}")
    print(f"Playable with 3 mana: {creature.is_playable(3)}")

    # Test play method
    game_state = {'battlefield': [], 'current_mana': 10}
    creature.play(game_state)
    print(f"Battlefield: {[c.name for c in game_state['battlefield']]}")
    print(f"Remaining mana: {game_state['current_mana']}")


if __name__ == '__main__':
    main()