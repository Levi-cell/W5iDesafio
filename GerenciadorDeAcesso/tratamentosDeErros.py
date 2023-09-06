import re
def trataNome(nome):
    while not nome.isalpha() or len(nome) < 3:
        nome = input("Nome inválido, por favor digite novamente:" + "\n")
    return nome


def trataCPF():
    while True:
        cpf = input("Agora Digite o CPF nesse formato: 'xxx.xxx.xxx-xx': ")
        cpfFormatado = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        if re.match(cpfFormatado, cpf):
            cpfNumeros = cpf.replace(".", "").replace("-", "")
            if len(cpfNumeros) == 11 and cpfNumeros.isdigit():
                return cpf
        print("CPF inválido. Por favor digite novamente.")
