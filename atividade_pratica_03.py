# Criando um programa para classificar a idade
idade = int(input("Digite a sua idade: "))

if idade <= 12:
    print("Você é uma criança!")

elif idade < 18:
    print("Você é um adolescente!")

elif idade < 60:
    print("Você é um adulto!")

else:
    print("Você é um idoso!")


# Criando um programa que calcula o IMC
peso = float(input("\n Digite o seu peso: "))
altura = float(input("\n Digite a sua altura: "))
classificacao = peso / altura ** 2

if classificacao < 18.5:
    print(f"\n Seu IMC é: {classificacao:.2f}")
    print(" Abaixo do peso")

elif classificacao < 25:
    print(f"\n Seu IMC é: {classificacao:.2f}")
    print(" Peso normal")

elif classificacao < 30:
    print(f"\n Seu IMC é: {classificacao:.2f}")
    print(" Sobrepeso")
else:
    print(f"\n Seu IMC é: {classificacao:.2f}")
    print(" Obeso")


# Criando um programa que converte a temperatura
origem = input("""\n Escolha a unidade de temperatura:
(C) Celsius
(F) Fahrenheit
(K) Kelvin
""").upper()

temp = float(input("\n Digite a temperatura: "))

if origem == "C":
    destino = input("\n Converter para: \n" 
    "(F) Fahrenheit \n" 
    "(K) Kelvin \n").upper()

    if destino == "F":
        resultado = (temp * 9/5) + 32
        print(f"\n Temperatura inicial em °C: {temp} \n"
        f"Temperatura final convertida para ºF: {resultado:.1f} \n")

    elif destino == "K":
        resultado = temp + 273
        print(f"\n Temperatura inicial em °C: {temp} \n"
        f"Temperatura final convertida para ºK: {resultado:.1f} \n")

elif origem == "F":
    destino = input("\n Converter para: \n" 
    "(C) Celsius \n" 
    "(K) Kelvin \n").upper()

    if destino == "C":
        resultado = (temp - 32) * 5/9
        print(f"\n Temperatura inicial em °F: {temp} \n"
        f"Temperatura final convertida para ºC: {resultado:.1f} \n")

    elif destino == "K":
        resultado = (temp - 32) * 5/9 + 273
        print(f"\n Temperatura inicial em °F: {temp} \n"
        f"Temperatura final convertida para ºK: {resultado:.1f} \n")

elif origem == "K":
    destino = input("\n Converter para: \n" 
    "(C) Celsius \n" 
    "(F) Fahrenheit \n").upper()

    if destino == "C":
        resultado = temp - 273
        print(f"\n Temperatura inicial em °K: {temp} \n"
        f"Temperatura final convertida para ºC: {resultado:.1f} \n")

    elif destino == "F":
        resultado = (temp - 273) * 9/5 + 32
        print(f"\n Temperatura inicial em °K: {temp} \n"
        f"Temperatura final convertida para ºF: {resultado:.1f} \n")

# Criando um programa que verifica se o ano é bissexto
ano = int(input("Digite um ano:"))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano de {ano} é bissexto!")

else:
    print(f"o ano de {ano} não é bissexto!")