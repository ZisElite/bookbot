def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        words = count_words(file_contents)
        char_count = count_character_appearences(file_contents)
        print_statistics(words, char_count)

def count_words(text:str) -> int:
    return len(text.split())

def count_character_appearences(text:str) -> dict:
    characters = {}
    text = text.lower()
    for char in text:
        if char not in "abcdefghijklmnopqrstuvwxyz":
            continue
        if char not in characters.keys():
            characters[char] = 0
        characters[char] += 1
    return dict(sorted(characters.items()))

def print_statistics(words:int, char_count:dict) -> None:
    print("---------Statistics for Frankenstein---------")
    print(f"Word count: {words}\n")
    print("character | appearences")
    for char, times in char_count.items():
        print(f"{char}         | {times}")
    print("--------------End of statistics--------------")

if __name__ == "__main__":
    main()