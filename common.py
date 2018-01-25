# ******5 most common--Question 2*******

filename = input("Enter file path: ")
filehandle = open(filename,'r')
content = filehandle.read()
words = content.split()
dictionary = {}

for word in words:
    if word in dictionary:
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1


for i in range(5):
    k = max(dictionary, key=dictionary.get)
    print(k, dictionary[k])
    del dictionary[k]

#Most Common
#Constitution.txt
#the 456
#of 348
#and 230
#shall 180
#to 155

#A tale of 2 cities
#the 7514
#and 4745
#of 4066
#to 3458
#a 2825

#twitter data
#a 1522
#bullying 1342
#to 1104
#the 1089
#bully 1071
