import random

from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    random.seed(14)
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Factory: FantasyCardFactory")
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")
    turn_result = engine.simulate_turn()
    print("Hand:", turn_result.get("hand"))
    print("Turn execution:")
    print("Strategy:", turn_result.get("strategy"))
    print("Actions:", turn_result.get("actions"))

    print("Game Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
