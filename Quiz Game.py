print('Welcome to the game')
playing = input('Do you want to play a game? ')

if playing.lower() != 'yes':
    quit()

print('Lets play!')
score = 0

answer = input('What is the capital city of Malawi? ')
if answer == 'Lilongwe':
    print('Correct answer!')
    score += 1
else:
    print('Wrong answer!')

answer = input('What is the header for queue in C++? ')
if answer == '<queue>':
    print('Correct answer!')
    score += 1
else:
    print('Wrong answer!')

answer = input('What language uses the Gin framework in web development? ')
if answer == 'Go':
    print('Correct answer!')
    score += 1
else:
    print('Wrong answer!')

answer = input('Which JavaScript frontend framework is used at organizational level? ')
if answer == 'Angular':
    print('Correct answer!')
    score += 1
else:
    print('Wrong answer!')
#str is for converting the input variable to string
print('You got ' + str(score) + ' questions correct')
print('Final Score = ' + str((score / 4) * 100 )+ '%')