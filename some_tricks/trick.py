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

list1 = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6]
print(Counter(list1))
