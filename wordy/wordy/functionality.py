from itertools import permutations as permut

PATH = r" " #  <<<< set text file path here

def get_words(characters: str, digits=None) -> list:
    if digits == None:
        digits = len(characters)

    permutations = permut(characters, digits)
    result = ["".join(word) for word in permutations]

    return result


def validate_words(characters: str, digits=None) -> str:

    words = get_words(characters, digits)
    results = ""
    with open(PATH, "r", encoding="utf-8") as valid_words:
        for word in valid_words:
            word = word.strip()
            if word in words:
                results += f"{word} "


    return f"\nНамерени думи: {results}\n"
