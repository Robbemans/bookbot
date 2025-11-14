from stats import count_words
from stats import count_characters
from stats import sort_dict
from stats import filepath

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count_words()} total words")
    print("--------- Character Count -------")
    for dict in sort_dict():
        if dict["char"].isalpha() is True:
            print(f"{dict["char"]}: {dict["num"]}")
        else:
            pass
    print("============= END ===============")
    
main()