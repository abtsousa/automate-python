import random
print('What is your name?')
name = input()
print('Hello '+name+'! I\'m thinking of a number between 1 and 20. Take a guess.')

secret = random.randint(1,20)

guesses = 0
while guesses < 6:
    try:
        guess = int(input())
        if guess<1 or guess>20:
            print('Please enter a number between 1 and 20.')
        else:
            guesses +=1
            if guess!=secret and guesses==6:
                print('Nope. I was thinking of ' + str(secret)+'. Better luck next time!')
            elif guess>secret:
                print('That\'s too high. Try again.')
            elif guess < secret:
                print('That\'s too low. Try again.')
            else:
                print('You solved it in', guesses, 'tries!')
    except ValueError:
        print('Please enter a valid number.')
