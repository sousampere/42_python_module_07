#!/usr/bin/python3

from ex4 import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self._cards = []
        self._matches = 0

    def register_card(self, card: TournamentCard) -> str:
        self._cards.append(card)
        return f"{card._name} (ID: {card._id}):\n\
- Interfaces: [Card, Combatable, Rankable]\n\
- Rating: {card._rating}\n\
- Record: {card._wins}-{card._loses}"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self._matches += 1
        win_r = -1
        los_r = -1
        for card in self._cards:
            if card._id == card1_id:
                card._rating += 16
                win_r = card._rating
                card._wins += 1
            if card._id == card2_id:
                card._rating -= 16
                card._loses += 1
                los_r = card._rating
        return {
            'winner': card1_id,
            'looser': card2_id,
            'winner_rating': int(win_r),
            'loser_rating': int(los_r)
        }

    def get_leaderboard(self) -> list:
        self._cards.sort(key=lambda x: x._rating, reverse=True)
        return self._cards

    def generate_tournament_report(self) -> dict:
        sum = 0
        for card in self._cards:
            sum += card._rating
        return {
            'total_cards': len(self._cards),
            'matches_played': self._matches,
            'avg_rating': sum / len(self._cards),
            'platform_status': 'active',
        }
