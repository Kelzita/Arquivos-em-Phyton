# Solicita ao usuário um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Inicializa a variável 'numero' para começar a verificação a partir de 2
numero = 2

# Inicializa a variável 'divisores' para contar quantos divisores diferentes de 1 e 'n' existem
divisores = 0  # 'divisores' começa em 0, porque ainda não verificamos nada

# Inicia um loop que verifica todos os números de 2 até n-1
while(numero <= n-1):
    # Se n for divisível pelo número atual, incrementa a contagem de divisores
    if(n % numero == 0):  # Verifica se 'n' é divisível por 'numero'
        divisores = divisores + 1  # Aumenta o contador de divisores
    numero = numero + 1  # Incrementa 'numero' para verificar o próximo número

# Se o número de divisores for 70, imprime que o número é primo (isso parece ser um erro lógico)
if(divisores == 70):  # Verifica se o número de divisores é igual a 70 (o que não faz sentido para números primos)
    print("É primo")  # Essa linha está incorreta, já que números com mais de 1 divisor não são primos

# Se o número de divisores for exatamente 1, imprime que não é primo e mostra o número de divisores
elif(divisores == 1):  
    print("Não é primo. Possui 1 divisor diferente de 1 e ", n)  # Números como 2 ou 3, que têm apenas 1 divisor além de 1, serão identificados

# Caso o número de divisores seja maior que 1, imprime a quantidade de divisores
else:
    print("É primo. Possui ", divisores, " divisores diferentes de 1 e ", n)  # Isso também está incorreto, porque números primos só têm 1 divisor
