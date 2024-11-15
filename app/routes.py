from app import __init__
from app import app
from flask import request, redirect, url_for, render_template
import sqlite3
from datetime import datetime

# Função para conectar ao banco de dados


def get_db_connection():
    conn = sqlite3.connect('produtos.db')
    conn.row_factory = sqlite3.Row
    return conn


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

    # Formatar a data para o padrão brasileiro
    produtos_formatados = []
    for produto in produtos:
        produto_formatado = dict(produto)
        produto_formatado['validade'] = datetime.strptime(
            produto['validade'], "%Y-%m-%d").strftime("%d/%m/%Y")
        produtos_formatados.append(produto_formatado)

    return render_template('produto.html', produtos=produtos_formatados)


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


@app.route('/alterar/<int:id>', methods=['GET', 'POST'])
def alterar(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        quantidade = request.form['quantidade']
        validade = request.form['validade']
        descricao = request.form['descricao']

        cursor.execute('''
            UPDATE produtos
            SET nome = ?, preco = ?, quantidade = ?, validade = ?, descricao = ?
            WHERE id = ?
        ''', (nome, preco, quantidade, validade, descricao, id))
        conn.commit()
        conn.close()

        return redirect(url_for('produto'))
    else:
        cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,))
        produto = cursor.fetchone()
        conn.close()
        return render_template('alterar.html', produto=produto)
