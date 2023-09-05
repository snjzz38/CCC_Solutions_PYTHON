Word = input("")
RevWord = Word[::-1]
WordList = []
PalindromesList = []


for i in range(len(Word)-1):
    WordList.append(RevWord[i:])
    print(RevWord[i:])
    for j in range(1, len(Word)-i):
        print(RevWord[i:-j])
        # if RevWord[i: -j]:
        WordList.append(RevWord[i:-j])

for i in range(len(WordList)):
    if WordList[i] in Word:
        PalindromesList.append(len(WordList[i]))

if max(PalindromesList) == len(Word):
    print(len(Word))    
else:
    print(max(PalindromesList))
