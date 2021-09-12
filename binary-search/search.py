lst = [1, 3, 2, 4, 5, 6, 9, 8, 7, 10]
lst.sort()
first = 0
last = len(lst)-1
mid = first + last // 2
found = False
num = int(input("Please enter a number: "))
while (first <= last and not found):
    mid = first + last // 2
    if num == lst[mid]:
        print(f"{num} is at {mid} position")
        found = True
    else:
        if num < lst[mid]:
           last = mid - 1
        else:
            first = mid + 1
if found == False:
    print("Number not found")
