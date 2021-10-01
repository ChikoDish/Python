def make_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print('* ', end="")
        print("\r")

def make_number_pyramid(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i, end="")
        print("\r")


def make_number_pyramid1(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(j, end="")
        print("\r")

make_pattern(5)
make_number_pyramid(5)
make_number_pyramid1(5)

