# Criando um Programa que converte um valor em reais para dólares e euros
valor = float(input("Digite o valor em reais: "))
dolar = valor / 5.20
euro = valor / 6.15

print(f"""
O valor em reias é: {valor:.2f}
O valor em dólares é: {dolar:.2f}
O valor em euros é: {euro:.2f}
""")

# Criando um Programa que calcula o desconto em uma loja
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço: "))
desconto = preco * 20 / 100
valor_final = preco - desconto

print(f"""
Nome do Produto: {produto}
Preço: {preco}
Desconto: 20%
Valor Final: {valor_final:.2f}
""")

# Criando um Programa que calcula a média escolar de um aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

print(f"""
Nota 1: {nota1}
Nota 2: {nota2}
Nota 3: {nota3}
Média: {media:.2f}
""")

# Criando um Programa que calcula o consumo médio de combustível de um veículo
distancia = float(input("Digite a distância percorrida em km: "))
combustivel = float(input("Digite a quantidade de combustível em litros: "))
consumo = distancia / combustivel

print(f"""
Distância percorrida: {distancia} km
Combustível gasto: {combustivel} litros
O consumo médio foi: {consumo:.2f} km/l
""")