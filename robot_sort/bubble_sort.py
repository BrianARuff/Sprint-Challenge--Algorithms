arr = [5, 3, 25, 12, -3, 0, 1, 33, -4, 22, 100, -100]

def bubble_sort(arr):
    # coun tracker to break out
    count = 0
    while count < len(arr)-1:
        for i in range(len(arr)-1):
            # if current item greater than next item swap
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # work backwards from current index, if current item is less than the item before it then swap
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
            count += 1
        # The array should be sorted after the count equals the array length - 1
    return arr

print(bubble_sort(arr))

