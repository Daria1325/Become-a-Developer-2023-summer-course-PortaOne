import re

def uniqueChar(text):
    cleanText = re.sub("[^a-zA-Z\s]+", "", text)
    cleanText = cleanText.split()
    uniqueLetters = []
    for word in cleanText:
        for char in word:
            count = word.count(char)
            if count == 1:
                uniqueLetters.append(char)
                break


    for letter in uniqueLetters:
        if uniqueLetters.count(letter) == 1:
            return letter

letter = uniqueChar("C makes it easy for you to shoot yourself in the foot. C++ makes that harder, but when you do, it blows away your whole leg. (с) Bjarne Stroustrup")

print(letter)
