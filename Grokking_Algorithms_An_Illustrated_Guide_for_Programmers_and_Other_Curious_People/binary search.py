def binary_search(obj, search):
    """ Return index of search """
    obj_sort= sorted(obj)
    print('sorted object:', obj_sort[:10], '...')
    Highest_index = len(obj_sort) - 1
    Lowest_index = 0
    while Lowest_index <= Highest_index:
        Mid_index = (Highest_index + Lowest_index) // 2
        if obj_sort[Mid_index] == search:
            while Mid_index >= Lowest_index: # find left edge of identical obj
                if obj_sort[Mid_index - 1] != search:
                    Left_Mid_index = Mid_index
                    break
                Mid_index -= 1
            while Mid_index <= Highest_index: # find right edge of identical obj
                if obj_sort[Mid_index + 1] != search:
                    Right_Mid_index = Mid_index
                    break
                Mid_index += 1
            return print(
                'Found in index:', Mid_index, '\n'
                'Leftmost index:', Left_Mid_index, '\n'
                'Rightmost index:', Right_Mid_index
            )
        elif obj_sort[Mid_index] < search:
            Lowest_index = Mid_index + 1
        elif obj_sort[Mid_index] > search:
            Highest_index = Mid_index -1
        else:
            return 'Not exist'

x=[7,3,5,1,100,0.5,0,356,7777,5,10,11111,5,5,5,5,5,5]
binary_search(x, 0)

