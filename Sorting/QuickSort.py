def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    smaller = []
    greater = []

    for element in arr[:-1]:
        if element <= pivot:
            smaller.append(element)
        else:
            greater.append(element)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


array = [5, 2, 9, 1, 7, 6, 3]
sorted_array = quick_sort(array)
print(sorted_array)
