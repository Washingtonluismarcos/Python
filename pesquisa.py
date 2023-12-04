import pickle

def cadastro(veiculos):
    novo_veiculo = {}
    novo_veiculo['proprietario'] = input("Digite o nome do proprietário: ")
    novo_veiculo['modelo'] = input("Digite o modelo do veículo: ")
    novo_veiculo['chassi'] = input("Digite o número do chassi: ")
    novo_veiculo['ano_fabricacao'] = input("Digite o ano de fabricação: ")
    novo_veiculo['placa'] = input("Digite a placa do veículo: ")
    veiculos.append(novo_veiculo)

def excluir_veiculo(veiculos):
    if not veiculos:
        print("Não há veículos para excluir.")
        return

    print("\nLista de Veículos:")
    for i, veiculo in enumerate(veiculos, 1):
        print(f"{i}. {veiculo}")

    try:
        indice = int(input("Digite o número do veículo a ser excluído: ")) - 1
        if 0 <= indice < len(veiculos):
            veiculo_excluido = veiculos.pop(indice)
            print(f"Veículo excluído: {veiculo_excluido}")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def pesquisar_veiculos(veiculos):
    termo_pesquisa = input("Digite parte do nome do proprietário para pesquisar: ").lower()
    resultados = [veiculo for veiculo in veiculos if termo_pesquisa in veiculo['proprietario'].lower()]

    if resultados:
        print("\nResultados da Pesquisa:")
        for i, veiculo in enumerate(resultados, 1):
            print(f"{i}. {veiculo}")
    else:
        print("Nenhum resultado encontrado.")

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
        print("3. Excluir veículo")
        print("4. Pesquisar veículos por proprietário")
        print("5. Sair")

        escolha = input("Escolha a opção (1/2/3/4/5): ")

        if escolha == '1':
            cadastro(VEICULOS)
            salvar_veiculos(VEICULOS, ARQUIVO_DADOS)
        elif escolha == '2':
            exibir_veiculos(VEICULOS)
        elif escolha == '3':
            excluir_veiculo(VEICULOS)
            salvar_veiculos(VEICULOS, ARQUIVO_DADOS)
        elif escolha == '4':
            pesquisar_veiculos(VEICULOS)
        elif escolha == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
