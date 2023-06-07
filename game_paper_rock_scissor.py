import random
import time

Player1 = 0
Player2 = 0
chooses = ['paper', 'rock', 'scissor']


def show_results(player):
    while True:
        choose_player = input(f'{player} chooses: ')
        if choose_player in chooses:
            return choose_player


def random_choose(lst):
    index = random.randint(0, len(lst) - 1)
    return lst[index]


def choose_player(choose_player1, choose_player2):
    if choose_player1 == choose_player2:
        print('draw')
        return 0

    result = {
        ('paper', 'rock'): 1,
        ('rock', 'scissor'): 1,
        ('scissor', 'paper'): 1
    }
    return result.get((choose_player1, choose_player2), -1)


print('Play paper/rock/scissor')

while Player1 != 3 and Player2 != 3:
    choose_player1 = show_results('Player1')

    print("Player2 is choosing...")
    time.sleep(2)
    choose_player2 = random_choose(chooses)

    print("Player2 chooses:", choose_player2)

    results = choose_player(choose_player1, choose_player2)

    if results == 1:
        print('Player1 win')
        Player1 += 1
    elif results == -1:
        print('Player2 win')
        Player2 += 1

if Player1 > Player2:
    print('Congratulation Player1!!')
else:
    print('Congratulation Player2!!')
