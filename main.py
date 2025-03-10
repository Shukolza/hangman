import os
import webbrowser
import random
try:
    from secret import dev_code
    from getpass import getpass
except ModuleNotFoundError:
    dev_code = 'IMPORT_FAILED'

dev_mode = False

words = [
    'computer', 'person', 'cat', 'dog', 'house', 'car', 'book', 'tree', 'phone', 'table',
    'chair', 'city', 'country', 'river', 'mountain', 'ocean', 'sky', 'sun', 'moon', 'star',
    'flower', 'grass', 'bird', 'fish', 'lion', 'tiger', 'elephant', 'monkey', 'snake', 'rabbit',
    'horse', 'cow', 'sheep', 'pig', 'chicken', 'duck', 'goat', 'frog', 'bear', 'wolf', 'fox',
    'whale', 'shark', 'dolphin', 'penguin', 'kangaroo', 'zebra', 'giraffe', 'crocodile', 'turtle',
    'butterfly', 'bee', 'ant', 'spider', 'apple', 'banana', 'orange', 'grape', 'strawberry',
    'watermelon', 'potato', 'tomato', 'onion', 'carrot', 'bread', 'cheese', 'milk', 'coffee',
    'tea', 'juice', 'water', 'paper', 'pen', 'pencil', 'notebook', 'clock', 'watch', 'camera',
    'mirror', 'lamp', 'door', 'window', 'key', 'lock', 'shirt', 'pants', 'shoes', 'hat', 'socks',
    'jacket', 'umbrella', 'bag', 'wallet', 'money', 'bank', 'school', 'hospital', 'park', 'road',
    'bridge', 'train', 'bus', 'plane', 'ship', 'rocket', 'satellite', 'internet', 'website'
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_all_occurancies(a : list, element):
    '''returns list of indexes of all occurancies of element in list '''
    indices = [i for i, x in enumerate(a) if x == element]
    return indices

def at_least_one_match(list1 : list, list2 : list):
    for i in list1:
        if i in list2:
            return True
    return False

hangman_stadies_prints = [
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
""",
]
# 8 attempts
def main_menu():
    global dev_mode
    while True:
        clear()
        print("========== Hangman! ==========")
        print("""
             O 👋
            /|/
             |
            / \\
        """)
        print("[1] Start game")
        print("[2] Exit")
        print("[3] Contact developer")
        choice = input("Choose an option >>>")
        if choice == "1":
            game()
        elif choice == "2":
            print("Goodbye!")
            break
        elif choice == "3":
            clear()
            print('[1] Contact developer')
            print('[2] Enable developer mode')
            choice = input('Choose an option >>>')
            if choice == '1':
                webbrowser.open('t.me/shukolza', 2)
                print("Or via email: shukolza@gmail.com")
                input('Press Enter to continue...')
            elif choice == '2':
                if dev_code == 'IMPORT_FAILED':
                    print('Developer mode is not available.')
                    input('Press Enter to continue...')
                else:
                    code = getpass('>>>')
                    if code == dev_code:
                        dev_mode = True
                        print('Developer mode enabled.')
                        input('Press Enter to continue...')
                    else:
                        print('Incorrect code.')
                        input('Press Enter to continue...')
            else:
                print("Invalid choice. Please try again.")
                input('Press Enter to continue...')
                continue
        else:
            print("Invalid choice. Please try again.")
            input('Press Enter to continue...')

def game():
    global dev_mode
    current_correct_word = random.choice(words)
    current_correct_word_without_found = list(current_correct_word)
    spent_attempts_counter = 0
    current_attempts_amount = len(hangman_stadies_prints)
    current_word_mask='_ '*len(current_correct_word)
    excluded_letters = []
    while True:
        letters_to_be_excluded = []
        if spent_attempts_counter == current_attempts_amount - 1:
            # TODO game_over()
            print("G_O")
            pass
        clear()
        print("========== Game ==========")
        if dev_mode:
            print(current_correct_word)
        print()
        print(hangman_stadies_prints[spent_attempts_counter])
        print()
        print("Word:")
        print(current_word_mask)
        print()
        print(f'Excluded letters: \n{';'.join(excluded_letters)}')
        print()
        user_suggestion = input('Your suggestion? >>>').lower()

        if at_least_one_match(list(user_suggestion), excluded_letters):
            print('You already tried one of these letters!')
            input('Press Enter to continue...')
            continue
        
        flag = False
        for symbol in user_suggestion:
            if symbol in current_correct_word:
                #current_word_mask = current_word_mask[current_correct_word.index(symbol)] = symbol
                tmp = current_word_mask.split()
                #tmp[current_correct_word_without_found.index(symbol)] = symbol
                for occurance in find_all_occurancies(current_correct_word_without_found, symbol):
                    tmp[occurance] = symbol
                #current_correct_word_without_found[current_correct_word_without_found.index(symbol)] = ''
                for occurance in find_all_occurancies(current_correct_word_without_found, symbol):
                    current_correct_word_without_found[occurance] = ''                                                           
                current_word_mask = ' '.join(tmp)
                flag = True
            else:
                letters_to_be_excluded.append(symbol)

        excluded_letters.extend(list(set(letters_to_be_excluded)))

        #check if it's any unrevealed symbols
        if not '_' in current_word_mask.split():
            # TODO winner()
            print("WIN")
            pass
        elif not flag:
            spent_attempts_counter += 1




if __name__ == "__main__":
    main_menu()