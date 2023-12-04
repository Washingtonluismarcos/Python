def contar_avaliacoes(resp):
    count_otimo = resp.count('ótimo')
    count_bom = resp.count('bom')
    return count_otimo, count_bom

# Exemplo de uso:
Resp = []

while True:
    resposta = input("Digite a avaliação (ótimo, bom, regular, ruim, péssimo), ou 'sair' para encerrar: ").lower()
    
    if resposta == 'sair':
        break
    
    if resposta in ['ótimo', 'bom', 'regular', 'ruim', 'péssimo']:
        Resp.append(resposta)
    else:
        print("Avaliação inválida. Por favor, digite uma opção válida.")

count_otimo, count_bom = contar_avaliacoes(Resp)

print(f"Número de respostas 'ótimo': {count_otimo}")
print(f"Número de respostas 'bom': {count_bom}")
