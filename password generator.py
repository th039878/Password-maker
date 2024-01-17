import random

nouns = ["bear", "hippo", "tiger", "dog", "dalmation", "girraffe", "whale", "dolphin", "dragon", "lizard", "gecko", "platypus", "cat", "pikachu", "squirtle"]
adjectives = ["happy", "angry", "excited", "weird", "silly", "goofy", "wild", "nasty", "glompis", "funny", "hilarious", "gnarly", "gross", "lame", "weak"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

userNounInput = input("List nouns you would like to include, with a / after *every* word : ")
userNouns = []
userString = ""
for x in userNounInput:
    if x != "/":
        userString += x
    elif x == "/":
        nouns.append(userString)
        userString = ""

print(nouns)
numNoun = 0
numAdjective = 0
numSymbol = 0

for x in nouns:
    numNoun += 1

noun = random.randint(0, numNoun)
noun = nouns[noun - 1]

for y in adjectives:
    numAdjective += 1

adjective = random.randint(0, numAdjective)
adjective = adjectives[adjective - 1]

for z in symbols:
    numSymbol += 1

symbol = random.randint(0, numSymbol)
symbol = symbols[symbol - 1]

password = adjective + noun + symbol
password = password.capitalize()
print(password)