#!/usr/bin/python3

from ex2 import Combatable, Magical
from ex0 import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, rarity, damage, combat_type):
        super().__init__(name, cost, rarity)
        self._damage = damage
        self._combat_type = combat_type

    def play(self, game_state: dict) -> dict:
        return {}

    def attack(self, target) -> dict:
        return {
            'attacker': self._name,
            'target': target,
            'damage': self._damage,
            'combat_type': self._combat_type
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self._name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': amount,
            'total_mana': self._cost + amount,
        }

    def get_magic_stats(self) -> dict:
        return {}

    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self._name,
            'damage_taken': incoming_damage,
            'damage_blocked': 3,
            'still_alive': True
        }

    def get_combat_stats(self) -> dict:
        return {}
