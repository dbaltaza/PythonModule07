from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.hand: list = []
        self.battlefield: list = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy,
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            self.factory.create_creature("Dragon"),
            self.factory.create_creature("Goblin"),
            self.factory.create_spell("Lightning"),
        ]
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            return {"error": "Engine not configured"}

        hand_snapshot = [f"{card.name} ({card.cost})" for card in self.hand]
        turn_result = self.strategy.execute_turn(self.hand, self.battlefield)
        turn_actions = turn_result.get("actions", {})
        self.total_damage += turn_actions.get("damage_dealt", 0)
        self.turns_simulated += 1

        return {
            "hand": hand_snapshot,
            "strategy": self.strategy.get_strategy_name(),
            "actions": turn_actions,
        }

    def get_engine_status(self) -> dict:
        strategy_name = "None"
        if self.strategy is not None:
            strategy_name = self.strategy.get_strategy_name()

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
