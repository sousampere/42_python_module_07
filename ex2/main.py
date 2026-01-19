#!/usr/bin/python3

from ex2 import EliteCard

print('')
print('=== DataDeck Ability System ===')
print('')

print('EliteCard capabilities:')
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print(" Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

print('')

print('Playing Arcane Warrior (Elite Card):')
arcane_warrior = EliteCard('Arcane Warrior', 4, 'Legendary', 5, 'melee')

print('Combat phase:')
print('Attack result:', arcane_warrior.attack('Enemy'))
print('Defense result:', arcane_warrior.defend(2))

print('')

print('Magic phase:')
print(f"Spell cast: {arcane_warrior.cast_spell(
    'Fireball', ['Enemy1', 'Enemy2'])}")
print(f"Mana channel: {arcane_warrior.channel_mana(3)}")

print('')

print('Multiple interface implementation successful!')
