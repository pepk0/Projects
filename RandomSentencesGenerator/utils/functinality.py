from random import randint


def get_random_word(path: str) -> str:
    with open(f"RandomSentencesGenerator\\text\\{path}", "r") as txt_file:
        lines = txt_file.readlines()
        last_word = len(lines) - 1
        word_choice = randint(0, last_word)
    return lines[word_choice].strip()


def make_sentence() -> str:
    sentence = ""
    file_paths = [
        "names.txt",
        "cities.txt",
        "adverbs.txt",
        "verbs.txt",
        "nouns.txt",
        "details.txt"
    ]

    for index, file_path in enumerate(file_paths):
        try:
            word = get_random_word(file_path)
            if index == 0:
                word = f"{word.capitalize()} from"
            word = f"{word} "
            sentence += word
        except FileNotFoundError:
            return "Missing text file, or incorrect file path"
    return sentence.strip()
