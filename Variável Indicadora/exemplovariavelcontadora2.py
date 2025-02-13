n = int(input("Digite uma quantidade de números a ser analisada: "))
print("Informe o número:")
anterior = int(input()) 

i = 1 # leu o número 
ordenado = 0 #ordenado é a variavel contadora

while(i < n) and (ordenado == 0):
    print("Informe o número")
    atual = int(input())
    i= i + 1 #leu mais um número
    if ( atual <= anterior ):
        ordenado = ordenado + 1
    anterior = atual

if(ordenado == 0):
    print("Sequência está ordenada.")

else: 
    print("Sequência não está ordenada")
              