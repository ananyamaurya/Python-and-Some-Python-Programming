import sys
from random import randint
sys.argv


start = int(sys.argv[1])
end = int(sys.argv[2])
num = randint(start,end)
print(f'Guess the number between {start} and {end}\n')
while True:
    try:
        temp = int(input('\nYour Guess :::::  '))
        if start > temp or temp > end :
            print('Enter a valid number !!!')
            continue
    except ValueError:
        print('Enter a valid number !!!')
        continue
    if(num == temp):
        print(''' \n\n\n    Congratulations!!!!!
            You WON.. ''')
        x = 'w'
        break
    x = str(input('''\n\n\n             YOU LOSE
        Wanna Try Again ??
Press Y for Yes and N to Exit the Game (Y/N) : '''))
    while True:
        if(x not in 'yYNn'):
            x= str(input('\nPress Y for Yes and N to Exit the Game (Y/N) : '))
            continue
        break
    if(x == 'Y' or x == 'y'):
            continue
    if(x == 'N' or x == 'n'):
            break
if(x!='w'):
    print('''\n\n\n           SAD TO SEE YOU GO ^___^
                    SEE YOU SOON ''')
        
        
