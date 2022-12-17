# minesweeper

This is a Python program that implements the game Minesweeper. It allows the 
user to specify the size of the game board and the number of mines at the 
beginning of the game. The program uses the Pygame library to display the game 
board and handle user input.

The game board is represented as a two-dimensional list, with each element 
representing a cell on the board. Mines are represented by the value -1, and 
the other cells contain a number representing the number of mines in the 
surrounding cells. The game keeps track of which cells have been revealed and 
which cells have been flagged by the player using separate two-dimensional 
lists.

The main game loop handles user input and updates the game board display. If 
the user clicks on a cell with a mine, the game ends and a message is 
displayed. If the user right-clicks on a cell, it is flagged. If the user left-
clicks on a cell, it is revealed. The game also checks for a win condition, 
which occurs when all cells that do not contain mines have been revealed. If 
the player wins, a message is displayed.
