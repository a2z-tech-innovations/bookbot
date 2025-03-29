def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_char_count(book_text):
    char_dict = {}
    for char in book_text:
        char = char.lower()
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char] = 1
    # print(char_dict)
    return char_dict

def get_sorted_chars(char_dict):
    sorted_chars = []

    # Only include alphabetical characters
    for char, count in char_dict.items():
        if char.isalpha():  # Check if character is alphabetical
            char_info = {"char": char, "count": count}
            sorted_chars.append(char_info)

    # Sort the list based on count (descending)
    sorted_chars.sort(key=lambda x: x["count"], reverse=True)

    return sorted_chars
