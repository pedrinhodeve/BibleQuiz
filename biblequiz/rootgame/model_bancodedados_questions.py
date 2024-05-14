import sqlite3

class BancoDeDadosQuestions():
    try:
        def __init__(self):
            self.connect()
            self.create_table_questions()
            self.insert_questions()
            self.take_10__questions()

            print('Banco de dados das questões conectado com sucesso.')

    except sqlite3.Error as error:
        print(error)

    def connect(self):
        self.conectar = sqlite3.connect('base.db')
        # print('Banco de dados conectado com sucesso.')

        self.cursor = self.conectar.cursor()
        
    def create_table_questions(self):
        try: 
            self.sql_table = """
            CREATE TABLE IF NOT EXISTS questions(
                pergunta VARCHAR(250),
                alternativa_1 VARCHAR (250),
                alternativa_2 VARCHAR (250),
                alternativa_3 VARCHAR (250),
                alternativa_4 VARCHAR (250),
                resposta VARCHAR (250),
                PRIMARY KEY(pergunta)
            )
            """
            self.cursor.execute(self.sql_table)
            # print('Tabela criada com sucesso.')
                 

        except sqlite3.Error as error:
            print("Erro na função 'create_table_questions'", error)

    def insert_questions(self):
        try:
            self.values = [
                ('Quem foi o primeiro homem criado segundo o Antigo Testamento?', 'Adão', 'Abraão', 'Noé', 'Jacó', 'Adão'),
                ('Qual o nome do profeta que construiu uma arca para salvar sua família e os animais do dilúvio?', 'Jonas', 'Isaías', 'Noé', 'Moisés', 'Noé'),
                ('Qual o nome do irmão de Moisés?', 'Arão', 'Samuel', 'Davi', 'Elias', 'Arão'),
                ('Qual foi a primeira praga enviada por Deus ao Egito durante o Êxodo?', 'Chuva de fogo', 'Praga dos gafanhotos', 'Água em sangue', 'Trevas', 'Água em sangue'),
                ('Qual o nome do rei que construiu o templo em Jerusalém?', 'Davi', 'Salomão', 'Ezequias', 'Josafá', 'Salomão'),
                ('Qual foi a esposa de Abraão que deu à luz a Isaque?', 'Sara', 'Raquel', 'Rebeca', 'Lia', 'Sara'),
                ('Qual foi o filho de Davi que se tornou rei após ele?', 'Salomão', 'Absalão', 'Davi II', 'Jeroboão', 'Salomão'),
                ('Quem foi o profeta que desafiou os profetas de Baal no monte Carmelo?', 'Eliseu', 'Elias', 'Samuel', 'Isaías', 'Elias'),
                ('Qual era o nome da esposa de Jacó que teve doze filhos, que mais tarde se tornaram as doze tribos de Israel?', 'Rebeca', 'Raquel', 'Lia', 'Zilpa', 'Lia'),
                ('Quem foi o profeta que foi engolido por um grande peixe e permaneceu em seu ventre por três dias e três noites?', 'Elias', 'Jonas', 'Jeremias', 'Zacarias', 'Jonas'),
                ('Qual foi o profeta que clamou "Eis-me aqui, envia-me a mim" quando Deus perguntou quem Ele enviaria para seu povo?', 'Isaías', 'Jeremias', 'Ezequiel', 'Oséias', 'Isaías'),
                ('Qual foi o profeta que sobreviveu à prova do fogo na cova dos leões?', 'Jonas', 'Daniel', 'Oseias', 'Miqueias', 'Daniel'),
                ('Quem foi o rei que escreveu muitos dos Salmos encontrados no Antigo Testamento?', 'Davi', 'Salomão', 'Ezequias', 'Josafá', 'Davi'),
                ('Qual foi o patriarca que teve um sonho onde uma escada chegava até o céu?', 'Abraão', 'Jacó', 'Moisés', 'Isaque', 'Jacó'),
                ('Quem foi o sumo sacerdote que ajudou a reconstruir os muros de Jerusalém após o exílio babilônico?', 'Josué', 'Esdras', 'Elias', 'Jó', 'Esdras'),
                ('Qual dos profetas do Antigo Testamento foi chamado "chorão" por seu lamento sobre Jerusalém?', 'Jeremias', 'Isaías', 'Ezequiel', 'Oséias', 'Jeremias'),
                ('Qual foi o nome do juiz que liderou Israel na guerra contra os midianitas?', 'Gideão', 'Sansão', 'Jefté', 'Eli', 'Gideão'),
                ('Quem foi o profeta que clamou "Como pode viver o homem puro?"', 'Isaías', 'Jeremias', 'Oséias', 'Ezequiel', 'Ezequiel'),
                ('Qual foi o irmão mais velho de Moisés?', 'Arão', 'Miriã', 'Josué', 'Calebe', 'Arão'),
                ('Quem foi o profeta que predisse a vinda de João Batista como precursor do Messias?', 'Isaías', 'Jeremias', 'Malaquias', 'Ezequiel', 'Malaquias'),
                ('Qual foi o nome do rei que teve seu reino dividido em Israel e Judá após sua morte?', 'Salomão', 'Davi', 'Roboão', 'Ezequias', 'Roboão'),
                ('Quem foi o profeta que clamou "O Senhor é a minha luz e a minha salvação, de quem terei medo?"', 'Davi', 'Jonas', 'Samuel', 'Moisés', 'Davi'),
                ('Qual foi o nome do profeta que enfrentou os profetas de Baal no Monte Carmelo?', 'Elias', 'Eliseu', 'Isaías', 'Jeremias', 'Elias'),
                ('Qual dos patriarcas do Antigo Testamento teve seu nome mudado para Israel?', 'Jacó', 'Abraão', 'Isaque', 'José', 'Jacó'),
                ('Quem foi o profeta que teve uma visão de um vale cheio de ossos secos que se tornaram um exército vivo?', 'Ezequiel', 'Isaías', 'Jeremias', 'Daniel', 'Ezequiel'),
                ('Qual era o nome da cidade onde nasceu Jesus Cristo?', 'Nazaré', 'Belém', 'Jerusalém', 'Caná', 'Belém'),
                ('Qual dos discípulos de Jesus o traiu?', 'João', 'Tiago', 'Pedro', 'Judas', 'Judas'),
                ('Qual foi o primeiro milagre de Jesus registrado no Novo Testamento?', 'Transformação da água em vinho', 'Ressurreição de Lázaro', 'Caminhar sobre as águas', 'Cura do cego Bartimeu', 'Transformação da água em vinho'),
                ('Quem foi o primeiro mártir cristão?', 'João Batista', 'Estevão', 'Pedro', 'Paulo', 'Estevão'),
                ('Qual foi o nome do rei que ordenou a morte de todos os meninos de Belém com menos de dois anos de idade, na tentativa de matar Jesus?', 'Herodes', 'Pilatos', 'Nero', 'Augusto', 'Herodes'),
                ('Quem foi o fariseu que teve um encontro noturno com Jesus para discutir sobre o Reino de Deus?', 'Nicodemos', 'Gamaliel', 'José de Arimateia', 'Zaqueu', 'Nicodemos'),
                ('Qual dos apóstolos de Jesus negou conhecê-lo três vezes antes do galo cantar?', 'Pedro', 'João', 'André', 'Tiago', 'Pedro'),
                ('Qual dos apóstolos de Jesus era conhecido como o "discípulo amado"?', 'Pedro', 'João', 'Tiago', 'Mateus', 'João'),
                ('Qual era o nome do governador romano que ordenou a crucificação de Jesus?', 'Pôncio Pilatos', 'Herodes Antipas', 'Nero', 'Tibério César', 'Pôncio Pilatos'),
                ('Quem foi o primeiro a ver Jesus após sua ressurreição?', 'Pedro', 'Maria Madalena', 'João', 'Tomé', 'Maria Madalena'),
                ('Quem foi o profeta que batizou Jesus nas águas do rio Jordão?', 'Isaías', 'Jeremias', 'João Batista', 'Ezequiel', 'João Batista'),
                ('Qual dos discípulos de Jesus era conhecido como "o discípulo que Jesus amava"?', 'Pedro', 'Tiago', 'João', 'Mateus', 'João'),
                ('Quem foi o apóstolo que traiu Jesus com um beijo?', 'Pedro', 'André', 'Tiago', 'Judas', 'Judas'),
                ('Qual dos discípulos de Jesus duvidou de sua ressurreição até que visse Jesus com seus próprios olhos?', 'Pedro', 'Mateus', 'João', 'Tomé', 'Tomé'),
                ('Qual dos discípulos de Jesus era conhecido como "o filho do trovão"?', 'Pedro', 'André', 'Tiago', 'João', 'Tiago'),
                ('Quem foi o fariseu que condenou Jesus à morte?', 'Nicodemos', 'Gamaliel', 'José de Arimateia', 'Caiaphas', 'Caiaphas'),
                ('Quem foi o homem que ajudou Jesus a carregar a cruz até o Calvário?', 'Pilatos', 'José de Arimateia', 'Simão de Cirene', 'Herodes', 'Simão de Cirene'),
                ('Quem foi o discípulo que negou Jesus três vezes antes do galo cantar?', 'João', 'Pedro', 'André', 'Mateus', 'Pedro'),
                ('Quem foi o fariseu que reconheceu Jesus como "Mestre vindo de Deus"?', 'Nicodemos', 'Gamaliel', 'José de Arimateia', 'Zaqueu', 'Nicodemos'),
                ('Quem foi o centurião romano que reconheceu Jesus como o Filho de Deus durante a crucificação?', 'Pilatos', 'José de Arimateia', 'Simão de Cirene', 'Cornélio', 'Cornélio'),
                ('Quem foi a mulher que ungiu Jesus com perfume caro antes de sua crucificação?', 'Maria Madalena', 'Maria, mãe de Jesus', 'Maria de Betânia', 'Maria, mãe de Tiago e de José', 'Maria de Betânia'),
                ('Quem foi o judeu que pediu o corpo de Jesus a Pilatos para sepultá-lo?', 'Nicodemos', 'Gamaliel', 'José de Arimateia', 'Zaqueu', 'José de Arimateia'),
                ('Quem foi o homem que Jesus encontrou sentado em uma figueira e o chamou pelo nome?', 'Zacarias', 'Zaqueu', 'Bartimeu', 'Simão', 'Zacarias'),
                ('Quem foi o discípulo que Jesus amava e que estava ao pé da cruz durante a crucificação?', 'Pedro', 'André', 'Tiago', 'João', 'João'),
                ('Quem foi o judeu que entregou Jesus a Pilatos?', 'Nicodemos', 'Gamaliel', 'Judas Iscariotes', 'Zaqueu', 'Judas Iscariotes')
            ]

            self.sql_questions = """
                INSERT OR IGNORE INTO questions(pergunta, alternativa_1,alternativa_2, alternativa_3, alternativa_4, resposta) VALUES (?, ?, ?,?, ?, ?)
            """
            

            # for self.ques in self.values:
            self.cursor.executemany(self.sql_questions, self.values)
            self.conectar.commit()

        except sqlite3.Error as error:
            print('Erro na função "insert_questions"', error)

    def take_10__questions(self):

        self.sql_10 = """
            SELECT * FROM questions ORDER BY RANDOM() LIMIT 10
        """
        self.cursor.execute(self.sql_10)
        self.questions10 = self.cursor.fetchall()
        
        return self.questions10

if __name__ == "__main__":
    mybd = BancoDeDadosQuestions()



