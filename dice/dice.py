import random
print("Press 1 for roll.. 2 for exit..\n")

while True:
    num = int(input("What do you want to do? \n"))

    if num == 1:
        roll = random.randint(1,6)
        print(roll)
    else:
        break