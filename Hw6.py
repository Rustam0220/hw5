def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def binary_search(element, lst):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1


unsorted_lst = [50, 29, 49, 41, 37, 100, 87, 98]
sorted_lst = bubble_sort(unsorted_lst)
print(sorted_lst)

element_to_find = 49
index = binary_search(element_to_find, sorted_lst)
if index != -1:
    print(f"Элемент {element_to_find} найден на позиции {index}.")
else:
    print(f"Элемент {element_to_find} не найден.")