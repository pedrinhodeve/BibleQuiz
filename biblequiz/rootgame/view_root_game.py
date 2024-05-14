from tkinter import Tk, ttk

class WidgetsGame():
    def __init__(self, root):
        # super().__init__()
        root.geometry('620x500+300+100')
        root.title('BibleQuiz')
        root.iconbitmap('C:/Python/BibleQuiz/docs/bible.ico')
        root.resizable(0,0)
        root.config(bg='#F2C744')
        
        self.create_label_pergunta(root)
        self.creatbtne_buttons_options(root)
        
    def create_label_pergunta(self, root):
        self.lbl_pergunta = ttk.Label(
            root, 
            background='#F2C744', 
            foreground='#FD4F5A',
            font='Arial 14 bold',
            wraplength=500
        )
        self.lbl_pergunta.pack(pady=80)

    def creatbtne_buttons_options(self, root):
        self.style = ttk.Style()
        self.style.configure('TButton',
                             font='Arial 12 bold',
                             background='#1089DD',
                             foreground='#1089DD',
                             width=30
        )

        
        self.btn_option1 = ttk.Button(
            root,
            text='Option 1'
        )
        self.btn_option1.pack(pady=10)

        self.btn_option2 = ttk.Button(
            root,
            text='Option 2'
        )
        self.btn_option2.pack(pady=10)

        self.btn_option3 = ttk.Button(
            root,
            text='Option 3'
        )
        self.btn_option3.pack(pady=10)

        self.btn_option4 = ttk.Button(
            root,
            text='Option 4'
        )
        self.btn_option4.pack(pady=10)