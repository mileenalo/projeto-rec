from datetime import date
import mysql.connector
con = mysql.connector.connect(host = '127.0.0.1', database = 'db_quiz', user = 'root', password = '')
if con.is_connected():
    db_info = con.get_server_info()
    #print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    #print("Conectado ao banco de dados ",linha)
#if con.is_connected():
 #   cursor.close()
  #  con.close()
   # print("Conexão ao MySQL foi encerrada")
def insert_ranking(nome, pontuacao):
    current_date = date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')
    sql = "INSERT INTO ranking(name, pontuacao, date) VALUES (%s, %s, %s)"
    values = (nome, pontuacao, formatted_date)
    cursor.execute(sql, values)
    cursor.close()
    return "Pontuação Inserida!"

def select_ranking():
    sql = ("SELECT id, name, pontuacao, data FROM ranking ORDER BY pontuacao DESC")
    cursor.execute(sql)
    cursor.close()
    return cursor

#for (id, name, cpf) in cursor:
 # print(id, name, cpf)
#print("\n")

def delete_ranking(id):
    sql = ("DELETE from ranking WHERE id =" + id + " ")
    cursor.execute(sql)
    cursor.close()
    return "Registro Deletado!"
  
