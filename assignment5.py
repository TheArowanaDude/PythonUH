filename = input("Enter file path: ")
filehandle = open(filename,'r')
content = filehandle.read()
words = content.split()
dictionary = {}

for word in words:
    if len(word) in dictionary:
        dictionary[len(word)] = dictionary[len(word)] + 1
    else:
        dictionary[len(word)] = 1

for letters in dictionary:
    print("size ", letters, dictionary[letters])
