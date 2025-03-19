#the entry point to the program and code that doesn't fit elsewhere
import sys
from stats import count_words
from stats import count_characters
from stats import sort_character_count



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1] 
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}")
        words = get_book_text(filepath)
        print("----------- Word Count ----------")
        count_words(words)
        print("--------- Character Count -------")
        char_count_dict = count_characters(words)
        sorted_character_count = sort_character_count(char_count_dict)
        for dict in sorted_character_count:
            if dict["character"].isalpha():
                print(dict["character"]+":", dict["count"])
        

#call entrypoint last
main()