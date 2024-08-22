def main():
    book_path = "frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words, chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    def sort_on(dict):
        return dict[1]

    char_list = sorted(chars_dict.items(), key=sort_on, reverse=True)
    for char, count in char_list:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


main()
