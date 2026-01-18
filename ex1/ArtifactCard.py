#!/usr/bin/python3


from ex0 import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self._effect = effect
        self._durability = durability

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self._name,
            'mana_used': self._cost,
            'effect': self._effect}

    def activate_ability(self) -> dict:
        pass
