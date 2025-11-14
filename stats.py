filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
       text = f.read()
    return text

def count_words():
    text = get_book_text(filepath)
    number_of_words = len(text.split())
    return number_of_words

def count_characters():
    text = get_book_text(filepath).lower()
    characters = {}

    for character in text:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def sort_on(characters):
    return characters["num"]

def sort_dict():
    characters = count_characters()
    info_list = []
    for character in count_characters():
        info = {
            "char": character,
            "num": characters[character],
        }
        info_list.append(info)
    info_list.sort(reverse=True, key=sort_on)
    return info_list



    

