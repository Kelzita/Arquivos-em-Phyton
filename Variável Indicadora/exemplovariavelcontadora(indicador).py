# Solicita ao usuário a quantidade de números a serem analisados
n = int(input("Digite uma quantidade de números para ser analisada: "))

print("Informe o número: ")
# Lê o primeiro número e o armazena na variável 'anterior'
anterior = int(input())

# Variável que indica se a sequência está ordenada
ordenado = True  

# Loop para ler os próximos números e verificar a ordem
for i in range(n - 1):
    print("Informe o número: ")
    atual = int(input())  # Lê o próximo número
    
    # Se o número atual for menor que o anterior, a sequência não está ordenada
    if atual < anterior:
        ordenado = False
        break  # Interrompe o loop imediatamente
    
    # Atualiza o valor de 'anterior' para a próxima comparação
    anterior = atual

# Verifica se a sequência está ordenada e exibe a mensagem correspondente
if ordenado:
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")
