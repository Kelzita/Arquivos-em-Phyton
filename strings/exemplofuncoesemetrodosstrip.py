# Define a variável 'b' contendo uma string com quebras de linha antes e depois do texto
b = "\nFizeram os exercícios?\n"

# Imprime a variável 'b', incluindo as quebras de linha
print(b)

# O trecho abaixo apenas exibe a string 'b', mas não a imprime (não tem efeito prático)
'\nFizeram os exercícios?\n'

# Usa o método .strip() para remover as quebras de linha no início e no fim da string
# Depois, imprime a string sem espaços extras, seguida de "oi"
print(b.strip(), "oi")  
