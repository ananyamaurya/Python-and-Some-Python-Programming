#Characters that should exist in a password
salphabets = 'abcdefghijklmnopqrstuvwxyz'
calphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '!@#$%&*'

#requesting username and password
user_name = input('Enter your username :: ')
pass_word = input('Enter Your Password :: ')

#validating length of password
if(len(pass_word)>25):
    print('\nPassword must be smaller than 25 characters')
    pass_word = input('Enter Your Password :: ')
if(len(pass_word)<8):
    print('\nPassword must be greater than 8 characters')
    pass_word = input('Enter Your Password :: ')

#checking if password contains the required characters
b_calpha,b_salpha,b_num,b_sym = False,False,False,False
for i in pass_word:
    if ( i in salphabets): b_salpha = True
    if ( i in calphabets): b_calpha = True
    if ( i in numbers): b_num = True
    if ( i in symbols): b_sym= True

print(f'\nYour password is {len(pass_word)} characters long', )


#deducing the strength of password
if( b_salpha and b_num and b_sym and b_calpha):
    print('\nYour Pass word is Very Strong')
elif ((b_salpha and b_num and b_sym) or (b_num and b_sym and b_calpha)):
    print('\nYour Pass word is Strong')
elif(b_salpha and b_num and b_calpha):
    print('\nYour Pass word is Moderate')
else:
    print('\nYour Pass word is Weak')
    
