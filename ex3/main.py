#!/usr/bin/python3

from ex3 import AggressiveStrategy, FantasyCardFactory, GameEngine


print('')

print('=== DataDeck Game Engine ===')

print('')

engine = GameEngine()
factory = FantasyCardFactory()
factory.create_creature("Fire Dragon (5)")
factory.create_creature("Goblin Warrior (2)")
factory.create_spell("Lightning Bolt (3)")
strategy = AggressiveStrategy()
print('Configuring Fantasy Card Game...')

engine.configure_engine(factory, strategy)
print(f"Available types: {factory.get_supported_types()}")

print('')

print('Simulating aggressive turn...')
cards = []
for card in engine._factory._cards:
    cards.append(card._name)
print(f"Hand: {cards}")

print('')

print('Turn execution:')
engine.simulate_turn()

print('')

print('Game Report:')
print(engine.get_engine_status())

print('')

print('Abstract Factory + Strategy Pattern: Maximum flexibility achieved!')