import time
import random


def selectionSort(list):

    for i, num in enumerate(list):
        try:
            if(list[i+1] < num):
                list[i] = list[i+1]
                list[i+1] = num
                selectionSort(list)
        except IndexError:
            pass
    return list


def gen_rand(a,b,n):
    num_list = []
    for i in range(n):
        num = random.randint(a,b)
        num_list.append(num)
    return num_list





start = time.time()
selectionSort([gen_rand(1,1000, 1000)])
end = time.time()
print("The runtime of Binary Search is: " + str(end - start) + " sec")


for x in range(0,3):
    selectionSort([gen_rand(1,1000, 1000)])

def someFunction():
    start = time.time()
    while (time.time() - start < 30):
        selectionSort([gen_rand(1,1000, 1000)])

    return;
