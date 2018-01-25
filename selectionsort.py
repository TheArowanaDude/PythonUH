def selectionSort(lst):
    start = 0
    while start != len(lst):
        for i in range(start, len(lst)):
            if lst[i] < lst[start]:
                lst[start], lst[i] = lst[i], lst[start]
                print(lst)
        start += 1
    return lst

A= [75, 30, 9, 14, 1, 18]
A_sorted = selectionSort(A)
print('The sorted list is: ', A_sorted)
