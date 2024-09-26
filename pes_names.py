import random

char_map = {
    "a": ["a", "ay", "ar"],
    "b": ["b", "d", "v", "p"],
    "c": ["c", "s", "k"],
    "d": ["b", "d", "p"],
    "e": ["i", "e", "er"],
    "f": ["f", "ef"],
    "g": ["g", "k", "j"],
    "h": ["h"],
    "i": ["i", "e"],
    "j": ["j", "g", "gy", "y"],
    "k": ["k", "q", "g"],
    "l": ["l", "el", "il"],
    "m": ["n", "m", "um", "em"],
    "n": ["n", "m", "un"],
    "o": ["o", "u"],
    "p": ["p", "b", "d"],
    "q": ["q", "ki", "ku"],
    "r": ["r", "b"],
    "s": ["s", "es", "ss"],
    "t": ["t", "d"],
    "u": ["u", "iu", "o"],
    "v": ["v", "f", "vi"],
    "w": ["w", "u", "v"],
    "x": ["x", "ex", "ix"],
    "y": ["y", "i", "ui", "ai"],
    "z": ["z", "s", "th"],
}

def get_name():
    while True:
        name = input("Enter a name to pessimate (or type 'quit' to exit): ")
        if name.strip() == '':
            print("Input cannot be empty. Please try again.")
        elif name.lower() == 'quit':
            return None, None
        else:
            max_length = len(name)
            return name, max_length

def pessimate(n, m):
    pes_name = ""
    length = 0
    for i, char in enumerate(n):
        if length > m + 3:
            break
        if i == 0:  # Keep the first character
            pes_name += char
            length += 1
        else:
            letter = char.lower()
            if letter in char_map:
                replacement = random.choice(char_map[letter])
                pes_name += replacement
                length += len(replacement)
            else:
                pes_name += char
                length += 1
    return pes_name.title()

def main():
    while True:
        n, m = get_name()
        if n is None:
            break
        elif n:
            print(pessimate(n, m))

main()
