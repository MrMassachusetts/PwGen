import os
import sys
import string
from random import randint
from random import shuffle
version = 1.0
print('PwGen by MrMassachusetts')
print('Version', version)
"""print('Do you want to:')
print('1. Check if your current password is in a wordlist')
print('2. Generate a password and check')"""
type = 2
type = int(type)
if type in (1, 2):
    if type == 1:
        print('Please enter the password you want to check:')
        pw = input('> ')
    elif type == 2:
        bk = list(string.ascii_lowercase)
        bg = list(string.ascii_uppercase)
        z = list(string.digits)
        sz = list('!°"§$%&/()=?}][{~#*+-.,_:;<>')
        shuffle(bk)
        shuffle(bg)
        shuffle(z)
        shuffle(sz)
        print('How many characters should you password have?')
        print('(At least 10 are recommended)')
        print('Maximum: 1000')
        char = input('> ')
        char = int(char)
        char -= 1
        pwd = []
        while char>=0:
            type = randint(1, 5)
            if type == 1:
                ran = randint(0, 25)
                pwt = bk[ran]
                pwd.extend([pwt])
                char-=1
            elif type == 2:
                ran = randint(0, 25)
                pwt = bg[ran]
                pwd.extend([pwt])
                char-=1
            elif type == 3:
                ran = randint(0, 9)
                pwt = z[ran]
                pwd.extend([pwt])
                char-=1
            elif type in (4, 5):
                ran = randint(0, 27)
                pwt = sz[ran]
                pwd.extend([pwt])
                char-=1
else:
    print('')
print('Your new generated password is:')
print(''.join(pwd))
input('Press enter to exit')

