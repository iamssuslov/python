import collections
import string


def count_unique_words(s: str):
    cleaned_string = s.translate(str.maketrans('', '', string.punctuation)).lower()
    words = cleaned_string.split()
    word_counter = collections.Counter(words)
    return len(word_counter)


if __name__ == '__main__':
    input_string = "Привет, мир! Привет всем."
    print(count_unique_words(input_string))
