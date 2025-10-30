import random

top_of_range = input('Type a number: ')

#to see if it's a number
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please type a number greater than 0 next time')
        quit()
else:
        print('Please type a number next time')
        quit()
random_number = random.randint(0,int(top_of_range))
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time')
        continue #brings us back at the top of the loop

    if user_guess == random_number:
        print('You got it!')
        break
        #you have many elif statements
    elif user_guess < random_number:
            print('Your guess is too low')
    else:
        print('Your guess is too high')

print(f'You guessed {guesses} times!') #or ('You guessed ', guesses, ' times!')





