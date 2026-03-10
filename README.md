# DataDeck - Python Module 07 (42 Lisboa)

DataDeck is a modular trading card game engine built for **Python Module 07** at **42 Lisboa**.
The project focuses on abstract programming patterns in Python: abstract base classes, interfaces, polymorphism, multiple inheritance, and design patterns.

## Learning Goals

- Build and use abstract base classes (`abc.ABC`).
- Implement concrete classes from abstract contracts.
- Apply polymorphism with shared interfaces.
- Compose behaviors with multiple inheritance.
- Use Strategy and Abstract Factory patterns in a game-oriented architecture.
- Keep code organized, typed, and reusable across modules.

## Project Structure

```text
.
├── __init__.py
├── ex0
│   ├── __init__.py
│   ├── Card.py
│   ├── CreatureCard.py
│   └── main.py
├── ex1
│   ├── __init__.py
│   ├── SpellCard.py
│   ├── ArtifactCard.py
│   ├── Deck.py
│   └── main.py
├── ex2
│   ├── __init__.py
│   ├── Combatable.py
│   ├── Magical.py
│   ├── EliteCard.py
│   └── main.py
├── ex3
│   ├── __init__.py
│   ├── GameStrategy.py
│   ├── CardFactory.py
│   ├── AggressiveStrategy.py
│   ├── FantasyCardFactory.py
│   ├── GameEngine.py
│   └── main.py
└── ex4
    ├── __init__.py
    ├── Rankable.py
    ├── TournamentCard.py
    ├── TournamentPlatform.py
    └── main.py
```

## Requirements

- Python `3.10+`
- No external dependencies
- flake8-compliant style
- In-memory processing only (no file I/O for game logic)

## How to Run

Run all exercises from repository root:

```bash
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
```

## Lint

Recommended flake8 command for this project:

```bash
flake8 __init__.py ex0 ex1 ex2 ex3 ex4
```

## Exercise Summary

- `ex0`: Abstract `Card` foundation and first concrete card (`CreatureCard`).
- `ex1`: Multiple concrete card types + deck management (`Deck`).
- `ex2`: Ability interfaces (`Combatable`, `Magical`) + multiple inheritance (`EliteCard`).
- `ex3`: Strategy + Abstract Factory + orchestrator (`GameEngine`).
- `ex4`: Tournament system combining `Card`, `Combatable`, and `Rankable`.

## 42 Evaluation Notes

- Use absolute imports between exercises.
- Keep each exercise executable through `python3 -m exN.main`.
- Be ready to explain these concepts clearly in defense:
- ABCs enforcing consistency.
- Polymorphism simplifying deck/game logic.
- Interface composition improving extensibility.
- Strategy + Factory decoupling behavior and object creation.

## Author

- `dbaltazar`
