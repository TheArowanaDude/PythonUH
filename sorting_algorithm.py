def sort(list):
    lesser = []
    greater = []
    if(len(list) < 2):
        return list
    else:
         lesser = [i for i in list[1:] if (i <= base)]
         greater = [i for i in list[1:] if(i > base)]
         return sort(lesser) + [base] + sort(greater)

print([3, 4, 5, 10, 11, 15])
