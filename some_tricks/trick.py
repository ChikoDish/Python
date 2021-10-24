import sys

# multiple inputs in a single line is
# x,y,z = input('Enter number: ').split()
# print(x)
# print(y)
# print(z)


#list vs generators

my_list = [ i for i in range(2000)]
print(sum(my_list))
print(sys.getsizeof(my_list))