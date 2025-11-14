from stats import count_words
from stats import count_characters
from stats import sort_dict
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(filepath)} total words")
    print("--------- Character Count -------")
    for dict in sort_dict(filepath):
        if dict["char"].isalpha() is True:
            print(f"{dict["char"]}: {dict["num"]}")
        else:
            pass
    print("============= END ===============")
    
main()