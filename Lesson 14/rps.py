import random
import time

print('-'*65)
print("Welcome to Rock, Paper, Scissors Bot!")
print()

print('Rock')
time.sleep(0.5)
print('Paper')
time.sleep(0.5)
print('Scissor')
time.sleep(0.5)
print()

userpick = input('Please select one of the three options displayed above. Good luck! ')
cpick = random.randint(1,3)
print()


time.sleep(1)
print('Rock...')
time.sleep(1)
print('Paper...')
time.sleep(1)
print('Scissor...')
time.sleep(1)
print('Says...')
time.sleep(2)
print('SHOOT!')
print()

#1 is rock, 2 is paper, 3 is scissors
if userpick == 'Rock' and cpick == 1:
	print('You and me picked the same thing! Tied!')

elif userpick == 'Rock' and cpick == 2:
	print('Ha! Paper beats rock! You lose!')

elif userpick == 'Rock' and cpick == 3:
	print('Dang it! Rock beats scissor! You won... :(')

elif userpick == 'Paper' and cpick == 1:
	print('Dang it! Paper beats rock! You won... :(')

elif userpick == 'Paper' and cpick == 2:
	print('You and me picked the same thing! Tied!')

elif userpick == 'Paper' and cpick == 3:
	print('Ha! Scissor beats paper! You lose!')

elif userpick == 'Scissor' and cpick == 1:
	print('Ha! Rock beats scissor! You lose!')

elif userpick == 'Scissor' and cpick == 2:
	print('Dang it! Scissor beats paper! You won... :(')

elif userpick == 'Scissor' and cpick == 3:
	print('You and me picked the same thing! Tied!')

print('-'*65)






