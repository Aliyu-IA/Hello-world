# Guessing Game

secret_number = 5
guess_count = 0
guess_limit = 3
while guess_limit > guess_count:
    guess = int(input("Guess? "))
    guess_count += 1
    if guess == secret_number:
        print('You have Won')
        break
    if guess_count == 3:
        print('Sorry, You have Failed')
    else:
        print('Try again!')
