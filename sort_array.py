def sort_array(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j] <= arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


enter_arr = [45, 78, 3, 65, 96]
print(sort_array(enter_arr))
