import random

print('ROCK, PAPER, SCISSORS')
wins = losses = ties = 0
while True:
    # print(wins,'Wins,',losses,'Losses,',ties,'Ties')
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    print('\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit')
    move = input()
    if move == 'q':
        print('Goodbye!')
        break
    elif move == 'r':
        print('ROCK versus...')
    elif move == 'p':
        print('PAPER versus...')
    elif move == 's':
        print('SCISSORS versus...')
    else:
        print('Please enter a valid move.')
        continue
    cpu = ['r', 'p', 's'][random.randint(0, 2)]

    if cpu == 'r':
        print('ROCK!')
    elif cpu == 'p':
        print('PAPER!')
    elif cpu == 's':
        print('SCISSORS!')

    if move == cpu:
        print("It's a tie!")
        ties += 1
    elif (move == 'r' and cpu == 's') or (move == 'p' and cpu == 'r') or (move == 's' and cpu == 'p'):
        print("You win!")
        wins += 1
    else:
        print("You lose...")
        losses += 1
