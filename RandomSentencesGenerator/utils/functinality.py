from random import randint


def get_random_word(path: str) -> str:
    with open(path, "r") as txt_file:
        lines = txt_file.readlines()
        last_word = len(lines) - 1
        word_choice = randint(0, last_word)
    return lines[word_choice].strip()


def make_sentence() -> str | bool:
    sentence = ""
    file_paths = [
        r"RandomSentencesGenerator\text\names.txt",
        r"RandomSentencesGenerator\text\cities.txt",
        r"RandomSentencesGenerator\text\adverbs.txt",
        r"RandomSentencesGenerator\text\verbs.txt",
        r"RandomSentencesGenerator\text\nouns.txt",
        r"RandomSentencesGenerator\text\details.txt"
    ]

    for index, file_path in enumerate(file_paths):
        try:
            word = get_random_word(file_path)
            if index == 0:
                word = f"{word.capitalize()} from"
            word = f"{word} "
            sentence += word
        except FileNotFoundError:
            return False
    return sentence.strip()
