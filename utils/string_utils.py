def capitalize_words(text):
    """Capitalize the first letter of each word in the text."""
    return text.title()


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def reverse_words(text):
    """Reverse the order of words in the text."""
    words = text.split()  # split into words
    # join the reversed words with a space
    reversed_words = " ".join(reversed(words))
    return reversed_words


if __name__ == "__main__":
    # this block is invisible to anyone who imports this file
    text = "hello world"
    print(capitalize_words(text))  # Hello World
    print(count_vowels(text))  # 3
    print(reverse_words(text))  # world hello
