#password_gen
#authored by mark minchoff

#import mods
import string
import random

#welcome message
print('Welcome to a "Password Generator"!')

#user inputs the length of password
#\n creates a new line
length = int(input('\nEnter the length of the password: '))

#defining data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combine the data
all = lower + upper + num + symbols

#random module
temp = random.sample(all, length)

password = "".join(temp)

#print the password
print(password)
