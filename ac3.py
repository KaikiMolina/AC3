#Kaiki Molina Aguiar / RA:2200516


from flask import Flask, request, jsonify

import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


@app.route('/cliente/consulta', methods=["GET"])
def consulta():
    try:
        con = mysql.connector.connect(host='localhost', database='db_Cliente', user='root', password='password')
        consulta_sql = "select * from tb_Cliente"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print("Número total de registros retornados: ", cursor.rowcount)
        print("\nMostrando os autores cadastrados")
        for linha in linhas:
            print("Nome:", linha[0])
            print("Sobrenome:", linha[1])
            print("cpf:", linha[2], "\n")
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()
            print("Conexão ao MySQL encerrada")
    return jsonify(list)


@app.route('/cliente/cadastro', methods=["POST"])
def cadastro():
    try:
        con = mysql.connector.connect(host='localhost', database='db_Cliente', user='root', password='password')
        cursor = con.cursor()
        sql = "INSERT INTO tb_Cliente (nome, sobrenome,cpf) VALUES (%s, %s, %s)"
        val = ("Kaiki", "Molina", "XXX")
        cursor.execute(sql, val)
        con.commit()
        print("\nCadastrado com Sucesso")
    except Error as e:
        print("Erro ao acessar tabela MySQL", e)
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()
            print("Conexão ao MySQL encerrada")
    jsonToReturn = {val['nome'], val['sobrenome'], ", Cadastro realizado"}
    return jsonify(jsonToReturn), 401


@app.route('/cliente/delete', methods=["DELETE"])
def delete(number):
    return "Excluido " + str(number), 401


app.run()
