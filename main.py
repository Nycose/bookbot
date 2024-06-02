def count_words(words):
    return len(words.split())

def count_chars(words):
    char_map = {}
    for ch in words:
        lower_ch = ch.lower()
        if lower_ch.isalpha():
            if lower_ch in char_map:
                char_map[lower_ch] += 1
            else:
                char_map[lower_ch] = 1
    return char_map

def get_char_list(char_map):
    char_list = []
    for char in char_map:
        char_list.append({ "letter": char, "count": char_map[char] })
    return char_list

# Some useful comment
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read() 
        print(f"{count_words(file_contents)} words found in the document")
        char_list = get_char_list(count_chars(file_contents))
        for ch in char_list:
            print(f"The '{ch["letter"]}' character was found '{ch["count"]}' times")


main()