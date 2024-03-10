import random

def monty_hall():
    # Initialize doors
    doors = ['goat', 'goat', 'car']
    # Shuffle doors
    random.shuffle(doors)
    
    # Player selects a door
    player_choice = random.randint(0, 2)
    
    # Monty reveals a goat behind one of the other doors
    revealed_door = next(i for i in range(3) if i != player_choice and doors[i] == 'goat')
    
    # Player decides whether to switch or stay
    switch = random.choice([True, False])
    
    # If player decides to switch, choose the other unchosen door
    if switch:
        player_choice = next(i for i in range(3) if i != player_choice and i != revealed_door)
    
    # Player wins if they chose the door with the car
    return doors[player_choice] == 'car'

# Run simulation multiple times to see the winning probabilities
num_simulations = 1000000
switch_wins = 0
stay_wins = 0

for _ in range(num_simulations):
    if monty_hall():
        switch_wins += 1
    else:
        stay_wins += 1

print("Switching wins:", switch_wins)
print("Staying wins:", stay_wins)
print("Winning percentage when switching:", switch_wins / num_simulations)
print("Winning percentage when staying:", stay_wins / num_simulations)
