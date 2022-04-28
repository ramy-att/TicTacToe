#imports
import tkinter as tk
from tkinter import Toplevel
from tkinter import ttk
from PIL import Image, ImageTk
import random
import time

class Front(ttk.Frame):
    def __init__(self,container,controller):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.cover_frame = ttk.Frame(self)
        self.cover_frame.grid(row=0, column=0, sticky="NSEW")

        #COVER PAGE

        cover_image = Image.open("./assets/T.png")
        cover_photo = ImageTk.PhotoImage(cover_image)

        cover_label = tk.Label(
            self.cover_frame ,
            image=cover_photo
        )

        cover_label.image = cover_photo
        cover_label.grid(
            row=0,
            column=0,
            padx=(0, 0),
            sticky="NSEW"
        )

        #Buttons
        b1 = tk.Button(
            self,
            bg="grey",
            fg="black",
            text="Play",
            command=lambda: controller.show_frame(Play)
        )
        b1.grid(
            row=1,
            column=0,
            pady=(20,0),
            padx=(0,0),
            sticky= "NSEW",

        )
        r = ttk.Label(
            self,
            text="Developed By Ramy Attalla"
        )
        r.grid(
            padx=(0, 0),
            pady=(50, 5),
            row=2,
            column=0,
        )
#Play Class
class Play(ttk.Frame):
    def __init__(self, container,controller):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #Set new strings and buttons
        self.player=tk.StringVar()
        self.player.set("Your move X !")

        self.turn= True #true-X, false-O (start with X)
        self.button0 = tk.StringVar()
        self.button0.set("-")
        self.button1=tk.StringVar()
        self.button1.set("-")
        self.button2 = tk.StringVar()
        self.button2.set("-")
        self.button3 = tk.StringVar()
        self.button3.set("-")
        self.button4 = tk.StringVar()
        self.button4.set("-")
        self.button5 = tk.StringVar()
        self.button5.set("-")
        self.button6 = tk.StringVar()
        self.button6.set("-")
        self.button7 = tk.StringVar()
        self.button7.set("-")
        self.button8 = tk.StringVar()
        self.button8.set("-")
        #Welcome label
        welcome = ttk.Label(
            self,
            textvariable=self.player
        )
        welcome.grid(
            row=5,
            column=2,
            pady=(60, 15),
            padx=(0,180),
            columnspan=4
        )
        #Buttons
        b = tk.Button(
            self,
            bg="red",
            fg="white",
            text="Reset",
            height=1,
            width=5,
            command=lambda: self.reset()
        )
        b.grid(
            padx=(0, 0),
            pady=(50,5),
            row=5,
            column=3,
        )

        pixelVirtual = tk.PhotoImage(width=1, height=1)
        #create buttons here using for loop

        # Create 9 buttons
        b0 = tk.Button(
            self,
            bg="black",
            fg="white",
            textvariable=self.button0,
            height=5,
            width=10,
            command=lambda: self.changeVal(b0,self.button0)
        )
        b0.grid(
            pady=(40,0),
            row=1,
            column=1,
        )
        b1 = tk.Button(
            self,
            bg="black",
            fg="white",
            textvariable=self.button1,
            height=5,
            width=10,
            command=lambda: self.changeVal(b1,self.button1)
        )
        b1.grid(
            row=1,
            column=2,
            pady=(40, 0),
        )
        b2 = tk.Button(
            self,
            bg="black",
            fg="white",
            textvariable=self.button2,
            height=5,
            width=10,
            command=lambda: self.changeVal(b2, self.button2)
        )
        b2.grid(
            row=1,
            column=3,
            pady=(40, 0),
            padx=(0, 60),

        )
        b3 = tk.Button(
            self,
            bg="black",
            fg="white",
            textvariable=self.button3,
            height=5,
            width=10,
            command=lambda: self.changeVal(b3, self.button3)
        )
        b3.grid(
            padx=(0, 0),
            row=2,
            column=1,
        )
        b4 = tk.Button(
            self,
            bg="black",
            fg="white",
            textvariable=self.button4,
            height=5,
            width=10,
            command=lambda: self.changeVal(b4, self.button4)
        )
        b4.grid(
            row=2,
            column=2,
        )
        b5 = tk.Button(
            self,
            bg="black",
            fg="white",
            textvariable=self.button5,
            height=5,
            width=10,
            command=lambda: self.changeVal(b5, self.button5)
        )
        b5.grid(
            row=2,
            column=3,
            padx=(0, 60),

        )
        b6 = tk.Button(
            self,
            bg="black",
            fg="white",
            textvariable=self.button6,
            height=5,
            width=10,
            command=lambda: self.changeVal(b6, self.button6)
        )
        b6.grid(
            padx=(0,0),
            row=3,
            column=1,
        )
        b7 = tk.Button(
            self,
            bg="black",
            fg="white",
            textvariable=self.button7,
            height=5,
            width=10,
            command=lambda: self.changeVal(b7, self.button7)
        )
        b7.grid(
            row=3,
            column=2,
        )
        b8 = tk.Button(
            self,
            bg="black",
            fg="white",
            textvariable=self.button8,
            height=5,
            width=10,
            command=lambda: self.changeVal(b8, self.button8)
        )
        b8.grid(
            row=3,
            column=3,
            padx=(0, 60),

        )
        self.buttons=[b0,b1,b2,b3,b4,b5,b6,b7,b8]
        #Board
        self.board=[[self.button0,self.button1,self.button2],[self.button3,self.button4,self.button5],[self.button6,self.button7,self.button8]]

    def getPlayer(self):
        '''Player's Turn'''
        if self.turn==True:
            self.player.set("Your move X !")
            print(self.player.get())
        else:
            self.player.set("Your move O !")

    def changeVal(self,button, text):
        '''Change the O and X'''
        if self.turn==True:
            print("True")
            text.set("X")
        else:
            print("False")
            text.set("O")
        button['state'] = 'disabled'
        self.turn=not self.turn
        self.getPlayer()
        self.checkWinner()


    def showWinner(self, lst):
        '''Game Over'''
        self.player.set("Game Over!")

        for button in self.buttons:
            button['state']='disabled'

        for element in lst:
            element.configure(bg="#d2d9cc", fg="black")

    def checkWinner(self):
        '''Check who won the game'''
        #Rows
        if self.board[0][0].get()==self.board[0][1].get() == self.board[0][2].get()!='-':
            self.player.set("Game over! "+ str(self.board[0][0].get())+" Wins")
            self.showWinner([self.buttons[0],self.buttons[1],self.buttons[2]])

        elif self.board[1][0].get()==self.board[1][1].get() == self.board[1][2].get()!='-':
            self.player.set("Game over! "+ str(self.board[1][0].get())+" Wins")
            self.showWinner([self.buttons[3],self.buttons[4],self.buttons[5]])

        elif self.board[2][0].get()==self.board[2][1].get() == self.board[2][2].get()!='-':
            self.player.set("Game over! "+ str(self.board[2][0].get())+" Wins")
            self.showWinner([self.buttons[6],self.buttons[7],self.buttons[8]])

        #Columns
        elif self.board[0][0].get()==self.board[1][0].get() == self.board[2][0].get()!='-':
            self.player.set("Game over! "+ str(self.board[0][0].get())+" Wins")
            self.showWinner([self.buttons[0],self.buttons[3],self.buttons[6]])

        elif self.board[0][1].get()==self.board[1][1].get() == self.board[2][1].get()!='-':
            self.player.set("Game over! "+ str(self.board[0][1].get())+" Wins")
            self.showWinner([self.buttons[1],self.buttons[4],self.buttons[7]])

        elif self.board[0][2].get()==self.board[1][2].get() == self.board[2][2].get()!='-':
            self.player.set("Game over! " + str(self.board[0][2].get()) + " Wins")
            self.showWinner([self.buttons[2],self.buttons[5],self.buttons[8]])

        #Diagonals
        elif self.board[0][0].get()==self.board[1][1].get() == self.board[2][2].get()!='-':
            self.player.set("Game over! "+ str(self.board[0][0].get())+" Wins")
            self.showWinner([self.buttons[0], self.buttons[4], self.buttons[8]])

        elif self.board[0][2].get()==self.board[1][1].get() == self.board[2][0].get()!='-':
            self.player.set("Game over! "+ str(self.board[0][2].get())+" Wins")
            self.showWinner([self.buttons[2],self.buttons[4],self.buttons[6]])

        else:
            print("Playing")

    def reset(self):
        '''Reset the game'''
        for button in self.buttons:
            button['state']='normal'
            button.configure(bg="black", fg="white")

        for list in self.board:
            for text in list:
                text.set("-")
        self.turn=True;
        self.player.set("Your move X !")
