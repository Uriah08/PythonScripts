from tkinter import *
from tkinter import Tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("TicTacToe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.x = 0
        self.o = 0
        self.current_player = "X"
        self.draw()

    def draw(self):
        self.window.configure(background="black")
        self.frame_header = Frame(self.window,bg="black")
        self.frame_header.grid(row=0)
        self.label_title = Label(self.frame_header,text="TicTacToe",fg="green",bg="black",font=("Arial",50))
        self.label_title.grid(row=0)
        self.label_player_turn = Label(self.frame_header,text="Player " + self.current_player + " turn.",
                                       font=("Arial",30),fg="green",bg="black")
        self.label_player_turn.grid(row=1)
        self.button_frame = Frame(window,bg="black")
        self.button_frame.grid(row=1)
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(self.button_frame,bg="gray",fg="black",font=("Arial,",20),width=5,height=2,
                                            activebackground="gray",activeforeground="black",command=lambda row = i, col = j:self.process(row,col))
                self.buttons[i][j].grid(row=i,column=j,padx=4,pady=4)
        self.score_frame = Frame(window,bg="black")
        self.score_frame.grid(row=2,stick="w")
        self.score_label = Label(self.score_frame, text="Score:",bg="black",fg="green",font=("Arial",40))
        self.score_label.grid(row=0)
        self.x_score = Label(self.score_frame,text="X: " + str(self.x) ,fg="green",bg="black",font=("Arial",30))
        self.x_score.grid(row=1,sticky="w")
        self.o_score = Label(self.score_frame, text="O: " + str(self.x), fg="green", bg="black", font=("Arial", 30))
        self.o_score.grid(row=2, sticky="w")
        self.reset_button = Button(window,text="Reset Score",font=("Arial",15),bg="gray",fg="black",
                                   activeforeground="black",activebackground="gray",command=self.reset_btn)
        self.reset_button.grid(row=3,pady=5)

    def process(self,row,col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.checker():
                if self.current_player == "X":
                    self.x += 1
                    self.x_score.config(text="X: " + str(self.x))
                elif self.current_player == "O":
                    self.o += 1
                    self.o_score.config(text="O: " + str(self.o))
                if messagebox.askyesno(message="Player " + self.current_player + " wins! Wanna play again?"):
                    self.reset()
                else:
                    quit()
            elif self.full():
                if messagebox.askyesno(message="The game is tie! Wanna play again?"):
                    self.reset()
                else:
                    quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label_player_turn.config(text="Player " + self.current_player + " turn.")
        else:
            messagebox.showinfo(message="The current cell is occupied")

    def checker(self):
        for index in range(3):
            if((self.board[index][0] == self.board[index][1] == self.board[index][2] != " ")
                    or (self.board[0][index] == self.board[1][index] == self.board[2][index] != " ")):
                return True
        if ((self.board[0][0] == self.board[1][1] == self.board[2][2] != " ")
                or (self.board[0][2] == self.board[1][1] == self.board[2][0] != " ")):
            return True

    def full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    return False
        return True
    def reset(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text=" ")
        self.current_player = "X"

    def reset_btn(self):
        self.x = 0
        self.o = 0
        self.x_score.config(text="X: " + str(self.x))
        self.o_score.config(text="O: " + str(self.o))



window = Tk()
game = TicTacToe(window)
window.mainloop()