# Solicita um número inteiro positivo ao usuário e armazena em 'n'
n = int(input("Digite um número inteiro positivo: "))

# Inicializa a variável 'numero' com 2 (primeiro número a testar como divisor)
numero = 2

# Assume inicialmente que o número é primo
primo = True  # Variável booleana que será usada como um indicador

# Loop para verificar se 'n' é divisível por algum número de 2 até n-1
while (numero <= n - 1) and (primo):  
    # Se 'n' for divisível por 'numero', então ele não é primo
    if (n % numero == 0):  
        primo = False  # Define 'primo' como False, pois encontrou um divisor
    numero = numero + 1  # Incrementa 'numero' para testar o próximo divisor

# Após o loop, verifica o valor de 'primo'
if (primo):  
    print("É primo")  # Se 'primo' ainda for True, 'n' é primo
else:  
    print("Não é primo")  # Se 'primo' for False, 'n' não é primo
