import tkinter as tk
from tkinter import Tk, ttk
from tkinter.messagebox import showerror
# from PIL import Image, ImageT

class ViewRootLogin():
    def __init__(self, root, var_email, var_senha):
        ''' Configurando janela'''
        root.geometry('320x300+470+150')
        root.title('BibleQuiz')
        root.iconbitmap('C:/Python/BibleQuiz/docs/bible.ico')
        root.resizable(0,0)
        root.config(bg='#F2C744')

        

        ''' Configurando grid'''
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=1)

        ''' Inserindo widgets. '''
        self.create_label_email(root)
        self.create_entry_email(root, var_email)
        self.create_label_password(root)
        self.create_entry_password(root, var_senha)
        self.create_button_login(root)
        self.create_button_register(root)
        self.create_checkbutton_ver_senha(root)
        # self.check_ver_senha()

    def create_label_email(self, root):
        self.label_email = ttk.Label(
            root,
            text='Email',
            background='#F2C744',
            foreground='black',
            font='Times 13 bold'
        )
        self.label_email.grid(row=0, column=0, padx=15, sticky=tk.W)
    
    def create_entry_email(self, root, var_email):
        # self.var_email = tk.StringVar()
        self.entry_email = ttk.Entry(
            root,
            textvariable= var_email,     
            width=400
        )
        self.entry_email.focus()
        self.entry_email.grid(row=0, column=0, padx=15, sticky=tk.SW, columnspan=32)

    def create_label_password(self, root):
        self.label_password = ttk.Label(
            root,
            text='Senha',
            background='#F2C744',
            foreground='black',
            font='Times 13 bold'
        )
        self.label_password.grid(row=1, column=0, padx=15, sticky=tk.W)

    def create_entry_password(self, root, var_senha):
        # self.var_password = tk.StringVar()
        self.entry_password = ttk.Entry(
            root,
            textvariable= var_senha,
            width=400,
            show= '*'
        )
        self.entry_password.grid(row=1, column=0, padx=15, sticky=tk.SW, columnspan= 32)

    def create_button_login(self, root):
        self.button_login = ttk.Button(
            root,
            text='Login'
        )
        self.button_login.grid(row=2, column=0, sticky=tk.W, padx=15)

    def create_button_register(self, root):
        self.button_register = ttk.Button(
            root,
            text='Register'
        )
        self.button_register.grid(row=2, column=3, sticky=tk.W, padx=15)

    def create_checkbutton_ver_senha(self, root):
        self.style = ttk.Style()
        self.style.configure('TCheckbutton', background='#F2C744')
        # self.image = Image.open('C:/Python/BibleQuiz/docs/icon_eyes.png')
        # self.photo = ImageTk.PhotoImage(self.image)

        self.check_versenha = ttk.Checkbutton(
            root,
            text='Ver senha senha'

            # variable= var_versenha
        )
        self.check_versenha.grid(row=2, column=0, sticky=tk.NW, padx=15)

