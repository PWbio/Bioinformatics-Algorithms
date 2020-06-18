def sum_(object):
    if object == []:
        return 0
    return object[0] + sum(object[1:])

def len_(object):
    if object == []:
        return 0
    return 1 + len_(object[1:])

def max_(object):
    if len(object) == 2: # base case
        return object[0] if object[0] > object[1] else object[1]
    sub_max = max_(object[1:])
    return object[0] if object[0] > sub_max else sub_max # recursive base

def multiplication(object):
    for i in object:
        for j in object:
            print (i * j, end=" ")
        print()

def binary_search(object, search):
    object = sorted(object)
    print("Sorting Result:", object)
    low_index = 0
    high_index = len(object) - 1
    def binary_search_recursion(low=low_index, high=high_index):
        if low <= high:
            mid = (low + high) // 2
            if object[mid] == search:
                return mid
            elif object[mid] > search:
                return binary_search_recursion(low, mid-1)
            elif object[mid] < search:
                return binary_search_recursion(mid+1, high)
        else:
            return 'Not found'
    return binary_search_recursion()

x=[1,3,5,2,4,6]
sum_(x)
len_(x)
max_(x)
multiplication(x)
binary_search(x, 1)
