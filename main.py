#!/usr/bin/python3
import os
import sys
import webbrowser
import random
import colorama
from colorama import Fore

def resource_path(relative_path):
    """Get a correct file path for compiled EXE"""
    try:
        # Temp folder for PyInstaller
        base_path = sys._MEIPASS
    except AttributeError:
        # Standard mode (launched via Python)
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

try:
    import pygame
    pygame.mixer.init()
    error_sound = pygame.mixer.Sound(resource_path("sounds/error.mp3"))
    choose_sound = pygame.mixer.Sound(resource_path("sounds/choose.mp3"))
    game_over_sound = pygame.mixer.Sound(resource_path('sounds/game_over.mp3'))
    win_sound = pygame.mixer.Sound(resource_path('sounds/win.wav'))
    sound_enabled = True
except Exception as e:
    print(e)
    sound_enabled = False

try:
    from secret import dev_code
    from getpass import getpass
except ModuleNotFoundError:
    dev_code = "IMPORT_FAILED"

dev_mode = False
colorama.init()

WORDS = [
    "computer", "person", "cat", "dog", "house", "car", "book", "tree",
    "phone", "table", "chair", "city", "country", "river", "mountain",
    "ocean", "sky", "sun", "moon", "star", "flower", "grass", "bird",
    "fish", "lion", "tiger", "elephant", "monkey", "snake", "rabbit",
    "horse", "cow", "sheep", "pig", "chicken", "duck", "goat", "frog",
    "bear", "wolf", "fox", "whale", "shark", "dolphin", "penguin",
    "kangaroo", "zebra", "giraffe", "crocodile", "turtle", "butterfly",
    "bee", "ant", "spider", "apple", "banana", "orange", "grape",
    "strawberry", "watermelon", "potato", "tomato", "onion", "carrot",
    "bread", "cheese", "milk", "coffee", "tea", "juice", "water",
    "paper", "pen", "pencil", "notebook", "clock", "watch", "camera",
    "mirror", "lamp", "door", "window", "key", "lock", "shirt",
    "pants", "shoes", "hat", "socks", "jacket", "umbrella", "bag",
    "wallet", "money", "bank", "school", "hospital", "park", "road",
    "bridge", "train", "bus", "plane", "ship", "rocket", "satellite",
    "internet", "website"
]

HANGMAN_STAGES = [
    """
      |
      |
      |
      |
      |
      | 
      |    
    __|__""",
    """
      Г‾‾‾‾‾
      |
      |
      | 
      |
      |
      |    |_|
      |  __|_|__  
    __|___/___\\___""",
    """
      Г‾‾‾‾‾|
      |     |
      |     
      | 
      |
      |
      |    |_|
      |  __|_|__  
    __|___/___\\___""",
    """
      Г‾‾‾‾‾|
      |     |
      |     O
      | 
      |
      |
      |    |_|
      |  __|_|__  
    __|___/___\\___""",
    """
      Г‾‾‾‾‾|
      |     |
      |     O
      |    /|\\
      | 
      |
      |    |_|
      |  __|_|__  
    __|___/___\\___""",
    """
      Г‾‾‾‾‾|
      |     |
      |     O
      |    /|\\
      |     |
      |    / \\
      |    |_|
      |  __|_|__  
    __|___/___\\___""",
    """
      Г‾‾‾‾‾|
      |     |
      |     O Zzzz.....
      |    /|\\
      |     |
      |    / \\
      |
      |    ___  
    __|___/___\\___""",
    """
    (⏜⏜⏜⏜⏜⏜⏜⏜⏜)
    |   RIP   |
    | Hangman |
    |         |
    |         |
    |_________|
"""
]

def rainbow_text(text):
    colors = [
        Fore.RED, Fore.YELLOW, Fore.GREEN,
        Fore.CYAN, Fore.BLUE, Fore.MAGENTA
    ]
    return ''.join(colors[i % len(colors)] + char 
                  for i, char in enumerate(text)) + Fore.RESET

