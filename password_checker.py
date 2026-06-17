#---------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     18-06-2026
# Copyright:   (c) DELL 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------

import string

password = input("Enter your password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Uppercase check
if any(char.isupper() for char in password):
    score += 1

# Lowercase check
if any(char.islower() for char in password):
    score += 1

# Number check
if any(char.isdigit() for char in password):
    score += 1

# Special character check
if any(char in string.punctuation for char in password):
    score += 1

# Strength result
if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Moderate Password")
else:
    print("Strong Password")
