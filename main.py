import sys

def main():
    if len(sys.argv) == 1:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    print_report(book_path, word_count, char_count)

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        #print(file_content)
        return file_content

from stats import count_words

from stats import count_characters

from stats import print_report

main()