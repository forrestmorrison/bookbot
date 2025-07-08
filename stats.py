def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_counts = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1
    return char_counts