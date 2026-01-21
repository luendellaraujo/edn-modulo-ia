import csv
import json

# Criando um programa que lê um arquivo CSV
def analisar_csv():
    nome_arquivo = input("Digite o nome do arquivo CSV para análise: ")

    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            
            tempos = []
            for linha in leitor:
                if "tempo_execucao" in linha:
                    tempos.append(float(linha["tempo_execucao"]))

            if not tempos:
                print("\nO arquivo está vazio ou a coluna não foi encontrada!")
                return

            media = sum(tempos) / len(tempos)
            maximo = max(tempos)

            print("\nResultados da Análise ")
            print(f"Média de tempo: {media:.2f}")
            print(f"Tempo máximo: {maximo:.2f}")

    except FileNotFoundError:
        print("\nErro: Arquivo não encontrado!")
    except ValueError:
        print("\nErro: A coluna tempo_execucao contém valores inválidos!")
    except Exception as erro:
        print("\nErro inesperado na leitura!", erro)

analisar_csv()


# Criando um programa que cria um arquivo com dados em formato tabular 
def criar_arquivo():
   
    dados = [
        ["Nome", "Idade", "Cidade"],
        ["Lucas", 25, "São Paulo"],
        ["Mariana", 30, "Curitiba"],
        ["Pedro", 22, "Rio de Janeiro"]
    ]

    nome_arquivo = input("\nEscolha o nome do arquivo para salvar: ")

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for linha in dados:
                
                texto = f"{linha[0]}\t{linha[1]}\t{linha[2]}\n"
                arquivo.write(texto)
        
        print(f"\nArquivo '{nome_arquivo}' salvo com sucesso!")

    except Exception as erro:
        print("\nFalha ao salvar o arquivo!", erro)

criar_arquivo()


# Criando um programa que leia um arquivo informado pelo usuário
def ler_arquivo():
    nome_arquivo = input("\nDigite o nome do arquivo para ler: ")

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print("\nConteúdo do arquivo ")
            for linha in arquivo:
                print(linha.strip())
    
    except FileNotFoundError:
        print("\nErro: Arquivo não encontrado!")
    except Exception as erro:
        print("\nErro ao tentar ler o arquivo!", erro)

ler_arquivo()


# Criando um programa que leia e escreva arquivos no formato JSON
def gerenciar_dados_json():

    print("\nCriar arquivo em formato JSON")
    print("Criando...")

    pessoa = {
        "nome": "Fernanda",
        "idade": 28,
        "cidade": "São Bernardo do Campo"
    }
    
    nome_arquivo = "dados_usuario.json"

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(pessoa, arquivo, indent=4)
        print("Dados salvos no arquivo JSON.")
    except Exception as erro:
        print("Falha ao salvar o arquivo JSON!", erro)
        return 

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

            print("\nDados do arquivo ")
            print(f"Nome: {dados.get('nome')}")
            print(f"Idade: {dados.get('idade')}")
            print(f"Cidade: {dados.get('cidade')}")

    except FileNotFoundError:
        print("\nO arquivo JSON não existe!")
    except Exception as erro:
        print("\nErro inesperado!", erro)


gerenciar_dados_json()