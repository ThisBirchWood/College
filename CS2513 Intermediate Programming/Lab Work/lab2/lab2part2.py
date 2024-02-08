def longestWord():
    inFile = open("myfile.txt", "r")
    data = inFile.readlines()
    data = [word.strip() for word in data]
    inFile.close()

    longest_words = []
    highest_count = 0

    for word in data:
        if len(word) > highest_count:
            highest_count = len(word)

    for word in data:
        if len(word) >= highest_count:
            longest_words.append(word)

    return longest_words


print(longestWord())