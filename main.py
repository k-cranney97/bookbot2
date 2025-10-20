def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    result = get_num_words(text)
    print(result)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return f"Found {len(words)} total words."


main()