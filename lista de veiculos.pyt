def cadastro(proprietario, modelo, chassi, ano_fabricacao, placa):
    """
    Cadastra um veículo na lista VEÍCULOS.

    Args:
        proprietario: Nome do proprietário do veículo.
        modelo: Modelo do veículo.
        chassi: Número do chassi do veículo.
        ano_fabricacao: Ano de fabricação do veículo.
        placa: Placa do veículo.
    """

    # Cria um dicionário com as informações do veículo.
    dicionario_veiculo = {
        "proprietario": proprietario,
        "modelo": modelo,
        "chassi": chassi,
        "ano_fabricacao": ano_fabricacao,
        "placa": placa
    }

    # Insere o dicionário na lista VEÍCULOS.
    VEICULOS.append(dicionario_veiculo)

# Exemplo de uso:

cadastro("João da Silva", "Gol", "1234567890123456", 2023, "ABC-1234")
