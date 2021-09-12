import random

num = random.randint(1,10)
for i in range(0,3):
    user = int(input("Guess the number: "))
    if user == num:
        print(f"Congratulations! {num} is the right number!")
        break
if user != num:
    print(f"Sorry, Please try again later!")