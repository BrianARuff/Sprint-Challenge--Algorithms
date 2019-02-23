# define arr
array = [5, 25, -5, -25, 4, 16]

def bubble_sort(arr):
    # counter to exit out of the while loop
    count = 0
    while count < len(arr)-1:
        for i in range(len(arr)-1):
            # current > next item
            if arr[i] > arr[i+1]:
                # swap these items
                arr[i], arr[i+1] = arr[i+1], arr[i]
        count += 1
    return arr

print(bubble_sort(array))