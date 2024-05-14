import tkinter as tk
from tkinter import Tk, ttk
import os


class RootEndRound(Tk):
    def __init__(self, score):
        super().__init__()

        #.: Configurando janela
        self.geometry('400x200+450+200')
        self.iconbitmap('C:/Python/BibleQuiz/docs/bible.ico')
        self.title('BibleQuiz')
        self.resizable(0,0)
        self.config(bg='#1089DD')

        #.: Configurando grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)


        #.: Inserindo widgets
        self.create_message_label(score)
        self.create_buttons()

        self.mainloop()

    def create_message_label(self, score):
        self.message_label = ttk.Label(
            self,
            text=f'Parabéns, você chegou ao fim desta rodada \n\nO seu score final é: {score}/10',
            background='#1089DD',
            foreground='Black',
            font='Times 12 bold'
        )
        self.message_label.grid(row=0, column=1, columnspan=2, sticky=tk.W)

    def create_buttons(self):
        self.btn_again = ttk.Button(
            self,
            text='PLAY AGAIN',
            command= self.command_button_again
        )
        self.btn_again.grid(row=1, column=1, sticky=tk.S)

        self.btn_exit= ttk.Button(
            self,
            text='EXIT',
            command= self.destroy
        )
        self.btn_exit.grid(row=1, column=2, sticky=tk.SW)

    def command_button_again(self):
        from biblequiz.rootgame.constructor_root_game import RootGame
        self.destroy()
        os.system('cls')
        RootGame()



# if __name__ == "__main__":
#     teste = RootEndRound()
#     teste.mainloop()