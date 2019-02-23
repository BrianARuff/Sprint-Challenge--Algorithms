arr = [5, 3, 25, 12, -3, 0, 1]

def advanced_bubble_sort(arr):
    count = 0
    while count < len(arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
            count += 1
        if count == len(arr)-1:
                break
    return arr

print(advanced_bubble_sort(arr))
