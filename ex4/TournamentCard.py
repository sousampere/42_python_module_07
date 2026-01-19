#!/usr/bin/python3


from ex4 import Card, Combatable, Rankable


class TournamentCard(Card, Combatable, Rankable):
    def play(self, game_state) -> dict:
        return super().play(game_state)

    def attack(self, target) -> dict:
        return super().attack(target)

    def calculate_ratings(self) -> int:
        pass

    def get_tournament_stats(self) -> dict:
        pass

