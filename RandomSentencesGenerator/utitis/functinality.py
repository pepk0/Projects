from random import randint


def get_random_adverb() -> str:
    with open(r"RandomSentencesGenerator\text\adverbs.txt", "r") as txt_file:
        line = txt_file.readlines()
        word_choice = randint(1, 999)
    return line[word_choice].strip()


def get_random_city() -> str:
    with open(r"RandomSentencesGenerator\text\cities.txt", "r") as txt_file:
        line = txt_file.readlines()
        word_choice = randint(1, 79100)
    return line[word_choice].strip()


def get_random_detail() -> str:
    with open(r"RandomSentencesGenerator\text\details.txt", "r") as txt_file:
        line = txt_file.readlines()
        word_choice = randint(1, 124)
    return line[word_choice].strip()


def get_random_name() -> str:
    with open(r"RandomSentencesGenerator\text\names.txt", "r") as txt_file:
        line = txt_file.readlines()
        word_choice = randint(1, 5980)
    return line[word_choice].strip().capitalize()


def get_random_noun() -> str:
    with open(r"RandomSentencesGenerator\text\nouns.txt", "r") as txt_file:
        line = txt_file.readlines()
        word_choice = randint(1, 499)
    return line[word_choice].strip()


def get_random_verb() -> str:
    with open(r"RandomSentencesGenerator\text\verbs.txt", "r") as txt_file:
        line = txt_file.readlines()
        word_choice = randint(1, 490)
    return line[word_choice].strip()

def make_sentence() -> str:
    random_name = get_random_name()
    random_place = get_random_city()
    random_adverb = get_random_adverb()
    random_verb = get_random_verb()
    random_noun = get_random_noun()
    random_detail = get_random_detail()
    person = f"{random_name} from {random_place} "
    action = f"{random_adverb} {random_verb} a {random_noun} "
    detail = f"{random_detail}"
    return person + action + detail 
