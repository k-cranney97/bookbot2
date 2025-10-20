def get_num_words(text):
    words = text.split()
    return f"Found {len(words)} total words."

def get_num_characters(text):
    total = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in total:
            total[char] = 1
        else:
            total[char] += 1
    return total