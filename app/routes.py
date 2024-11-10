from app import app
from app import _init_

from flask import render_template


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')


@app.route('/produto')
def produto():
    conectar = conectar_db()
    cursor = conectar.cursor()
    
    cursor.execute(
            'SELECT * FROM produto'
    )
    #produto = cursor.fetchall()
    conectar.close()

    return render_template('produto.html')



@app.route('/adicionar', methods = ['POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['Nome']
        preco = request.form['Preço']
        quant = request.form['Quantidade']
        val = request.form['Validade']
        desc = request.form['Descrição']

        conectar = conectar_db()
        cursor = conectar.cursor()
        
        cursor.execute(
            'INSERT INTO produto (nomeProduto, preco, quantidade, validade, descricao) VALUES (?, ?, ?, ?, ?)', (nome, preco, quant, val, desc)
        )
        
        conectar.commit()
        conectar.close()
        flash('Produto adicionado com sucesso!', 'success')

        return render_template('adicionar.html')

if __name__ == '__main__':
    criar_tabela_produto()
    app.run(debug=True)
