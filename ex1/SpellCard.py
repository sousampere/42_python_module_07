#!/usr/bin/python3

from ex0 import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self._effect_type = effect_type
    
    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self._name,
            'mana_used': self._cost,
            'effect': self._effect_type
        }
    
    def resolve_effect(self, targets: list) -> dict:
        pass
