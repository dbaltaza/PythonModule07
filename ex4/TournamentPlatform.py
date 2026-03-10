import random

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches: list[dict] = []
        self._next_id = 1

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise TypeError("Only TournamentCard instances can be registered")

        suffix = f"{self._next_id:03d}"
        card_id = f"{card.name.lower().replace(' ', '_')}_{suffix}"
        self.cards[card_id] = card
        self._next_id += 1
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            return {"error": "One or both card IDs are not registered"}
        if card1_id == card2_id:
            return {"error": "A card cannot battle itself"}

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        score1 = card1.attack_points + card1.health + random.randint(0, 3)
        score2 = card2.attack_points + card2.health + random.randint(0, 3)

        if score1 >= score2:
            winner_id = card1_id
            loser_id = card2_id
        else:
            winner_id = card2_id
            loser_id = card1_id

        winner = self.cards[winner_id]
        loser = self.cards[loser_id]
        winner.update_wins(1)
        loser.update_losses(1)

        result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }
        self.matches.append(result)
        return result

    def get_leaderboard(self) -> list:
        ranked = sorted(
            self.cards.items(),
            key=lambda item: (item[1].rating, item[1].wins),
            reverse=True,
        )
        leaderboard = []
        for index, (card_id, card) in enumerate(ranked, start=1):
            leaderboard.append(
                {
                    "rank": index,
                    "card_id": card_id,
                    "name": card.name,
                    "rating": card.rating,
                    "record": f"{card.wins}-{card.losses}",
                }
            )
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        if total_cards == 0:
            avg_rating = 0
        else:
            total_rating = sum(card.rating for card in self.cards.values())
            avg_rating = int(round(total_rating / total_cards))

        status = "active" if total_cards > 0 else "inactive"
        return {
            "total_cards": total_cards,
            "matches_played": len(self.matches),
            "avg_rating": avg_rating,
            "platform_status": status,
        }
