#start by importing random.
from random import randint

#creating a function

def gameon():
    while True:
        x = randint(1,20)
        u = input('Select a number from 1-20 :\n')
#a try statement against using characters.
        try:
            userx = int(u)
        except:
            print('Not a number.')
            print('Try again')
            continue
        if userx == x:
            print('Congratulations\n You Won!!')
            break
        else:
            print('Ooo Noo\n Wrong choice.')
            print('Try Again')

#A welcome statement.
print('Welcome Player\n Select any number from 1 - 20 to Play.')

#calling the above function.
gameon()

#ENJOY PLAYING
