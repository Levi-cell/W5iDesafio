from banco import cursor

cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        sobrenome TEXT,
        CPF TEXT)''')

cursor.execute("""
CREATE TABLE IF NOT EXISTS registro_entrada(
id_registro_entrada INTEGER PRIMARY KEY AUTOINCREMENT,
data_hora_entrada DATETIME NOT NULL,
codigo_funcionario INTEGER NOT NULL,
FOREIGN KEY (codigo_funcionario) REFERENCES funcionarios(id_funcionario)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS registro_saida(
id_registro_saida INTEGER PRIMARY KEY AUTOINCREMENT,
data_hora_saida DATETIME NOT NULL,
codigo_funcionario INTEGER NOT NULL,
FOREIGN KEY (codigo_funcionario) REFERENCES funcionarios(id_funcionario)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS operacao(
id_operacao INTEGER PRIMARY KEY AUTOINCREMENT,
tempo_da_operacao_em_segundos REAL NOT NULL,
codigo_funcionario INTEGER NOT NULL,
FOREIGN KEY (codigo_funcionario) REFERENCES funcionarios(id_funcionario)
)""")

