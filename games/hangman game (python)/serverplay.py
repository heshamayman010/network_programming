import socket
from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 7070))
serversocket.listen(3)  # become a server socket, maximum 5 connections


class HangmanGUI:
    def __init__(self, master):
        self.master = master
        master.title("Hangman Game")

        # Create widgets
        self.message_label = tk.Label(
            master, text="Waiting for client to connect...")
        self.message_label.pack()

        self.quit_button = tk.Button(
            master, text="Quit", command=self.quit_game)
        self.quit_button.pack()

        # Start game
        self.start_game()

    def start_game(self):
        self.connection, address = serversocket.accept()
        self.message_label.config(text="Client connected.")
        buf = self.connection.recv(64)
        word = str(buf, "utf-8")
        self.play_game(word)

    # def play_game(self, secretWord):
    #     HANGMANPICS = ['''
    #     +-----+
    #     |     |
    #     |
    #     |
    #     |
    #     |
    #     ======= ''', '''
    #     +-----+
    #     |     |
    #     |     0
    #     |
    #     |
    #     |
    #     ======= ''', '''
    #     +-----+
    #     |     |
    #     |     0
    #     |     |
    #     |
    #     ======= ''', '''
    #     +-----+
    #     |     |
    #     |     0
    #     |    /|
    #     |
    #     |
    #     ======= ''', '''
    #     +-----+
    #     |     |
    #     |     0
    #     |    /|\\
    #     |
    #     |
    #     ======= ''', '''
    #     +-----+
    #     |     |
    #     |     0
    #     |    /|\\
    #     |    /
    #     |
    #     ======= ''', '''
    #     +-----+
    #     |     |
    #     |     0
    #     |    /|\\
    #     |    / \\
    #     |
    #     ======= ''']

    #     missedLetters = ''
    #     correctLetters = ''
    #     gameIsDone = False

    #     while not gameIsDone:
    #         self.display_board(HANGMANPICS, missedLetters,
    #                            correctLetters, secretWord)
    #         guess = self.get_guess(missedLetters + correctLetters)

    #         if guess in secretWord:
    #             correctLetters += guess
    #             foundAllLetters = True
    #             windows.mainloop()

    #             for i in range(len(secretWord)):
    #                 if secretWord[i] not in correctLetters:
    #                     foundAllLetters = False
    #                     break
    #             if foundAllLetters:
    #                 self.display_board(
    #                     HANGMANPICS, missedLetters, correctLetters, secretWord)
    #                 self.message_label.config(
    #                     text=f'Yes! The secret word is "{secretWord}"! You have won!')
    #                 self.connection.send(
    #                     bytes('You lostopponent won', 'UTF-8'))
    #                 gameIsDone = True
    #                 #windows.mainloop()

    #         else:
    #             missedLetters += guess
    #             if len(missedLetters) == len(HANGMANPICS) - 1:
    #                 self.display_board(
    #                     HANGMANPICS, missedLetters, correctLetters, secretWord)
    #                 self.message_label.config(
    #                     text=f'You have run out of guesses!\nAfter {len(missedLetters)} missed guesses and {len(correctLetters)} correct guesses, the word was "{secretWord}"')
    #                 self.connection.send(
    #                     bytes('You won opponent lost', 'UTF-8'))
    #                 gameIsDone = True
    #                 windows.mainloop()

    #                 # here is the modifications
    #         # label1 = Label(self.master, text="the gussed words")

    #         # label1.grid()
    #         # Widget1 = Widget(self, correctLetters)
    #         # Widget1.grid()
    #         # Widget2 = Widget(self, missedLetters)
    #         # Widget2.grid()

    #         windows = Tk()
    #         windows.title("your chances")
    #         windows.geometry("300x300")
    #         hangman_pic2 = tk.Label(
    #             windows, text=HANGMANPICS[len(missedLetters)], font=("Courier", 20))
    #         hangman_pic2.pack(pady=20)

    #         missed_letters_label = tk.Label(
    #             windows, text=f"Missed letters: {' '.join(missedLetters)}", font=("Courier", 14))
    #         missed_letters_label.pack()

    #         word_label1 = tk.Label(windows, text=' '.join(
    #             [letter if letter in correctLetters else '_' for letter in secretWord]), font=("Courier", 20))
    #         word_label1.pack(pady=20)
    #        # windows.mainloop()

    def play_game(self, secretWord):
        HANGMANPICS = [''' 
        +-----+
        |     |
        |
        |
        |
        |
        ======= ''', '''
        +-----+
        |     |
        |     0
        |
        | 
        |
        ======= ''', '''
        +-----+
        |     |
        |     0
        |     |
        |
        ======= ''', '''
        +-----+
        |     |
        |     0
        |    /|
        |     
        |
        ======= ''', '''
        +-----+
        |     |
        |     0
        |    /|\\
        |     
        |
        ======= ''', '''
        +-----+
        |     |
        |     0
        |    /|\\
        |    / 
        |
        ======= ''', '''
        +-----+
        |     |
        |     0
        |    /|\\
        |    / \\
        |
        ======= ''']

        missedLetters = ''
        correctLetters = ''
        gameIsDone = False

        # Create the widgets
        windows = tk.Tk()
        windows.title("Your chances")
        windows.geometry("300x300")

        hangman_pic2 = tk.Label(
            windows, text=HANGMANPICS[0], font=("Courier", 20))
        hangman_pic2.pack(pady=20)

        missed_letters_label = tk.Label(
            windows, text=f"Missed letters: {missedLetters}", font=("Courier", 14))
        missed_letters_label.pack()

        word_label1 = tk.Label(windows, text=' '.join(
            [letter if letter in correctLetters else '_' for letter in secretWord]), font=("Courier", 20))
        word_label1.pack(pady=20)

        while not gameIsDone:
            self.display_board(HANGMANPICS, missedLetters,
                               correctLetters, secretWord)
            guess = self.get_guess(missedLetters + correctLetters)

            if guess in secretWord:
                correctLetters += guess
                foundAllLetters = True

                for i in range(len(secretWord)):
                    if secretWord[i] not in correctLetters:
                        foundAllLetters = False
                        break
                if foundAllLetters:
                    self.display_board(
                        HANGMANPICS, missedLetters, correctLetters, secretWord)
                    self.message_label.config(
                        text=f'Yes! The secret word is "{secretWord}"! You have won!')
                    self.connection.send(
                        bytes('You lostopponent won', 'UTF-8'))
                    gameIsDone = True

            else:
                missedLetters += guess
                if len(missedLetters) == len(HANGMANPICS) - 1:
                    self.display_board(
                        HANGMANPICS, missedLetters, correctLetters, secretWord)
                    self.message_label.config(
                        text=f'You have run out of guesses!\nAfter {len(missedLetters)} missed guesses and {len(correctLetters)} correct guesses, the word was "{secretWord}"')
                    self.connection.send(
                        bytes('You won opponent lost', 'UTF-8'))
                    gameIsDone = True

            # Update the widgets after each guess
            hangman_pic2.config(text=HANGMANPICS[len(missedLetters)])
            missed_letters_label.config(
                text=f"Missed letters: {missedLetters}")
            word_label1.config(text=' '.join(
                [letter if letter in correctLetters else '_' for letter in secretWord]))

            windows.update()

        windows.mainloop()

    def display_board(self, HANGMANPICS, missedLetters, correctLetters, secretWord):
        self.master.geometry("500x500")  # set window size
        self.master.resizable(False, False)  # disable window resizing

        hangman_pic = tk.Label(
            self.master, text=HANGMANPICS[len(missedLetters)], font=("Courier", 20))
        hangman_pic.pack(pady=20)

        missed_letters_label = tk.Label(
            self.master, text=f"Missed letters: {' '.join(missedLetters)}", font=("Courier", 14))
        missed_letters_label.pack()

        word_label = tk.Label(self.master, text=' '.join(
            [letter if letter in correctLetters else '_' for letter in secretWord]), font=("Courier", 20))
        word_label.pack(pady=20)

    def get_guess(self, alreadyGuessed):
        while True:
            guess = simpledialog.askstring("Guess a letter", "Enter a letter:")
            guess = guess.lower()

            if guess is None:
                self.quit_game()
            elif len(guess) != 1:
                tk.messagebox.showerror(
                    "Error", "Please enter only one letter.")
            elif guess in alreadyGuessed:
                tk.messagebox.showerror(
                    "Error", "You have already guessed that letter. Choose again.")
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                tk.messagebox.showerror("Error", "Please enter a LETTER.")
            else:
                return guess

    def quit_game(self):
        self.master.destroy()
        serversocket.close()


root = tk.Tk()
hangman_gui = HangmanGUI(root)
root.mainloop()
