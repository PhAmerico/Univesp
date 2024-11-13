from app import app
from flask import request, redirect, url_for, render_template
import sqlite3
from datetime import datetime


# conectar ao banco

def get_db_connection():
    conn = sqlite3.connect('produtos.db')
    conn.row_factory = sqlite3.Row
    return conn

# rotas


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/produto')
def produto():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return render_template('produto.html', produtos=produtos)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        quantidade = request.form['quantidade']
        validade = request.form['validade']
        descricao = request.form['descricao']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO produtos (nome, preco, quantidade, validade, descricao)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, preco, quantidade, validade, descricao))
        conn.commit()
        conn.close()

        return redirect(url_for('produto'))

    return render_template('adicionar.html')


@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('produto'))


@app.route('/alterar')
def alterar():
    return render_template('alterar.html')
