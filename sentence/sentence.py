import random

def getWord(filename):
    fileHandle = open(filename, 'r')
    content = fileHandle.read()
    list = content.split
    random.choice(list)



num = int(input("Enter the number of sentences you want"))
for i in range(num):
    sentence = getWord("subject.txt") + " " + getWord("verbs.txt") + " " + getWord("prepositions.txt") + " " + randomWord("articles.txt") + " " + randomWord("nouns.txt")
    print(sentence)
