def reverse_word(text):
    if isinstance(text, int):
        raise TypeError("Input must be a integer")
    return text[::-1]

def count_vowels(text):
    if isinstance(text, int):
        raise TypeError("Input must be a integer")
    count = 0

    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count

def word_count(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    words = text.split()
    return len(words)


if __name__ == "__main__":
    print(reverse_word("Knowledge")) 
    print (count_vowels("Energy")) 
    print (word_count("Hi Python World")) 
