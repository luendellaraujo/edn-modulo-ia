from datetime import date

# Criando uma função que calcula a gorjeta em um restaurante
def calcular_gorjeta(conta, porcentagem):
    gorjeta = conta * (porcentagem / 100)
    return gorjeta


valor_conta = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = float(input("\nDigite a porcentagem da gorjeta: "))

valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

print(f"""
Valor da conta: {valor_conta:.2f}
Porcentagem da gorjeta: {porcentagem_gorjeta}%
Valor da gorjeta: {valor_gorjeta:.2f}
""")

# Criando uma função que verifica se uma palavra ou frase é um palíndromo
def verificar_palindromo(texto):
    texto_sem_espaco = texto.replace(" ", "")

    apenas_letras = ""

    for letra in texto_sem_espaco:
        if letra.isalnum():
            apenas_letras += letra

    apenas_letras = apenas_letras.lower()

    if apenas_letras == apenas_letras[::-1]:
        return True
    else: 
        return False

texto_usuario = input("Digite uma palavra ou frase: ")

if verificar_palindromo(texto_usuario):
    print("\nÉ palíndromo!")
else:
    print("\nNão é palíndromo!")


# Criando um programa para calcular o preço final de um produto após aplicar desconto percentual
valor_produto = float(input("Digite o valor do produto: "))
porcentagem_desconto = float(input("\nDigite a porcentagem de desconto: "))
valor_desconto = valor_produto * (porcentagem_desconto / 100)
valor_final = valor_produto - valor_desconto

print(f"""
Valor do Produto: R${valor_produto}
Porcentagem do desconto: {porcentagem_desconto}%
Valor final com o desconto: R${valor_final:.2f}
""")

# Criando um programa que calcula quantoa dias uma pessoa está viva

dia = int(input("Digite o dia de nascimento: "))
mes = int(input("\nDigite o mês de nascimento: "))
ano = int(input("\nDigite o ano de nascimento: "))

data_nascimento = date(ano, mes, dia)
data_hoje = date.today()

diferenca = data_hoje - data_nascimento

print(f"Hoje é dia: {data_hoje.day}/{data_hoje.month}/{data_hoje.year}")
print(f"Você está vivo há: {diferenca.days} dias!")