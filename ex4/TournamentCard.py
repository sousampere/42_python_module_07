#!/usr/bin/python3


from ex4 import Card, Combatable
from ex4.Rankable import Rankable
from abc import ABCMeta


class TournamentCard(Card, Combatable, Rankable, metaclass=ABCMeta):
    def __init__(self, name: str, cost: int, rarity: str, wins: int, loses: int, rating: int, id: str):
        super().__init__(name, cost, rarity)
        self.update_wins(wins)
        self.update_loses(loses)
        self._rating = rating
        self._id = id

    def play(self, game_state) -> dict:
        return super().play(game_state)

    def attack(self, target) -> dict:
        return super().attack(target)
    
    def defend(self, incoming_damage):
        return super().defend(incoming_damage)

    def calculate_rating(self) -> int:
        return self._rating
    
    def get_combat_stats(self):
        return super().get_combat_stats()
    
    def get_rank_info(self):
        return super().get_rank_info()
    
    def update_loses(self, loses):
        return super().update_loses(loses)
    
    def update_wins(self, wins):
        return super().update_wins(wins)

    def get_tournament_stats(self) -> dict:
        return {
            'wins': self._wins,
            'loses': self._loses,
            'rating': self._rating
        }
