from flask import Flask, flash
from app import routes

import sqlite3

app = Flask(__name__)

#conexão do BD ao back-end
def conectar_db():
  conectar = sqlite3.connect('banco.db')
  return conectar

def criar_tabela_produto():
  conectar = conectar_db()
  cursor = conectar.cursor()
  cursor.execute ('''
    create table if not exists produto (
      idProduto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      nomeProduto TEXT NOT NULL,
      preco NUMERIC NOT NULL, 
      quantidade NUMERIC NOT NULL,
      validade TEXT NOT NULL,
      descricao TEXT NOT NULL,
    )
  ''')
  conectar.commit()
  conectar.close()

