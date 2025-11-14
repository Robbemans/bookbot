from stats import count_words
from stats import count_characters

def main():
    print(f"Found {count_words()} total words")
    character_amount = count_characters()
    print(character_amount)
    
main()