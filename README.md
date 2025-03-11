# Hangman Game

A classic Hangman game implemented in Python with colorful text, sound effects, and developer mode for debugging. Challenge yourself by guessing words letter-by-letter or attempt to guess the entire word at once!

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Colorful Interface**: Rainbow-themed menus and colored text for better visuals.
- **Sound Effects**: Enjoy sound effects for correct guesses, errors, wins, and game overs.
- **Developer Mode**: Debugging tools like showing the correct word during gameplay.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Customizable Word List**: Add or remove words from the `words` list in the code.

## Installation

### Prerequisites

- Python 3.x
- `pygame` library (for sound effects) (not necessary)
- `colorama` library (for colored text)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   cd hangman-game
   ```

2. Install dependencies:
   ```bash
   pip install pygame colorama
   ```

4. Run the game:
   ```bash
   python hangman.py
   ```

## Usage

1. Launch the game using the command:
   ```bash
   python hangman.py
   ```

2. Choose an option from the main menu:
   - `[1] Start game`: Begin a new game.
   - `[2] Exit`: Quit the program.
   - `[3] Contact developer`: Get support.

3. Follow the on-screen instructions to guess letters or the full word.

## Game Rules

- Guess the hidden word by suggesting letters or the entire word.
- Each incorrect guess reduces your remaining attempts.
- You have a maximum of 8 attempts before the game ends.
- Multi-letter guesses are allowed but count as one attempt if invalid.
- Duplicate letters in the word are revealed all at once when guessed correctly.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

For major changes, please open an issue first to discuss your ideas.

## License

This project is not licensed. I don't think someone will steal this peace of ~~shit~~ code XD
