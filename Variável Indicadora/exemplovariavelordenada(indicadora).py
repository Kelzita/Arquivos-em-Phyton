# Solicita ao usuário a quantidade de números que serão analisados
n = int(input("Digite uma quantidade de números para ser analisada: "))

# Exibe uma mensagem para o usuário informar o primeiro número
print("Informe o número: ")

# Lê o primeiro número e armazena na variável 'anterior'
anterior = int(input())

# Inicializa o contador de números lidos
i = 1  # Já lemos um número

# Variável indicadora que assume que a sequência está ordenada
ordenado = True  

# Inicia um loop para verificar os próximos números inseridos
while (i < n) and (ordenado):  # Continua enquanto não atingimos 'n' e a sequência estiver ordenada
    print("Informe o número")  # Solicita o próximo número ao usuário
    atual = int(input())  # Lê o próximo número informado

    i = i + 1  # Incrementa o contador de números lidos

    # Se o número atual for menor que o anterior, a sequência não está ordenada
    if (atual < anterior):
        ordenado = False  # Define 'ordenado' como False, pois a sequência foi quebrada

    # Atualiza 'anterior' para comparar com o próximo número na próxima iteração
    anterior = atual  

# Após sair do loop, verifica se a sequência permaneceu ordenada
if (ordenado):  
    print("Sequência ordenada.")  # Se 'ordenado' for True, a sequência estava em ordem crescente
else:  
    print("Sequência não ordenada.")  # Se 'ordenado' for False, a sequência não era crescente
