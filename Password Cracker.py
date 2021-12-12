import random

password = input("Enter your passwprd: ");

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*~./\|"

all = lower + upper + number + symbol
crackedPassword = 0;

while(crackedPassword != password):

    crackedPassword = "".join(random.sample(all, len(password)))
    print(crackedPassword)

print(f"Password found\nPassword is '{crackedPassword}'")
