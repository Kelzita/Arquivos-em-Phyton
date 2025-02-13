def letra_mais_comum(texto):
    frequencia = {}  # Dicionário para contar as letras

    for letra in texto:
        if letra.isalpha():  # Só conta as letras
            frequencia[letra] = frequencia.get(letra, 0) + 1  # Conta as ocorrências

    # Retorna a letra com maior contagem
    return max(frequencia, key = frequencia.get)

# O usuário digita a palavra
texto = input("Digite uma palavra: ")

# Exibe a letra mais comum
print("A letra mais comum é:", letra_mais_comum(texto))
