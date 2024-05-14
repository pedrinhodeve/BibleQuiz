import tkinter as tk
from tkinter import Tk, ttk
from tkinter.messagebox import showerror, showinfo
from biblequiz.rootlogin.view_root_login import ViewRootLogin
from biblequiz.rootlogin.model_root_login import BancoDeDadosLogin
from biblequiz.rootgame.constructor_root_game import RootGame
import os
import re

class ConstructorRootLogin(Tk):
    def __init__(self):
        super().__init__()

        """ Definindo váriaveis uteis para interação entre View e Constructor"""
        self.var_email = tk.StringVar()
        self.var_senha = tk.StringVar()        

        self.root_login = ViewRootLogin(self, self.var_email, self.var_senha)
        self.bdd_login = BancoDeDadosLogin()

        self.root_login.button_login.config(command= self.command_login)
        self.root_login.button_register.config(command=self.command_register)
        self.root_login.check_versenha.config(command=self.check_versenha)

        self.mainloop()

    def command_login(self):
        # self.re_email = re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", self.var_email.get())
        if self.var_email.get() =='':
            showerror(title='Campo obrigatório', message='O campo email é obrigatório.')
        # elif self.re_email is None:
        #     showerror(message='Email inválido.')
        elif self.var_senha.get() == '':
            showerror(title='Campo obrigatório', message='O campo senha é obrigatório.')
        # elif len(self.var_senha.get()) < 8:
        #     showerror(message='A senha deve ter no mínimo 8 caracteres.')
        else:
            if self.bdd_login.login(self.var_email.get(), self.var_senha.get()) == 'Entrando.':
                os.system('cls')
                self.destroy()
                RootGame()
            # elif  self.bdd_login.login(self.var_email.get(), self.var_senha.get()) == 'Senha incorreta.':
            #     showerror(message='Senha incorreta.')
            # else:
            #     showerror(message='Usuário não encontrado.\nVerique o email ou registre-se.')

    def command_register(self):
        self.re_email = re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", self.var_email.get())
        if self.re_email =='':
            showerror(title='Campo obrigatório', message='O campo email é obrigatório.')
        elif self.re_email is None:
            showerror(message='Email inválido.')
        elif self.var_senha.get() == '':
            showerror(title='Campo obrigatório', message='O campo senha é obrigatório.')
        elif len(self.var_senha.get()) < 8:
            showerror(message='A senha deve ter no mínimo 8 caracteres.')
        else:
            if self.bdd_login.register(self.var_email.get(), self.var_senha.get()) == 'Registrado.':
                os.system('cls')
                showinfo(message='Usuário registrado com sucesso.\nPreparado para jogar? Vamos nessa!!!')
                self.destroy()
                RootGame()
            elif self.bdd_login.register(self.var_email.get(), self.var_senha.get()) == 'Email já registrado.':
                os.system('cls')
                showerror(message='Este email já está registrado. Faça o login ou insira outro email.')
            
    def check_versenha(self):
        if self.root_login.entry_password['show'] == '':
            self.root_login.entry_password.config(show='*')
        else:
            self.root_login.entry_password.config(show='')
            


# if __name__ == '__main__':
#     teste = ConstructorRootLogin()
#     # teste.mainloop()