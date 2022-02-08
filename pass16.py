# Import Necesary Modules
import random
import string
import pyperclip3 as pc

print('Hello! Welcome to the password generator!'),

#Iimput for length of password
# length = int(input('\nEnter the length of your password: '))
length = 16


# define data
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
special = string.punctuation
string.ascii_letters

# Combine data
all = lowercase + uppercase + numbers + special

# Use random
temp = random.sample(all, length)

# Create password
password = ''.join(temp)

# Print password
print('\nHere is your Password: \n \n' +password +'\n')

# Copy text to clipboard
print('Password copied to clipboard')
pc.copy(password)