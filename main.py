from stats import get_num_words
from stats import get_num_characters
from stats import sort_chars
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_num_characters(text)
    ordered_char_dict = sort_chars(char_dict)
    print_report(book_path, num_words, ordered_char_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, ordered_char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in ordered_char_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()