
#Importar biblioteca tkinter para visualização gráfica
from tkinter import *
 
#Importar caixa de mensagem como mb
from tkinter import messagebox as mb
 
from datetime import date

#import json to use json file for data
import json

import mysql.connector
class Quiz:
    
    #inicializa o quiz
    def __init__(self):
        
        self.opt_buttons()

    def game(self):

        def getname(text):
            self.name = text
            janela.destroy()

        janela = Tk()
        janela.title("Jogador")
        texto = Label(janela, text="Nome do Jogador:")
        texto.grid(column=0, row=0)
        codigo = Entry(janela, width=100)
        codigo.grid(column=0, row=1)
        botao = Button(janela, text="Jogar", command=lambda: getname(codigo.get()))
        botao.grid(column=0, row=2)
        
        self.num_question = 0

        self.display_title()
        
        self.display_question()

        self.opt_selected = IntVar()

        self.opts = self.radio_buttons()

        self.display_options()
         
        self.buttons()

        self.data_size = len(question)

        self.correct = 0
    
    #Objeto de resultado do quiz
    def display_result(self):
         
        #Calculo de acertos e erros
        wrong_count = self.data_size - self.correct
        correct = f"Acertos: {self.correct}"
        wrong = f"Erros: {wrong_count}"
         
        #Calcula a porcentagem de acertos
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        
        #Mostra o resultado
        mb.showinfo("Resultado", f"{result}\n{correct}\n{wrong}")
        self.insert_ranking(self.name, score)
       
        self.select_ranking()
        
 
    #Verificação de acerto ou não da resposta
    def check_ans(self, num_question):

        if self.opt_selected.get() == answer[num_question]:
            return True
 
    #Chamada do botão next
    def next_btn(self):
         
        #Verifica se a resposta ta certa
        if self.check_ans(self.num_question):
             
            self.correct += 1
            
        self.num_question += 1
         
        #Verifica se acabaram as questões
        if self.num_question == self.data_size:
             
            #Mostra o resultado
            self.display_result()

            gui.destroy()
        else:
            #Mostra a proxima questão
            self.display_question()
            self.display_options()
    
    #Objeto de resultado do quiz
    def ranking_btn(self):
        self.select_ranking()

     #Objeto de resultado do quiz
    def deltRank_btn(self):
        self.delete_ranking()

    def opt_buttons(self):

        #Botão Ranking
        ranking_button = Button(gui, text = "Ver Ranking", command = self.ranking_btn,
        width = 10, bg = "blue", fg = "black", font = ("ariel", 16, "bold"))

        ranking_button.place(x = 15, y = 50)
         
        #Botão Delete Ranking
        delRank_button = Button(gui, text = "Deletar Ranking", command = self.deltRank_btn,
        width = 10, bg = "black", fg = "black", font = ("ariel", 16, " bold"))

        delRank_button.place(x = 160, y = 50)

        #Botão jogar
        play_button = Button(gui, text = "Jogar", command = self.game,
        width = 10, bg = "black", fg = "black", font = ("ariel", 16, " bold"))

        play_button.place(x = 305, y = 50)

    #Criação e disposição gráfica dos botões 
    def buttons(self):
         
        #Botão Próxima
        next_button = Button(gui, text = "Próxima", command = self.next_btn,
        width = 10, bg = "blue", fg = "black", font = ("ariel", 16, "bold"))

        next_button.place(x = 350, y = 380)
         
        #Botão Sair
        quit_button = Button(gui, text = "Sair", command = gui.destroy,
        width = 5,bg = "black", fg = "grey", font = ("ariel", 16, " bold"))

        quit_button.place(x = 700, y = 50)

    #Carrega as opções
    def display_options(self):
        val = 0
         
        self.opt_selected.set(0)
         
        #Mostra todas as opções
        for option in options[self.num_question]:
            self.opts[val]['text'] = option
            val += 1
 
 
    #Mostra as opções
    def display_question(self):
         
        num_question = Label(gui, text = question[self.num_question], width = 60,
        font = ( 'ariel', 16, 'bold' ), anchor = 'w')

        num_question.place(x = 70, y = 100)
 
 
    #Mostra o titulo
    def display_title(self):
         
        title = Label(gui, text = "QUIZ DO MEIO AMBIENTE",
        width = 60, bg = "green", fg = "white", font = ("ariel", 20, "bold"))
         
        title.place(x = 0, y = 2)
 
 
    #Cria objeto radio botão
    def radio_buttons(self):
         
        #Inicializa a lista de opções
        q_list = []
         
        y_pos = 150
         
        #Adiciona as opções na lista
        while len(q_list) < 5:
             
            radio_btn = Radiobutton(gui, text = " ", variable = self.opt_selected,
            value = len(q_list) + 1, font = ("ariel", 14))

            q_list.append(radio_btn)

            radio_btn.place(x = 100, y = y_pos)
             
            y_pos += 40
        return q_list

    def insert_ranking(self, nome, pontuacao):
        con = mysql.connector.connect(host = '127.0.0.1', database = 'db_quiz', user = 'root', password = '')
        if con.is_connected():
            cursor = con.cursor()
            current_date = date.today()
            formatted_date = current_date.strftime("%d/%m/%Y")

            sql = "INSERT INTO ranking(name, pontuacao, date) VALUES (%s, %s, %s)"
            values = (nome, pontuacao, formatted_date)
            cursor.execute(sql, values)
            con.commit()
            mb.showinfo("Ranking", "Adicionado ao Ranking!")
            return

    def select_ranking(self):
        con = mysql.connector.connect(host = '127.0.0.1', database = 'db_quiz', user = 'root', password = '')
        if con.is_connected():
            cursor = con.cursor()
            sql = ("SELECT name, pontuacao, date FROM ranking ORDER BY pontuacao DESC")
            cursor.execute(sql)
            aRanking = ""
            count = 0
            myresult = cursor.fetchall()
            for x in myresult:
                count = count + 1
                aRanking = aRanking + f"{count}º:  {x}\n"

            if aRanking == "":
                aRanking = "Ranking vazio! Jogue pra iniciar!"

            mb.showinfo("Ranking", aRanking)
            return 

    def delete_ranking(self):
        con = mysql.connector.connect(host = '127.0.0.1', database = 'db_quiz', user = 'root', password = '')
        if con.is_connected():
            cursor = con.cursor()
            sql = ("DELETE from ranking")
            cursor.execute(sql)
            con.commit()
            cursor.close()
            mb.showinfo("Ranking", "Ranking deletado!\nJogue novamente para iniciar um novo ranking!")
            return
    

#Cria objeto grafico
gui = Tk()
 
#Tamanho da tela
gui.geometry("800x450")
 
#Nome na janela (titulo)
gui.title("QUIZ DO MEIO AMBIENTE")
 
#Informações do quiz do arquivo data.json
with open('data.json') as f:
    data = json.load(f)
 
#
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
 
quiz = Quiz()

gui.mainloop()
 