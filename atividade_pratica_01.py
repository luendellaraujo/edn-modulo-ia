# Criando um programa que imprimi a mensagem "Olá, mundo!"
print("Olá, mundo! \n")

# Criando um programa que soma dois números
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
resultado = n1 + n2

print(f"O resultado da soma de {n1} + {n2} é: {resultado} \n")

# Criando um programa que calcula o volume
comprimento = float(input("Digite o comprimento: "))
largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
volume = comprimento * largura * altura

print(f"O volume é: {volume}cm³ \n")

#Criando um programa que calcula o preço total de uma compra
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço: "))
qnt = int(input("Digite a quantidade: "))
preco_total = preco * qnt


print(f"""
Nome do produto: {produto}
Preço: {preco}
Quantidade: {qnt}
Valor total da compra: {preco_total}
""")