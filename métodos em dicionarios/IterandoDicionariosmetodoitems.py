ra = {"Liz": 229874, "Hugo": 215793, "Sofia": 199745}  
# Criamos um dicionário onde os nomes são as chaves e os números de registro são os valores.

for nome, numero in ra.items():  
    # Percorremos o dicionário pegando tanto a chave (nome) quanto o valor (número).

    print(nome, numero, sep=' - ')  
    # Exibimos o nome e o número separados por um espaço.

#O sep é um parâmetro da função print() que define o separador entre os valores impressos. 
# Por padrão, o separador é um espaço (' '), mas você pode mudá-lo para qualquer outro caractere.