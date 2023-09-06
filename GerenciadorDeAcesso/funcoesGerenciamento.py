from funcionario import Funcionario
from banco import *
from datetime import datetime
from tratamentosDeErros import trataCPF, trataNome


def adicionaFuncionario():

    nome = input("Para fazer parte do nosso sistema comece digitando o seu nome: " + "\n")
    nome = trataNome(nome)
    sobrenome = input("Seu sobrenome:" + "\n")
    sobrenome = trataNome(sobrenome)

    while True:
        cpf = trataCPF()
        cursor.execute("""SELECT * FROM funcionarios WHERE CPF = ?""", (cpf,))
        verificacao = cursor.fetchone()

        if verificacao is not None:
            print("Esse CPF já consta no nosso banco de dados.....")
            opcao = input("Deseja retornar para o menu ? Digite S para sim ou N para não: \n")
            if opcao == "S":
                return
        else:
            break

    novoFuncionario = Funcionario(nome, sobrenome, cpf)
    if novoFuncionario is not None:
        cursor.execute("INSERT INTO funcionarios (nome,sobrenome, CPF) VALUES (?, ?, ?)",
                       (novoFuncionario.nome, novoFuncionario.sobrenome, novoFuncionario.cpf,))
        conexao.commit()
        cursor.execute("SELECT * FROM funcionarios WHERE CPF = ?", (novoFuncionario.cpf,))
        resultado = cursor.fetchone()

    print("Funcionário inserido com sucesso:")
    print("ID:", resultado[0])
    print("Nome:", resultado[1])
    print("Sobrenome:", resultado[2])
    print("CPF:", resultado[3] + "\n")

    return


# comentar outra forma
def tempoExpediente(idFuncionario, idFuncionario1):
    cursor.execute("""SELECT (strftime('%s',  MAX(rs.data_hora_saida)) - strftime('%s', MAX(re.data_hora_entrada)))
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
            # Consultas auxiliares para apresentação
            cursor.execute("SELECT MAX(DATE(data_hora_entrada)) FROM registro_entrada WHERE codigo_funcionario = ?",
                           (resultado[0],))
            dataEntrada = cursor.fetchone()

            cursor.execute("SELECT MAX(strftime('%H:%M:%S', data_hora_entrada)) FROM registro_entrada"
                           " WHERE codigo_funcionario = ?",
                           (resultado[0],))
            horaEntrada = cursor.fetchone()

            print(f"Olá {resultado[1]} {resultado[2]}"
                  f" seja bem vindo a operação, a contagem do seu tempo de trabalho começa agora... \n")
            print(f"data de entrada na operação: {dataEntrada[0]}")
            print(f"hora de entrada na operação: {horaEntrada[0]} \n")

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
            horas = diferenca[0][0]
            horas = float(horas)
            horas = horas/3600

            # adicionando o tempo do expediente na tabela operacao

            cursor.execute("""INSERT INTO operacao (tempo_da_operacao_em_segundos, codigo_funcionario)
            VALUES (?, ?)""", (horas, resultado[0],))
            conexao.commit()

            # Consultas auxiliares para apresentação
            cursor.execute("SELECT MAX(DATE(data_hora_entrada)) FROM registro_entrada WHERE codigo_funcionario = ?",
                           (resultado[0],))
            dataEntrada = cursor.fetchone()

            cursor.execute("SELECT MAX(strftime('%H:%M:%S', data_hora_entrada)) FROM registro_entrada"
                           " WHERE codigo_funcionario = ?",
                           (resultado[0],))
            horaEntrada = cursor.fetchone()

            cursor.execute("SELECT MAX(DATE(data_hora_saida)) FROM registro_saida WHERE codigo_funcionario = ?",
                           (resultado[0],))
            dataSaida = cursor.fetchone()

            cursor.execute("SELECT MAX(strftime('%H:%M:%S',data_hora_saida)) FROM registro_saida"
                           " WHERE codigo_funcionario = ?",
                           (resultado[0],))
            horaSaida = cursor.fetchone()

            print(f"Olá {resultado[1]} {resultado[2]}"
                  f" Bom Descanso, a contagem do seu tempo de trabalho termina agora...")
            print("Dados de Entrada:\n")
            print(f"data de entrada na operação: {dataEntrada[0]}")
            print(f"hora de entrada na operação: {horaEntrada[0]} \n")
            print("Dados de Saída:\n")
            print(f"data de saida na operação: {dataSaida[0]}")
            print(f"hora de saida na operação: {horaSaida[0]} \n")
            if horas >= 0.01:
                print(f"Duração do expediente em horas: {horas:.3f} horas")
            else:
                print(f"Duração do expediente em horas: {horas:.7f} horas")


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





