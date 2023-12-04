import pickle

def cadastro(veiculos):
    novo_veiculo = {}
    novo_veiculo['proprietario'] = input("Digite o nome do proprietário: ")
    novo_veiculo['modelo'] = input("Digite o modelo do veículo: ")
    novo_veiculo['chassi'] = input("Digite o número do chassi: ")
    novo_veiculo['ano_fabricacao'] = input("Digite o ano de fabricação: ")
    novo_veiculo['placa'] = input("Digite a placa do veículo: ")
    veiculos.append(novo_veiculo)

def salvar_veiculos(veiculos, arquivo):
    with open(arquivo, 'wb') as f:
        pickle.dump(veiculos, f)

def carregar_veiculos(arquivo):
    try:
        with open(arquivo, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def exibir_veiculos(veiculos):
    print("\nLista de Veículos:")
    for veiculo in veiculos:
        print(veiculo)

def main():
    ARQUIVO_DADOS = 'dados_veiculos.pkl'
    
    # Carregar dados existentes
    VEICULOS = carregar_veiculos(ARQUIVO_DADOS)

    while True:
        print("\nOpções:")
        print("1. Cadastrar novo veículo")
        print("2. Exibir lista de veículos")
        print("3. Sair")

        escolha = input("Escolha a opção: ")

        if escolha == '1':
            cadastro(VEICULOS)
            salvar_veiculos(VEICULOS, ARQUIVO_DADOS)
        elif escolha == '2':
            exibir_veiculos(VEICULOS)
        elif escolha == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
