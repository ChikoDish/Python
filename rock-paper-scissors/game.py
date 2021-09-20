import random

options = ['Rock', 'Paper', 'Scissors']
computer_score = 0
player_score = 0
Playing = True
while Playing:
    player = input('Please choose Rock, Paper or Scissors or Quit for final score: ')
    computer = random.choice(options)
    if computer == player:
        print('Tie')
    elif player == 'Rock':
        if computer == 'Paper':
            print('Computer wins')
            computer_score += 1
        else:
            print('You wins')
            player_score += 1
    elif player == 'Paper':
        if computer == 'Scissors':
            print('Computer wins')
            computer_score += 1
        else:
            print('You wins')
            player_score += 1
    elif player == 'Scissors':
        if computer == 'Rock':
            print('Computer wins')
            computer_score += 1
        else:
            print('You wins')
            player_score += 1
    elif player == 'Quit':
        Playing = False
        if player_score == computer_score:
            print('Game Tied', player_score)
            break
        elif player_score > computer_score:
            print('You win with the score of ', player_score)
            break
        else:
            print('Computer wins with a score of ', computer_score)
            break

