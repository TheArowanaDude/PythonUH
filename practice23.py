def mergeSort(lst):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = len(lst) //2
        print(lst[0:middle])
        print(middle,"\n")
        left = mergeSort(lst[0:middle])


        right = mergeSort(lst[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left): #leftover
        result.append(left[i])
        i += 1
    while j < len(right): #leftover
        result.append(right[j])
        j += 1
    return result

list = [1,5,7,3,9,10]

print(mergeSort(list))
