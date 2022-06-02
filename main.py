import random
options = ['R', 'P', 'S']
def choices():
    computer_choice = random.choice(options)
    player_choice = input('Enter an option: R for Rock, P for Paper, S for Scissors: ')
    if player_choice.upper() not in options:
        print('Error, invalid input. Please try again')
        player_choice = input('Enter an option: R for Rock, P for Paper, S for Scissors: ')
    return (computer_choice, player_choice.upper())

# players[0] is the computer and players[1] is the other player    
players = choices()
print('players choice is {} and computer choice is {}'.format(players[1], players[0]))
if players[0] == players[1]:
    print('its a tie please play again')
    players = choices()
if players[1] == 'R':
    if players[0] == 'S':
        print('player wins')
    else:
        print('computer wins')
elif players[1] == 'S':
    if players[0] == 'P':
        print('player wins')
    else:
        print('computer wins')
elif players[1] == 'P':
    if players[0] == 'R':
        print('player wins')
    else:
        print('computer wins')