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
VEICULOS = []
cadastro(VEICULOS)
