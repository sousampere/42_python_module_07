#!/usr/bin/python3


from ex0 import Card
import random


class Deck:
    def __init__(self):
        self._cards = []

    def add_card(self, card: Card) -> None:
        self._cards.append(card)
        return None

    def remove_card(self, card_name: str) -> bool:
        for card in self._cards:
            if card._name == card_name:
                self._cards.remove(card)
                return True
        return False

    def suffle(self) -> None:
        random.shuffle(self._cards)
        return None

    def draw_card(self) -> Card:
        for card in self._cards:
            match type(card).__name__:
                case "CreatureCard":
                    t = 'Creature'
                case "ArtifactCard":
                    t = 'Artifact'
                case "SpellCard":
                    t = 'Spell'
            print(f'Drew: {card._name} ({t})')
            print(f'Play result: {card.play({})}\n')

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        costs = []
        for card in self._cards:
            costs.append(card._cost)
            match type(card).__name__:
                case "CreatureCard":
                    creatures += 1
                case "ArtifactCard":
                    artifacts += 1
                case "SpellCard":
                    spells += 1
        return {
            'total_cards': len(self._cards),
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': sum(costs) / len(costs),
        }
