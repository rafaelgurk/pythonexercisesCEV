# Guessing game
from random import randint
mac = randint(0, 10)
numb = int(input('Try>> '))
atte = 1
while numb != mac:
    if numb < mac:
        print('More...')
        numb = int(input('Try again>> '))
        atte += 1
    else:
        print('Less...')
        numb = int(input('Try again>> '))
        atte += 1
print(f'You win!! Needed {atte} attempt(s)')
print('--> {} <--'.format(mac))
