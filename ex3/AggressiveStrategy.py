from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        available_mana = 5
        cards_played: list[str] = []
        mana_used = 0
        damage_dealt = 0
        targets_attacked = ["Enemy Player"]
        played_cards = []

        for card in sorted(hand, key=lambda current: current.cost):
            if card.cost > available_mana:
                continue

            game_state = {
                "battlefield": battlefield,
                "artifacts": [],
                "current_mana": available_mana,
            }
            result = card.play(game_state)
            if "error" in result:
                continue

            available_mana = game_state["current_mana"]
            mana_used += card.cost
            cards_played.append(card.name)
            played_cards.append(card)

            card_info = card.get_card_info()
            card_type = card_info.get("type", "")
            if card_type == "Creature":
                damage_dealt += card_info.get("attack", 0)
            elif isinstance(card, SpellCard) and card.effect_type == "damage":
                damage_dealt += 3

        for card in played_cards:
            hand.remove(card)

        if damage_dealt == 0:
            targets_attacked = []

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": targets_attacked,
                "damage_dealt": damage_dealt,
            },
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        prioritized = sorted(
            available_targets,
            key=lambda target: str(target).lower() != "enemy player",
        )
        return prioritized
