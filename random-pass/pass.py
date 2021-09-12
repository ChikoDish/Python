import random

length = input("Please enter length of password: ")
if length.isnumeric():
    length = int(length)
    words="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = "".join(random.sample(words,length))
    print(password)
else:
    print("Please enter a number!")