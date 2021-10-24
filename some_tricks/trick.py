import sys
from typing import Counter

# multiple inputs in a single line is
# x,y,z = input('Enter number: ').split()
# print(x)
# print(y)
# print(z)


#list vs generators

# my_list = [ i for i in range(2000)]
# print(sum(my_list))
# print(sys.getsizeof(my_list))

# my_generator = (i for i in range(2000))
# print(sum(my_generator))
# print(sys.getsizeof(my_generator))


# arr = ['d','d','e','o']
# concatenate = ''.join(arr)
# print(concatenate)

#counter 

# list1 = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6]
# print(Counter(list1))


# dict1 = {1: 'one', 2: 'two', 4: 'four'}
# print(dict1.get(3))
# print(dict1.setdefault(3, 'Default Value'))


# Sort Complex Iterables in One Go
# Python built-in sorted() method can be used to sort any iterable in Python. The advantage of this sorted method is that it can sort any complex iterable easily.
# You can also specify the order of the sorting, i.e., ascending or descending, and this method will do all the hard work for you.
# data = [{'name': 'John', 'age': 21},
#         {'name': 'Max', 'age': 19},
#         {'name': 'Lisa', 'age': 22}
#        ]
# sorted_data = sorted(data, key=lambda x: x['age'])
# print(sorted_data)


# physics = 80
# chemistry = 80
# maths = 98

# condition = [physics > 60, chemistry > 60, maths > 60]
# print('Pass 'if all(condition) else 'Fail')
# print('Pass' if any(condition) else 'Fail')

# a = 100
# b = 200
# a, b = b, a  # swap values
# print(a)
# print(b)


def add_sub (num1, num2):
    add = num1 + num2
    sub = num1 - num2
    return add, sub

add, sub = add_sub(13,5)
print(add, sub)