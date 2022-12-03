
#Importar biblioteca tkinter para visualização gráfica
from tkinter import *

from connect import * 
#Importar caixa de mensagem como mb
from tkinter import messagebox as mb
 
#import json to use json file for data
import json
 
class Quiz:
    
    #inicializa o quiz
    def __init__(self):
         
        self.num_question = 0

        self.display_title()
        self.input()
        
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
        correct = f"Acertos: {self.correct} {self.name}"
        wrong = f"Erros: {wrong_count}"
         
        #Calcula a porcentagem de acertos
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        insert_ranking(self.name, score)
        #Mostra o resultado
        mb.showinfo("Resultado", f"{result}\n{correct}\n{wrong}")
 
 
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
 
    def input(self):
        self.name = input("Digite o nome do usuário:")

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
 