def binary_search(arr, value):
   
    mid_pos = len(arr)//2
    # print(arr, mid_pos)

    if len(arr) == 1:
        if arr[mid_pos] == value:
            return mid_pos
        else:
            return -1
    else:
        if arr[mid_pos] <= value:
            return binary_search(arr[mid_pos:], value)
        elif arr[mid_pos] > value:
            return binary_search(arr[:mid_pos], value) 
        


print(binary_search([1,2,3,4,5,6,7,8],6))