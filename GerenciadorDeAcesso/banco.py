import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

