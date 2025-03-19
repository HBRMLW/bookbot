#this file contains functions for analyzing the text
def count_words(file_text):
    word_list = file_text.split() 
    word_count = len(word_list)
    return print(f"Found {word_count} total words")

def count_characters(book_text_string):
    character_dict = {}
    string_list = book_text_string.split()
    for word in string_list:
        word = word.lower()
        for character in word:
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
    return character_dict

def sort_on(dict):
    return dict["count"]

def sort_character_count(dict):
    dictionary_list = []
    for item in dict:
        inter_dict = {}
        inter_dict["character"] = item
        inter_dict["count"] = dict[item]
        dictionary_list.append(inter_dict)
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
    
