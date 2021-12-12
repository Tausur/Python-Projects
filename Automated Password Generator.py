import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*"
length = 9

all = lower + upper + number + symbol

password = "".join(random.sample(all,length))

print("The password you generated is: ", password)