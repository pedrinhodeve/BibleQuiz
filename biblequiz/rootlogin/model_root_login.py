import sqlite3


class BancoDeDadosLogin():
    def __init__(self):
        self.conect()
        self.create_table_login()
        print('Banco de dados de usuários conectado com sucesso.')

    def conect(self):
        self.conectar = sqlite3.connect('base_users.db')

        self.cursor = self.conectar.cursor()

    def create_table_login(self):
        try:
            self.sql_table_login = '''
            CREATE TABLE IF NOT EXISTS login(
                email VARCHAR(250),
                senha VARCHAR(250),
                PRIMARY KEY(email)
            )
            '''
            self.cursor.execute(self.sql_table_login)
            # print('Tabela criada com sucesso.')
        except sqlite3.Error as error:
            print(error)

    def register(self, email, password):
        
        try:
            self.sql_verificação =  '''
            SELECT 1 FROM login WHERE email = ?
            ''' 
            self.cursor.execute(self.sql_verificação, (email,))
            result = self.cursor.fetchone()

            if result is not None:
                self.return_ = 'Email já registrado.'
                print(self.return_)
                return self.return_
            else:
                self.sql_register = '''
                INSERT INTO login(email, senha) VALUES (?, ?)
                '''

                self.values = (email, password)

                self.cursor.execute(self.sql_register, self.values)
                self.conectar.commit()
                self.return_ = "Registrado."
                return self.return_

        except sqlite3.Error as error:
            print(error)
            # print('Email já registrado')

    def login(self, email, password):
        import tkinter as tk
        from tkinter.messagebox import showerror, showinfo
        try:
            self.sql_verificação =  '''
            SELECT 1 FROM login WHERE email = ?
            ''' 
            self.cursor.execute(self.sql_verificação, (email,))
            result = self.cursor.fetchone()

            if result is not None:
                self.sql_login_ =  '''
                SELECT * FROM login WHERE email = ? AND senha = ?
                ''' 
                self.cursor.execute(self.sql_login_, (email, password))
                result = self.cursor.fetchone()

                if result is not None:
                    self.return_ = 'Entrando.'
                    print(self.return_)
                    return self.return_
        
                else:
                    self.return_ = "Senha incorreta."
                    print(self.return_)
                    showerror(message=self.return_)
            else:
                self.return_ = 'Usuário não encontrado.'
                print(self.return_)
                showerror(message=self.return_)

        except sqlite3.Error as error:
            print(error)




# teste = BancoDeDadosLogin()
# # teste.verificação(input())
# # teste.register(input(), input())
# teste.login(input(), input())