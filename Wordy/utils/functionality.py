from itertools import permutations as permut


def get_words(characters: str, digits=None) -> list:
    if digits == None:
        digits = len(characters)
    permutations = permut(characters, digits)
    result = ["".join(word) for word in permutations]
    return result


def validate_words(characters: str, digits=None) -> str:
    path = r"Wordy\words.txt"
    words = get_words(characters, digits)
    results = "Намерени думи: "
    try:
        with open(path, "r", encoding="utf-8") as valid_words:
            for word in valid_words:
                word = word.strip()
                if word in words:
                    results += f"{word} "
    except FileNotFoundError:
        results = "Missing words file"
    return results
