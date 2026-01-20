#!/usr/bin/python3



from ex4 import TournamentCard, TournamentPlatform


print('')

print('=== DataDeck Tournament Platform ===')

print('')

print('Registering Tournament Cards...')

print('')
platform = TournamentPlatform()
dragon = TournamentCard(
    name="Fire Dragon",
    cost=5,
    rarity=8,
    wins=0,
    loses=0,
    rating=1200,
    id="dragon_001"
)
wizard = TournamentCard(
    name="Ice Wizard",
    cost=5,
    rarity=8,
    wins=0,
    loses=0,
    rating=1150,
    id="wizard_001"
)
print(platform.register_card(dragon))

print('')

print(platform.register_card(wizard))

print('')

print("Creating tournament match...")

print(f'Match result: {platform.create_match('dragon_001', 'wizard_001')}')

print('')

print("Tournament Leaderboard:")
i = 1
cards = platform.get_leaderboard()
for card in cards:
    print(f"{i}: {card._name} - Rating: {card._rating} ({card._wins}-{card._loses})")
    i += 1

print('')

print('Platform Report:')
print(platform.generate_tournament_report())

print('')

print('=== Tournament Platform Successfully Deployed! ===')
print('All abstract patterns working together harmoniously!')