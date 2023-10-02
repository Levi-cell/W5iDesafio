from funcoesGerenciamento import *
from banco import conexao, cursor


while True:

    menu = input("""Seja bem vindo ao Gerenciamento de Acesso, o que deseja fazer?
    1 - Se Cadastrar no nosso sistema
    2 - Entrar na Operação
    3 - Sair da Operação
    Digite a opção que deseja:""" + "\n")

    if menu == "1":
        adicionaFuncionario()

    if menu == "2":
        entrada()

    if menu == "3":
        saida()

    print("Digitou a opção errada ou deseja fazer mais alguma coisa ?")
    opcao = input("Caso sim,"
                  "digite S para voltar ao menu ou digite N para encerrar o programa: " + "\n")
    if opcao == "N":
        break

