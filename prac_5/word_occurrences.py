def main():
    # Dictionary for words and their frequencies
    words_to_count = {}
    # Prompt for user to enter string
    user_string = str(input("Please enter some words:- "))

    # Split string into separate words
    words = user_string.split()
    # Count occurrences of each word
    for word in words:
        frequency = words_to_count.get(word, 0)
        words_to_count[word] = frequency + 1

    words = list(words_to_count.keys())
    words.sort()

    max_length = max((len(word) for word in words))
    for word in words:
        print("{:{}} : {}".format(word, max_length, words_to_count[word]))
    # Neatly print words and number of occurrences


main()
