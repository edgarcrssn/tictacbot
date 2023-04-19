from pynput import keyboard
import pyperclip
import pyautogui
from art import text2art
from colorama import init, Fore, Style
from tictacbot import tictacbot
import json
import random

init()

keys_pressed = []
remaining_letters = list("abcdefghijklmnopqrstuvwxyz")


def print_new_section(init: bool):
    global remaining_letters
    if not init:
        print("\n")
        print("_" * 50)
    label_colored = Fore.LIGHTYELLOW_EX + "Remaining letters: " + Style.RESET_ALL
    print(label_colored + json.dumps(remaining_letters) + "\n")
    print(Fore.LIGHTYELLOW_EX + "Keys pressed: " + Style.RESET_ALL)


def print_success_message():
    text = "Alphabet completed !"
    width = len(text) + 4
    border = "-" * width
    content = f"| {text} |"
    str = f"{border}\n{content}\n{border}"

    for i, char in enumerate(str):
        color = i % 6
        if color == 0:
            print(Fore.RED + char, end="")
        elif color == 1:
            print(Fore.YELLOW + char, end="")
        elif color == 2:
            print(Fore.GREEN + char, end="")
        elif color == 3:
            print(Fore.CYAN + char, end="")
        elif color == 4:
            print(Fore.BLUE + char, end="")
        elif color == 5:
            print(Fore.MAGENTA + char, end="")

    print(Style.RESET_ALL)


def update_remaining_letters(word_found: str):
    global remaining_letters
    remaining_letters = [
        letter for letter in remaining_letters if letter not in word_found
    ]
    if len(remaining_letters) == 0:
        print_success_message()
        remaining_letters = list("abcdefghijklmnopqrstuvwxyz")


def paste_word(word: str):
    print("\n" + Fore.LIGHTBLUE_EX + "Pasting..." + Style.RESET_ALL)
    pyperclip.copy(word)
    pyautogui.press("backspace", presses=len(keys_pressed) + 1)
    pyautogui.hotkey("command", "v")
    print(Fore.GREEN + "Pasted !" + Style.RESET_ALL)


def escape():
    print(Fore.LIGHTBLUE_EX + "Escaping..." + Style.RESET_ALL)
    keys_pressed.clear()
    print_new_section(init=False)


def search():
    print("\n" + Fore.LIGHTBLUE_EX + "Searching..." + Style.RESET_ALL)
    global remaining_letters
    letters = "".join(keys_pressed)
    best_word = tictacbot(letters, remaining_letters)

    if best_word and best_word["word"] and len(best_word["word"]):
        word_found: str = best_word["word"]
        word_score: int = best_word["score"]
        word_found_label_colored = Fore.LIGHTYELLOW_EX + "Found: " + Style.RESET_ALL
        word_found_colored = word_found.replace(letters, Fore.GREEN +  letters + Style.RESET_ALL)
        score_label_colored = Fore.LIGHTYELLOW_EX + "Score: " + Style.RESET_ALL
        score = str(word_score) + '/' + str(len(remaining_letters))
        if word_score == len(remaining_letters):
            score = Fore.GREEN + score + Style.RESET_ALL

        print(
            word_found_label_colored
            + word_found_colored
            + " - "
            + score_label_colored
            + score
        )
        update_remaining_letters(word_found)
        paste_word(word_found)
    else:
        print(Fore.RED + "Not found" + Style.RESET_ALL)
    keys_pressed.clear()
    print_new_section(init=False)


def on_press(key):
    try:
        key_char = key.char
        if not key_char.isalpha():
            return
        keys_pressed.append(key_char)
    except AttributeError:
        if key == keyboard.Key.esc:
            escape()
        if key == keyboard.Key.space:
            search()

    if len(keys_pressed):
        print(json.dumps(keys_pressed))


listener = keyboard.Listener(on_press=on_press)

listener.start()

print(text2art("Tictacbot"))
print_new_section(init=True)

listener.join()
