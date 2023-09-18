# Tic-Tac-Toe Python Game

## Overview

Welcome to the Tic-Tac-Toe Python game! In this project, I've explored Python classes and implemented a classic game that most of us have played on a piece of paper. 🚀🐍

This project also brings back fond memories of my time at Northcoders. I look back at the Object-Oriented Programming (OOP) sprint with great nostalgia and gratitude. Those experiences equipped me with valuable skills, and I'm glad to have learned from them, and translated them from JavaScript to Python.

## Python Classes and Game Logic

- **Python Classes:** This project showcases the use of Python classes to model the game of Tic-Tac-Toe. We've created three classes: `Player`, `RandomComputerPlayer`, `HumanPlayer`, and `SuperComputerPlayer`. These classes effectively manage player moves and the game's logic.

- **Game Logic:** The heart of the game resides in the `TicTacToe` class. It maintains the game's state, checks for a winner, and ensures valid moves. The board is represented as a list, and we track the current winner as the game progresses.

- **User Interface:** The game's user interface is simple yet functional. Players can make moves by entering numbers corresponding to the board positions. We also added some pauses between moves to simulate the turns and enhance the user experience.

- **SuperComputerPlayer:** Introducing the `SuperComputerPlayer` class that uses the minimax algorithm to play optimally. This player will always tie or win and never lose. This showcases advanced AI implementation in the game.

## Learning Python Insights

During this project, I've gained valuable insights into Python programming:

- **Object-Oriented Programming (OOP):** Building classes and using inheritance (e.g., `Player` and its subclasses) offers a structured and organized way to manage complex projects.

- **User Input Handling:** Implementing user input validation and error handling (in the `HumanPlayer` class) ensures a smooth user experience.

- **Game Logic:** Developing game logic and rules is a fundamental aspect of programming. In Tic-Tac-Toe, we check for winning conditions in rows, columns, and diagonals.

- **Artificial Intelligence:** The addition of the `SuperComputerPlayer` class demonstrates how AI can be implemented in games. It uses the minimax algorithm to make optimal moves.

## Usage

1. Run the `tic-tac-toe.py` file to start the game.
2. Players take turns making moves by entering numbers (0-8) corresponding to the board positions.
3. The game ends when a player wins or it's a tie.
4. Challenge yourself against the `SuperComputerPlayer` to test your skills or watch it play a perfect game.

## Future Implementations

- **Graphical User Interface:** Implement an interactive graphical interface using Python libraries like Tkinter or Pygame to enhance the game's visual appeal.

- **Difficulty Levels:** Implement multiple difficulty levels for the `SuperComputerPlayer` to provide varying challenges for players of different skill levels. Be able to select the size of the board and the type of computer player you're playing against.

- **Multiplayer Mode:** Add a multiplayer mode, allowing two human players to compete against each other on the same machine for a classic head-to-head match.

- **Statistics Tracking:** Include statistics tracking to record and display the number of wins, losses, and ties for each player.

- **Leaderboards:** Create leaderboards to showcase the top-performing players and their achievements.
