def getWord(filename):
    fileHandle = open(filename, 'r')
    content = fileHandle.read
    list = content.split
    random.choice(list)

def antonyms(sentence):
    fileHandle = open("antonyms.txt", 'r')
    lines = fileHandle.readlines()

    for i in range (len(sentence)):
        for line in antonyms:
            words = line.split()
            for j in range (len(words)-1):
                if words[j] == sentence[i]:
                    words.remove(words[j])
                    sentence[i] = random.choice(words)



def printFunct():
    sentence = getWord("subject.txt") + " " + getWord("verbs.txt") + " " + getWord("prepositions.txt") + " " + randomWord("articles.txt") + " " + randomWord("nouns.txt")
    print(sentence)
