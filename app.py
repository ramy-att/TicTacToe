import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames import Front,Play

#Crispy Text
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    print("warning: high DPI not possible")


class TicTacToe(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("TicTacToe Game")
        self.geometry("500x700")

        self.frames= {}
        container = ttk.Frame(self)
        container.grid(padx=0, pady=0, sticky="NSW")

        for FrameClass in (Front, Play):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(Front)
    def show_frame(self, container):
        '''Show a frame for the given page name'''
        frame = self.frames[container]
        frame.tkraise()

def main():
    app = TicTacToe()
    app.resizable(False, False)

    style= ttk.Style(app)
    font.nametofont("TkDefaultFont").configure(
        family= "Comic Sans MS",
        size=12
    )
    style.configure(
        "self.error_label.TLabel",
        foreground='red',
    )
    app.mainloop()

if __name__ == '__main__':
    main()
