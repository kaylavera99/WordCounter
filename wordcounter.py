def getInputPhrase():
     return input("Enter your phrase: ").lower()


def gettotalOccurencesOfLettersToCount(inputPhrase, lettersCount):
    totalOccurences = 0
    for character in inputPhrase:
        if character in lettersCount:
            totalOccurences = totalOccurences + 1
    return totalOccurences

def main():
    print("This program counts the number of given letters in an input phrase")
    lettersCount = input("Enter the letters to count (e.g., 'aeiou'): ").lower()
    inputPhrase = getInputPhrase()
    totalOccurencesOfLettersToCount = gettotalOccurencesOfLettersToCount(inputPhrase, lettersCount)
    print("Total occurences of '{}' in your phrase: {}".format(lettersCount, totalOccurencesOfLettersToCount))

if __name__ == "__main__":
    main()