# Tictacbot

A program that makes you unbeatable at [BombParty](https://jklm.fun/) (in french).

![Demo](tictacbot-demo.gif)

## Disclaimer

I developed this program because I wanted to challenge myself with code and found it fun to try to create a bot that could follow the rules of the game perfectly.

It's not meant to be used to ruin other players' games: for my part, I used it to amaze and make my friends laugh during our private games.

Anyway, I doubt that many people find much interest in cheating on a simple board game without much at stake.

## Installation

⚠️ This program requires a version of [python](https://www.python.org/) >= 3 installed on your machine.

Install the [pytictacbot](https://pypi.org/project/pytictacbot/) module using *pip* (it is included with python):
```zsh
pip install pytictacbot
```

## Usage

In order for this program to work, you must grant access to *Accessibility* and *Input Monitoring* to the application that will run the script. Indeed, the program need access to listen to the keys you type.

On Mac:
- Open *System settings*,
- Navigate into the *Privacy & Security* section,
- Click on *Accessibility*,
- Allow the application(s) in which you will run the script (ex: Terminal, iTerm...),
- Go back, then do the same thing for *Input Monitoring*.

Once this is done, it is ready to use !

In your terminal, run:
```zsh
tictacbot
```

An interface will be displayed. It will listen to the keys you type. A history of these keys will be displayed on the interface.

- To launch the search, **press the space bar**.
- To quit, **press control+c**.

After a successful search, the found word will be automatically pasted. The *remaining letters* list will be updated accordingly.

## Rules

Before understanding how does it work, let's remember the rules of the [jklm.fun's BombParty](https://jklm.fun/) :
1. The player will be given a series of letters. He have to find (as quickly as possible) a word that contains this series of letters *(ex: "**iso**" -> "ma**iso**n")*
2. The player can't reuse a word that has already been used during the game.
3. The player starts with a list of all the letters in the alphabet, except "k", "w", "x", "y" and "z". If, with the words he/she types during the game, the player manages to use all these letters at least once, then the player will gain an extra life.

Finally, the goal in each round would be to find a word containing the sequence of letters, that has not been used already, but also the one that will unlock the most letters at once!

## How does it work ?

Once the script is launched, it will run in the background, listening to the keys that are typed on the keyboard.

It will display everything on the interface to make it easier for the user to understand what is happening in the background.

When the user will press escape to search the best word including the sequence of letters he/she typed, *Tictacbot* will crawl a file containing all the words of the French language.

It will first determine a list of all words containing the given sequence of letters.
Then, it will crawl this list and, for each word, calculate a score using the letters to discover (cf. 3rd rule). At the end, it will return the word with the highest possible score.

Finally, it will erase the sequence of letters that has ben typed by the user and paste the word instead.

## TODO's

- [ ] **Handling this case**: Currently, the program does not remain the words that has been used by the other players (only those that the player himself used). This can sometimes result in the reuse of an already used word (cf. 2nd rule).
- [ ] **Refining the source**: In rare cases, a word retrieved by *Tictacbot* may not be accepted in the game. In this case, manually remove the word from [the source file](tictacbot/gutenberg.txt).
- [x] **Manage all environments**: Adapt the keyboard shortcuts to the user's operating system.