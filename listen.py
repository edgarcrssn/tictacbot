from pynput import keyboard
import pyperclip
import pyautogui
from art import *
from colorama import init, Fore, Style
from tictacbot import tictacbot

init()

keys_pressed = []
remaining_letters = list("abcdefghijklmnopqrstuvwxyz")


def update_remaining_letters(word_found: str):
    global remaining_letters
    remaining_letters = [
        letter for letter in remaining_letters if letter not in word_found
    ]
    if len(remaining_letters) == 0:
        remaining_letters = list("abcdefghijklmnopqrstuvwxyz")


def paste_word(word: str):
    pyperclip.copy(word)
    pyautogui.press("backspace", presses=len(keys_pressed) + 1)
    pyautogui.hotkey("command", "v")


def escape():
    keys_pressed.clear()
    print(keys_pressed)
    print("_" * 15)
    print("Keys pressed:")


def search():
    global remaining_letters
    word_found = tictacbot("".join(keys_pressed), remaining_letters)

    if word_found and len(word_found):
        update_remaining_letters(word_found)
        word_found_colored = Fore.GREEN + word_found + Style.RESET_ALL
        print("Found: " + word_found_colored)
        paste_word(word_found)
    else:
        print(Fore.RED + "Not found" + Style.RESET_ALL)
    print("_" * 15)
    print(remaining_letters)
    print("Keys pressed:")
    keys_pressed.clear()


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
            print("Searching...")
            search()

    if len(keys_pressed):
        print(keys_pressed)


listener = keyboard.Listener(on_press=on_press)

listener.start()

tprint("Tictacbot")
print("Keys pressed:")

listener.join()
