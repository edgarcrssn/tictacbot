from pynput import keyboard
import pyperclip
import pyautogui
from art import *
from colorama import init, Fore, Style
from tictacbot import tictacbot

init()

keys_pressed = []

def retrieve_word() -> str | None:
    letters = "".join(keys_pressed)
    return tictacbot(letters)

def paste_word(word: str):
    pyperclip.copy(word)
    pyautogui.press('backspace', presses=len(keys_pressed) + 1)
    pyautogui.hotkey("command", "v")

def on_press(key):
    try:
        key_char = key.char
        if not key_char.isalpha():
            return
        keys_pressed.append(key_char)
    except AttributeError:
        if key == keyboard.Key.esc:
            keys_pressed.clear()
            print(keys_pressed)
            print('_' * 15)
            print('Keys pressed:')
        if key == keyboard.Key.space:
            print('Searching...')
            word_found = retrieve_word()
            if(word_found and len(word_found)):
                word_found_colored = Fore.GREEN + word_found + Style.RESET_ALL
                print('Found: ' + word_found_colored)
                paste_word(word_found)
            else:
                print(Fore.RED + 'Not found' + Style.RESET_ALL)
            keys_pressed.clear()
            print('_' * 15)
            print('Keys pressed:')

    if len(keys_pressed):
        print(keys_pressed)


listener = keyboard.Listener(on_press=on_press)

listener.start()

tprint('Tictacbot')
print('Keys pressed:')

listener.join()
