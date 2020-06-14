def find_smallest(list):
    smallest_num = list [0]
    smallest_index = 0
    for i in range (1, len(list)):
        if list[i] < smallest_num:
            smallest_num = list[i]
            smallest_index = i
    return smallest_index

def selection_sort(list):
    sorted_list = []
    for i in range (len(list)):
        smallest = find_smallest(list)
        sorted_list.append(list.pop(smallest))
    return sorted_list

x = [17,5,47,9,43]
selection_sort(x)