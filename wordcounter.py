def main():
    print("This program counts the number of given letters in an input phrase")
    lettersCount = input("Enter the letters to count (e.g., 'aeiou'): ").lower()
    inputPhrase = input("Enter your phrase: ")


    totalOccurencesOfLettersToCount = 0
    for character in inputPhrase:
        if character in lettersCount:
            totalOccurencesOfLettersToCount = totalOccurencesOfLettersToCount + 1

    
    print("Total occurences of '{}' in your phrase: {}".format(lettersCount, totalOccurencesOfLettersToCount))


if __name__ == "__main__":
    main()