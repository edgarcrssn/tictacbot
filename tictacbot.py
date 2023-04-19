import os

this_file_path = os.path.dirname(os.path.abspath(__file__))
gutenberg = os.path.join(this_file_path, "gutenberg.txt")


def tictacbot(
    str_to_search: str, remaining_letters: list[str]
) -> dict["word":str, "score":int] | None:
    if str_to_search.isalpha():
        str_to_search = str_to_search.lower()

        best_word = {"word": None, "score": -1}
        with open(gutenberg, "r", encoding="utf-8") as f:
            for word in f:
                if str_to_search in word:
                    score = len(set(word) & set(remaining_letters))
                    word_found = {"word": word.strip(), "score": score}
                    if best_word["score"] < word_found["score"]:
                        best_word = word_found
            return best_word
