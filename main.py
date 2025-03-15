from stats import get_num_words, get_char_count, dic_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path) as f:
        text = f.read()
        num_words = get_num_words(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        char_count = get_char_count(text)
        char_list = dic_list(char_count)
        for item in char_list:
            print(f"{item['char']}: {item['count']}")
        print("============= END ===============")


main()
