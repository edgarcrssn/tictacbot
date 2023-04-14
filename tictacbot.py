import os

this_file_path = os.path.dirname(os.path.abspath(__file__))
gutenberg = os.path.join(this_file_path, "gutenberg.txt")
gutenberg_tictacbot = os.path.join(this_file_path, "gutenberg-tictacbot.txt")


def tictacbot(letters: str) -> str | None:
    if letters.isalpha():
        letters = letters.lower()

        with open(gutenberg_tictacbot, "r", encoding="utf-8") as f:
            for word in f:
                if letters in word:
                    word_found = word.strip()
                    return word_found

        # If word not found in gutenberg-tictacbot.txt
        with open(gutenberg, "r", encoding="utf-8") as f:
            for word in f:
                if letters in word:
                    word_found = word.strip()
                    with open(gutenberg_tictacbot, "a", encoding="utf-8") as f2:
                        f2.write(word_found + "\n")
                        return word_found

            return None
