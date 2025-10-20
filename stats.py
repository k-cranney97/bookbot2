def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    total = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in total:
            total[char] = 1
        else:
            total[char] += 1
    return total

def sort_on(d):
    return d["num"]


def sort_chars(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
        