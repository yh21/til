numbers = [800, 32, 4, 122, 766, 12, 98,53, 772, 8]

def merge_sort(num_list):

    if len(num_list) <= 1:
        return num_list
    
    mid = len(num_list) // 2
    left_list = merge_sort(num_list[:mid])
    right_list = merge_sort(num_list[mid:])
    return_array = list()

    while (True):
        if len(left_list) == 0:
            return_array += right_list
            break
        if len(right_list) == 0:
            return_array += left_list
            break
        if (left_list[0] <= right_list[0]):
            return_array.append(left_list[0])
            del(left_list[0])
        else:
            return_array.append(right_list[0])
            del(right_list[0])

    return return_array

print(merge_sort(numbers))

        
    