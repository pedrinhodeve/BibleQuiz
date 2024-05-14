import tkinter as tk
from tkinter import Tk, ttk
from biblequiz.rootgame.view_root_game import WidgetsGame
from biblequiz.rootgame.model_bancodedados_questions import BancoDeDadosQuestions
from biblequiz.rootend.root_end_round import RootEndRound

class RootGame(Tk):
    def __init__(self):
        super().__init__()
 
        '''Definindo várias úteis para o funcionamente de funções.'''
        self.indice_question = 0
        self.score = 0
        self.clicked_text_button = tk.StringVar()

        self.root = WidgetsGame(self)
        self.teste = BancoDeDadosQuestions().take_10__questions()
        
        self.update_text_widgets()
        self.update_command_buttons()

        self.mainloop()

    def update_text_widgets(self):
        try:
            self.current = self.teste[self.indice_question]

            #.: Update text label pergunta.
            self.root.lbl_pergunta.config(text=self.current[0])

            #.: Update text buttons options
            self.root.btn_option1.config(text=self.current[1])
            self.root.btn_option2.config(text=self.current[2])
            self.root.btn_option3.config(text=self.current[3])
            self.root.btn_option4.config(text=self.current[4])
            
            self.resposta = self.current[5]
        except:
            print('Acabou as perguntas.')
            print(f'Socre: {self.score}/10')
            self.destroy()
            RootEndRound(self.score)
            

    def update_command_buttons(self):
    
            self.root.btn_option1.config(command= lambda: self.command_buttons(self.root.btn_option1['text']))
            self.root.btn_option2.config(command=lambda: self.command_buttons(self.root.btn_option2['text']))
            self.root.btn_option3.config(command=lambda: self.command_buttons(self.root.btn_option3['text']))
            self.root.btn_option4.config(command=lambda: self.command_buttons(self.root.btn_option4['text']))

    def command_buttons(self, button_text):
        self.indice_question+=1
        print(f'Questão {self.indice_question}')
        self.system_points(button_text)
        self.update_text_widgets()
  
    def take_buttontext_clicked(self, button_text):
        self.clicked_text_button.set(button_text)
        self.escolhido = self.clicked_text_button.get()
        return self.escolhido

    def system_points(self, button_text):
        self.resposta_escolhida = self.take_buttontext_clicked(button_text)
        if self.resposta == self.resposta_escolhida:
            self.score+=1
            print('Resposta correta.')
        else:
            print('Resposta errada.')
        
        print(f'Resposta: {self.resposta}')
        print(f'Alternativa escolhida: {self.resposta_escolhida}')
        print('')


# if __name__ == "__main__":
#     app = RootGame()
#     app.mainloop()