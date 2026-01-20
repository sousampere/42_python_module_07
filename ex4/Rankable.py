#!/usr/bin/python3

from abc import ABC, abstractmethod


class Rankable(ABC):
    @abstractmethod
    def __init__(self):
        self._wins = 0
        self._loses = 0

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        self._wins = wins
        return None

    @abstractmethod
    def update_loses(self, loses: int) -> None:
        self._loses = loses
        return None
    
    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
