# def transition(phrase):
#     translate = ""
#     for latter in phrase:
#         if latter in 'AEIOUaeiou':
#             translate = translate + 'g'
#         else:
#             translate = translate + latter
#     return translate          
# print(transition(input("Enter a phrase: ")))




# n = int(input("Enter a number: "))
# x = range(n)
# for i in x:
#     print(i*i)



# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#         else: leap = True
#     return leap

# year = int(input())
# print(is_leap(year))


# n = int(input("Enter  a number: "))
# for i in range(n+1):
#     if i != 0:
#         print(i, end='')

## Directory merge

# dir = {"name": "Ankit", "city": "NY"}
# dir1 = {"name1": "Rock", "city1": "NY"}
# merged = {**dir, **dir1}
# print(merged)

## Print a string n times

# n = 8
# print("Yo " * n)


## Retrieve the Last Element of a List

# colors = ['Red', 'Green', 'Yellow']

# #Using brute force method
# print(colors[len(colors) -1])

# #Using negative indeces
# print(colors[-1])

# #pop method 
# print(colors.pop())
