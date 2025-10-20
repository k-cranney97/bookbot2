from stats import get_num_words
from stats import get_num_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    result = get_num_words(text)
    num_char = get_num_characters(text)
    print(result)
    print(num_char)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()