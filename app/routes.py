from app import app
<<<<<<< HEAD
from flask import request, redirect, url_for, render_template
import sqlite3
from datetime import datetime
=======
from app import _init_
>>>>>>> c58311c0b944653f37b2152f751863f72e9f3974


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
<<<<<<< HEAD
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return render_template('produto.html', produtos=produtos)


@app.route('/adicionar', methods=['GET', 'POST'])
=======
    conectar = conectar_db()
    cursor = conectar.cursor()
    
    cursor.execute(
            'SELECT * FROM produto'
    )
    #produto = cursor.fetchall()
    conectar.close()

    return render_template('produto.html')



@app.route('/adicionar', methods = ['POST'])
>>>>>>> c58311c0b944653f37b2152f751863f72e9f3974
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
<<<<<<< HEAD
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
=======
        quant = request.form['quantidade']
        val = request.form['validade']
        desc = request.form['descricao']

        conectar = conectar_db()
        cursor = conectar.cursor()
        
        cursor.execute(
            'INSERT INTO produto (nomeProduto, preco, quantidade, validade, descricao) VALUES (?, ?, ?, ?, ?)', (nome, preco, quant, val, desc)
        )
        
        conectar.commit()
        conectar.close()
        flash('Produto adicionado com sucesso!', 'success')
>>>>>>> c58311c0b944653f37b2152f751863f72e9f3974

        return render_template('adicionar.html')

<<<<<<< HEAD
@app.route('/alterar')
def alterar():
    return render_template('alterar.html')
=======
if __name__ == '__main__':
    criar_tabela_produto()
    app.run(debug=True)
>>>>>>> c58311c0b944653f37b2152f751863f72e9f3974
