# Criando uma calculadora com operações básicas
operacao = input("Escolha uma operação: \n"
                 "(1) Soma \n"
                 "(2) Subtração \n"
                 "(3) Multiplicação \n"
                 "(4) Divisão \n")

n1 = float(input("\nDigite o primeiro número: \n"))
n2 = float(input("\nDigite o segundo número: \n"))

if operacao == "1":
    resultado = n1 + n2
    print(f"\nO resultado da soma de {n1} + {n2} é: {resultado:.2f}")

elif operacao == "2":
    resultado = n1 - n2
    print(f"\nO resultado da subtração de {n1} - {n2} é: {resultado:.2f}")

elif operacao == "3":
    resultado = n1 * n2
    print(f"\nO resultado da multiplicação de {n1} * {n2} é: {resultado:.2f}")

elif operacao == "4":
    resultado = n1 / n2
    print(f"\nO resultado da divisão de {n1} / {n2} é: {resultado:.2f}")

# Criando um programa para calcular a média de uma turma
qntd_alunos = int(input("Digite a quantidade de alunos: \n"))
soma_media = 0

for i in range (qntd_alunos):
    print(f"\nDigite os dados do Aluno {i+1}")

    nome = input("\nNome: ")
    nota1 = float(input("\nNota 1: "))
    nota2 = float(input("\nNota 2: "))

    media_aluno = (nota1 + nota2) / 2

    soma_media += media_aluno


media_geral = soma_media / qntd_alunos

print(f"A média geral da turma é igual a: {media_geral:.2f}")


# Criando um programa para verificar critérios de senha

senha = input("Digite uma senha: ")

if len(senha) < 8:
    print("\nA senha precisa ter pelo menos 8 caracteres!")

else:
    tem_numero = False

    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break
    
    if tem_numero == True:
        print("\nSua senha atende aos critérios de segurança!")
    
    else:
        print("\nSua senha não atende aos critérios de segurança!")

# Criando um programa para analisar números digitados
qntd_numeros = int(input("Digite a quantidade de números que você quer analisar: \n"))

soma_par = 0
soma_impar = 0

for i in range(qntd_numeros):
    numero = int(input(f"\nDigite o {i+1} número: \n"))

    if numero % 2 == 0:
        print(f"\nO número {numero} é um número par")
        soma_par += 1

    else:
        print(f"\nO número {numero} é um número ímpar")
        soma_impar += 1

print(f"\nQuantidade de números pares: {soma_par}")
print(f"\nQuantidade de números ímpares: {soma_impar}")
