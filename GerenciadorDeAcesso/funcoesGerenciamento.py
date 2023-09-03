from funcionario import Funcionario
from banco import *
from datetime import datetime
from tratamentosDeErros import trataCPF, trataNome


def adicionaFuncionario():

    nome = input("Para fazer parte do nosso sistema comece digitando o seu nome: " + "\n")
    nome = trataNome(nome)
    sobrenome = input("Seu sobrenome:" + "\n")
    sobrenome = trataNome(sobrenome)
    cpf = trataCPF()

    novoFuncionario = Funcionario(nome, sobrenome, cpf)

    return novoFuncionario


# comentar outra forma
def tempoExpediente(idFuncionario, idFuncionario1):
    cursor.execute("""SELECT strftime('%s',  MAX(rs.data_hora_saida)) - strftime('%s', MAX(re.data_hora_entrada))
                      FROM registro_entrada re 
                      INNER JOIN registro_saida rs      
                      WHERE re.codigo_funcionario = ? and rs.codigo_funcionario = ?"""
                   , (idFuncionario, idFuncionario1,))
    diferenca = cursor.fetchall()
    return diferenca


def entrada():
    cpf = input("Antes de entrar na operação, Digite o seu CPF: " + "\n")
    cursor.execute("""SELECT * FROM funcionarios 
     WHERE CPF = ?""", (cpf,))
    resultado = cursor.fetchone()

    if resultado:

        quantidadeEntradas, quantidadeSaidas = consultaEntradasSaidasPorFuncionario(resultado[0])
        if quantidadeEntradas > quantidadeSaidas:
            print("Você já entrou, agora você deve sair...." + "\n")
        else:
            horaInicio = datetime.now()
            cursor.execute("""INSERT INTO registro_entrada (data_hora_entrada, codigo_funcionario)
                                              VALUES(?, ?)""", (horaInicio, resultado[0],))
            conexao.commit()
            print(f"""Olá {resultado[1]} seja bem vindo a operação, a contagem do seu tempo
            de trabalho começa agora, data e hora de ínicio: {horaInicio}  """ + "\n")

    else:
        print("Você não está no nosso banco de dados." + "\n")


def saida():
    cpf = input("Antes de sair da operação, Digite o seu CPF:" + "\n")
    cursor.execute("""SELECT * FROM funcionarios WHERE CPF = ?""", (cpf,))
    resultado = cursor.fetchone()

    if resultado:

        quantidadeEntradas, quantidadeSaidas = consultaEntradasSaidasPorFuncionario(resultado[0])

        if quantidadeEntradas == quantidadeSaidas:
            print("Você já está fora da operação, agora você deve entrar." + "\n")
        else:
            horaTermino = datetime.now()

            # Pegando a ultima entrada do funcionário
            cursor.execute("""INSERT INTO registro_saida (data_hora_saida, codigo_funcionario)
            VALUES (?, ?)""", (horaTermino, resultado[0],))
            conexao.commit()

            diferenca = tempoExpediente(resultado[0], resultado[0])
            # descompactando
            segundos = diferenca[0][0]
            segundoFloat = float(segundos)

            # adicionando o tempo do expediente na tabela operacao

            cursor.execute("""INSERT INTO operacao (tempo_da_operacao_em_segundos, codigo_funcionario)
            VALUES (?, ?)""", (segundoFloat, resultado[0],))
            conexao.commit()
            print(f"{resultado[1]} tenha um bom descanso, data e hora de termino: {horaTermino} ")
            print(f"""Duração do expediente foi de: {segundoFloat} segundos""" + "\n")


    else:
        print("Você não está no nosso banco de dados" + "\n")


def consultaEntradasSaidasPorFuncionario(idFuncionario):

    cursor.execute("""SELECT COUNT(id_registro_entrada) FROM registro_entrada WHERE codigo_funcionario = ? """
                   , (idFuncionario,))

    quantidadeEntradas = cursor.fetchall()

    cursor.execute("""SELECT COUNT(id_registro_saida) FROM registro_saida  WHERE codigo_funcionario = ? """
                   , (idFuncionario,))

    quantidadeSaidas = cursor.fetchall()

    return quantidadeEntradas, quantidadeSaidas





