from funcoesGerenciamento import *
from banco import conexao, cursor


while True:

    menu = input("""Seja bem vindo ao Gerenciamento de Acesso, o que deseja fazer?
    1 - Se Cadastrar no nosso sistema
    2 - Entrar na Operação
    3 - Sair da Operação
    Digite a opção que deseja:""" + "\n")

    if menu == "1":
        funcionario = adicionaFuncionario()
        cursor.execute("INSERT INTO funcionarios (nome,sobrenome, CPF) VALUES (?, ?, ?)",
                       (funcionario.nome, funcionario.sobrenome, funcionario.cpf,))
        conexao.commit()
        cursor.execute("SELECT * FROM funcionarios WHERE nome = ?", (funcionario.nome,))
        resultado = cursor.fetchone()

        print("Funcionário inserido com sucesso:")
        print("ID:", resultado[0])
        print("Nome:", resultado[1])
        print("Sobrenome:", resultado[2])
        print("CPF:", resultado[3] + "\n")

    if menu == "2":
        entrada()

    if menu == "3":
        saida()

    opcao = input("""Digitou a opção errada ou deseja fazer mais alguma coisa ?
    Digite S para prosseguir ou digite qualquer tecla para encerrar o programa: """ + "\n")
    if opcao == "N":
        break

