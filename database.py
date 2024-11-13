import sqlite3

# Conecta ao banco de dados (ou cria um se não existir)
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

# Cria a tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL,
    validade TEXT NOT NULL,
    descricao TEXT
)
''')

conn.commit()
conn.close()
