from ex0.Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict):
        game_state['battlefield'].append(self)
        game_state['current_mana'] -= self.cost

    def get_card_info(self):
        return f"{self.name} - Cost: {self.cost}, Attack: {self.attack}, Health: {self.health}"

    def is_playable(self, available_mana: int):
        return available_mana >= self.cost
