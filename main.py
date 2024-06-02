def count_words(words):
    return len(words.split())

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read() 
        # print(file_contents)
        print(f"word count: {count_words(file_contents)}")

main()