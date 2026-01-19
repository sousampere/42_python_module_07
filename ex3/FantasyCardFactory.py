#!/usr/bin/python3

from ex0 import Card, CreatureCard
from ex3 import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self._cards = []
        self._creatures = ['dragon', 'goblin']
        self._spells = ['fireball']
        self._artifacts = ['mana_ring']

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        card = CreatureCard(name_or_power, 1, 'Legendary', 1, 20)
        self._cards.append(card)
        return (card)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        card = CreatureCard(name_or_power, 1, 'Legendary', 1, 20)
        self._cards.append(card)
        return (card)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        card = CreatureCard(name_or_power, 1, 'Legendary', 1, 20)
        self._cards.append(card)
        return (card)

    def create_themed_deck(self,
                           name_or_power: str | int | None = None) -> Card:
        card = CreatureCard(name_or_power, 1, 'Legendary', 1, 20)
        self._cards.append(card)
        return (card)

    def get_supported_types(self) -> dict:
        return {
            'creatures': self._creatures,
            'spells': self._spells,
            'artifacts': self._artifacts,
            }
