n = int(input("Digite uma quantidade de números para ser digitada(lida): "))

print("Informe um número: ")
anterior = int(input())

ordenado = True 

for i in range(n-1):
    print("Informe o número: ")
    atual = int(input())
    
    if anterior == atual:  #verifica se há números adjacentes iguais1
        ordenado = False
        break  # para o loop assim que encontrar números iguais
    
    anterior = atual  # atualiza o "anterior" para a próxima interação

if ordenado: 
    print("Foram lidos ",n," números e não há valores adjacentes iguais.")
else:
    print("Foram lidos ",n, " números e há pelo menos dois valores adjacentes iguais.")
