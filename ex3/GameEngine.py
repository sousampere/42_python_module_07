#!/usr/bin/python3

from ex3 import CardFactory, GameStrategy


class GameEngine:
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._factory = factory
        self._strategy = strategy
        self._turns = 0
        self._damage = 8
        print(f"Factory: {type(self._factory).__name__}")
        print(f"Strategy: {type(self._strategy).__name__}")

    def simulate_turn(self) -> dict:
        print(f"Strategy: {type(self._strategy).__name__}")
        dict = {
            'cards_played': [],
            'mana_used': 0,
            'targets_attacked': 'Enemy Player'
        }
        for card in self._factory._cards:
            play = card.play({})
            dict['cards_played'].append(play['card_played'])
            dict['mana_used'] += play['mana_used']
        print(f"Actions: {dict}")
        return dict

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self._turns,
            'strategy_used': type(self._strategy).__name__,
            'total_damage': self._damage,
            'cards_created': len(self._factory._cards)
        }
