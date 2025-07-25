def count_words(text):
    num_words = len(text.split())
    #print(num_words)
    return num_words

def count_characters(text):
    characters_dict = {}
    characters_list = list(text.lower())
    for character in characters_list:
        if character.isalpha():
            if character in characters_dict:
                characters_dict[character] += 1
            else:
                characters_dict[character] = 1
    characters_dict_list = []
    for item in characters_dict:
        value = characters_dict[item]
        characters_dict_list.append({"char": item, "count": value})
    characters_dict_list.sort(reverse=True, key=sort_on)
    #print(characters_dict_list[0]["char"])
    return characters_dict_list

def sort_on(dict):
    return dict["count"]

def print_report(path, word, char):
    print(f"--- Begin report of {path} ---")
    print(f"{word} words found in the document")
    print("")
    for item in char:
        character = item["char"]
        count = item["count"]
        print(f"The {character} character was found {count} times")
        print(f"{character}: {count}")
    print("--- End report ---")