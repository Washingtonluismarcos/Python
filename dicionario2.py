def cadastro(veiculos):
    novo_veiculo = {}  # Criando um novo dicionário para armazenar as informações do veículo

    # Solicitando informações ao usuário
    novo_veiculo['proprietario'] = input("Digite o nome do proprietário: ")
    novo_veiculo['modelo'] = input("Digite o modelo do veículo: ")
    novo_veiculo['chassi'] = input("Digite o número do chassi: ")
    novo_veiculo['ano_fabricacao'] = input("Digite o ano de fabricação: ")
    novo_veiculo['placa'] = input("Digite a placa do veículo: ")

    # Inserindo o novo veículo na lista
    veiculos.append(novo_veiculo)

# Exemplo de uso:
# Suponha que você já tenha uma lista de veículos chamada VEICULOS
def main():
    VEICULOS = []


 # Cadastrar veículos
    num_veiculos = int(input("Quantos veículos deseja cadastrar? "))
    for _ in range(num_veiculos):
        cadastro(VEICULOS)

    # Exibir lista de veículos
    print("\nLista de Veículos:")
    for veiculo in VEICULOS:
        print(veiculo)

if __name__ == "__main__":
    main()