def color(text, color_name):
    color_map = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        'black': Fore.BLACK
    }
    return color_map.get(color_name.lower(), Fore.WHITE) + text + Fore.RESET

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print(rainbow_text("========== Hangman! =========="))
        print("""
             O 👋
            /|/
             |
            / \\
        """)
        if dev_mode:
            print(rainbow_text("Dev Mode: ON"))
            print(f"Sound: {'✓' if sound_enabled else '✗'}")
        print("[1] Start game")
        print("[2] Exit")
        print("[3] Contact developer")
        
        choice = input("Choose an option >>> ").strip()
        
        if choice == '1':
            if sound_enabled:
                choose_sound.play()
            play_game()
        elif choice == '2':
            if sound_enabled:
                choose_sound.play()
            print("Goodbye!")
            break
        elif choice == '3':
            if sound_enabled:
                choose_sound.play()
            handle_developer_options()
        else:
            if sound_enabled:
                error_sound.play()
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

def handle_developer_options():
    clear_screen()
    print("[1] Contact developer")
    print("[2] Enable developer mode")
    choice = input("Choose an option >>> ").strip()
    
    if choice == '1':
        webbrowser.open("https://t.me/shukolza", new=2)
        print("Or via email: shukolza@gmail.com")
        input("Press Enter to continue...")
    elif choice == '2':
        handle_dev_mode_activation()
    else:
        if sound_enabled:
            error_sound.play()
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")

def handle_dev_mode_activation():
    global dev_mode
    if dev_code == "IMPORT_FAILED":
        print("Developer mode unavailable")
        input("Press Enter to continue...")
        return
        
    code = getpass("Enter developer code: ")
    if code == dev_code:
        dev_mode = True
        print("Developer mode enabled!")
        if sound_enabled:
            choose_sound.play()
    else:
        print("Incorrect code!")
        if sound_enabled:
            error_sound.play()
    input("Press Enter to continue...")

def play_game():
    word = random.choice(WORDS)
    guessed_letters = set()
    excluded_letters = []
    attempts = 0
    max_attempts = len(HANGMAN_STAGES) - 1
    
    while True:
        clear_screen()
        print(rainbow_text("========== Game =========="))
        if dev_mode:
            print(f"Debug: {word}")
        
        print(color(f"Remaining attempts: {max_attempts - attempts}", "cyan"))
        print(HANGMAN_STAGES[attempts])
        print("\nWord: " + create_word_mask(word, guessed_letters))
        print(f"\nExcluded letters: {', '.join(excluded_letters)}")
        
        guess = input("\nYour guess (letter or full word): ").lower().strip()
        
        if not guess.isalpha():
            handle_invalid_input()
            continue
        
        if len(guess) == len(word):
            handle_full_word_guess(guess, word, guessed_letters)
            break
        
        handle_letter_guess(guess, word, guessed_letters, excluded_letters)
        
        if is_word_guessed(word, guessed_letters):
            show_winner(word)
            break
            
        if not any(c in word for c in guess if c not in excluded_letters):
            attempts += 1
            if attempts >= max_attempts:
                show_game_over(word)
                break

def create_word_mask(word, guessed_letters):
    return ' '.join([c if c in guessed_letters else '_' for c in word])

def handle_invalid_input():
    print("Please enter only letters (a-z)!")
    if sound_enabled:
        error_sound.play()
    input("Press Enter to continue...")

def handle_full_word_guess(guess, word, guessed_letters):
    if guess == word:
        guessed_letters.update(word)
        show_winner(word)
    else:
        print("Incorrect word guess!")
        if sound_enabled:
            error_sound.play()
        input("Press Enter to continue...")

def handle_letter_guess(guess, word, guessed_letters, excluded_letters):
    for symbol in guess:
        if symbol in excluded_letters or symbol in guessed_letters:
            print(f"'{symbol}' was already guessed!")
            continue
            
        if symbol in word:
            guessed_letters.add(symbol)
            if sound_enabled:
                choose_sound.play()
        else:
            excluded_letters.append(symbol)
            if sound_enabled:
                error_sound.play()

def is_word_guessed(word, guessed_letters):
    return all(c in guessed_letters for c in word)

def show_winner(word):
    clear_screen()
    print(color("========== YOU WON! ==========", "green"))
    print("""
         O 🏆
        /|/
         |
        / \\
    """)
    print(f"The word was: {word}")
    if sound_enabled:
        win_sound.play()
    input("\nPress Enter to return to menu...")

def show_game_over(word):
    clear_screen()
    print(color("========== GAME OVER ==========", "red"))
    print(HANGMAN_STAGES[-1])
    print(f"\nThe word was: {word}")
    if sound_enabled:
        game_over_sound.play()
    input("\nPress Enter to return to menu...")
    if sound_enabled:
        game_over_sound.stop()

if __name__ == "__main__":
    main_menu()