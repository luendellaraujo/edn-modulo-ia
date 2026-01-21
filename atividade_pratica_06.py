import requests
import random
import string

# Criando um programa que gera senhas aleatórias com letras, números e símbolos
def gerar_senha():
    print("\nGerador de Senhas")
    try:
        tamanho = int(input("\nDigite o tamanho da senha: "))
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = "".join(random.choice(caracteres) for _ in range(tamanho))
        print(f"\nSenha gerada: {senha} \n")
    except ValueError:
        print("Erro: Digite apenas números para definir o tamanho da senha!")


gerar_senha()

# Criando um programa que acessa a API para buscar um usuário fictício aleatório
def buscar_usuario_aleatorio():
    print("\nBuscar Usuário Fictício")
    print("\nBuscando...")
    try:
        url = "https://randomuser.me/api/"
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            usuario = dados["results"][0]
            
            nome = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']
            
            print(f"""
Usuário encontrado
Nome: {nome}
E-mail: {email}
País: {pais}
""")
        else:
            print("Erro ao conectar na API.")
    except:
        print("Falha na conexão.")


buscar_usuario_aleatorio()

# Criando um programa que consulte informações de um CEP na API
def consultar_cep(cep):
    cep = cep.replace("-","").strip()

    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Digite um CEP com 8 números!")
        return 
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Erro ao acessar a API via CEP")
        return
    
    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado!")
        return
    
    print("\n Endereço encontrado: ")
    print(f"Logradouro: {dados.get('logradouro')}")
    print(f"Bairro: {dados.get('bairro')}")
    print(f"Cidade: {dados.get('localidade')}")
    print(f"Estado: {dados.get('uf')}")

cep_usuario = input("Digite o CEP: ")
consultar_cep(cep_usuario)

# Criando um programa que verifica a cotação de moedas em tempo real
converter_para_real = lambda valor, cotacao: valor * cotacao

def obter_cotacao(par_moedas):
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{par_moedas}"
        reposta = requests.get(url)
        dados = reposta.json()
        
        chave = par_moedas.replace("-", "")

        if chave in dados: 
            return dados[chave]
        else:
            return None
    except requests.exceptions.RequestException:
        print("Erro ao tentar acessar a API de cotação")
        return None

def moedas():
    try:
        print("\nConversor de Moedas")
        origem = input("""\nEscolha a moeda de origem:
(R) Real
(D) Dolar
(E) Euro
""").upper()

        valor_input = float(input("\nDigite o valor para converter: "))
        
        if origem == "R":
            destino = input("\nConverter para: \n(D) Dolar \n(E) Euro \n").upper()
            
            if destino == "D":
                dados = obter_cotacao("BRL-USD")
                if dados:
                    cotacao = float(dados["bid"])
                    maxima = float(dados["high"])
                    minima = float(dados["low"])
                    resultado = valor_input * cotacao
                    
                    print(f"""
Valor inicial: R$ {valor_input:.2f}
Cotação atual: {cotacao:.2f}
Valor final: USD {resultado:.2f}
Máxima: {maxima:.2f} | Mínima: {minima:.2f}
Data: {dados['create_date']}
""")

            elif destino == "E":
                dados = obter_cotacao("BRL-EUR")
                if dados:
                    cotacao = float(dados["bid"])
                    maxima = float(dados["high"])
                    minima = float(dados["low"])
                    resultado = valor_input * cotacao
                    
                    print(f"""
Valor inicial: R$ {valor_input:.2f}
Cotação atual: {cotacao:.2f}
Valor final: EUR {resultado:.2f}
Máxima: {maxima:.2f} | Mínima: {minima:.2f}
Data: {dados['create_date']}
""")

        elif origem == "D":
            destino = input("\n Converter para: \n(R) Real \n(E) Euro \n").upper()
            
            if destino == "R":
                dados = obter_cotacao("USD-BRL")
                if dados:
                    cotacao = float(dados["bid"])
                    maxima = float(dados["high"])
                    minima = float(dados["low"])
                    resultado = valor_input * cotacao
                    
                    print(f"""
Valor inicial: USD {valor_input:.2f}
Cotação atual: R$ {cotacao:.2f}
Valor final: R$ {resultado:.2f}
Máxima: R$ {maxima:.2f} | Mínima: R$ {minima:.2f}
Data: {dados['create_date']}
""")
            elif destino == "E":
                dados = obter_cotacao("USD-EUR")
                if dados:
                    cotacao = float(dados["bid"])
                    maxima = float(dados["high"])
                    minima = float(dados["low"])
                    resultado = valor_input * cotacao
                    
                    print(f"""
Valor inicial: USD {valor_input:.2f}
Cotação atual: EUR {cotacao:.2f}
Valor final: EUR {resultado:.2f}
Máxima: EUR {maxima:.2f} | Mínima: EUR {minima:.2f}
Data: {dados['create_date']}
""")

        elif origem == "E":
            destino = input("\n Converter para: \n(R) Real \n(D) Dolar \n").upper()
            
            if destino == "R":
                dados = obter_cotacao("EUR-BRL")
                if dados:
                    cotacao = float(dados["bid"])
                    maxima = float(dados["high"])
                    minima = float(dados["low"])
                    resultado = valor_input * cotacao
                    
                    print(f"""
Valor inicial: EUR {valor_input:.2f}
Cotação atual: R$ {cotacao:.2f}
Valor final: R$ {resultado:.2f}
Máxima: R$ {maxima:.2f} | Mínima: R$ {minima:.2f}
Data: {dados['create_date']}
""")
            elif destino == "D":
                dados = obter_cotacao("EUR-USD")
                if dados:
                    cotacao = float(dados["bid"])
                    maxima = float(dados["high"])
                    minima = float(dados["low"])
                    resultado = valor_input * cotacao
                    
                    print(f"""
Valor inicial: EUR {valor_input:.2f}
Cotação atual: USD {cotacao:.2f}
Valor final: USD {resultado:.2f}
Máxima: USD {maxima:.2f} | Mínima: USD {minima:.2f}
Data: {dados['create_date']}
""")

    except ValueError:
        print("Digite um número válido!")
    except Exception as erro:
        print("Erro inesperado!", erro)

moedas()

