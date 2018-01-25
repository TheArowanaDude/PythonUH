sentence = input("Input sentence")
keyword = input("Input keyword")
count = 0

for i in keyword:
    for x in sentence:
        if (i == x):
            count+=1

    print(i, count)
