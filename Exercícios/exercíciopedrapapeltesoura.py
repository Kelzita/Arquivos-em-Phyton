def jogar():
    while True:
        print("Jogador 1, escolha:")
        print("0 - Pedra")
        print("1 - Papel")
        print("2 - Tesoura")
        
        escolha_jogador1 = int(input("Jogador 1, digite sua escolha (0, 1 ou 2): "))
        
        if escolha_jogador1 == 0:
            escolha1 = "Pedra"
        elif escolha_jogador1 == 1:
            escolha1 = "Papel"
        elif escolha_jogador1 == 2:
            escolha1 = "Tesoura"
        else:
            print("Opção inválida! Tente novamente.")
            continue
        
        print("\nJogador 2, escolha:")
        print("0 - Pedra")
        print("1 - Papel")
        print("2 - Tesoura")
        
        escolha_jogador2 = int(input("Jogador 2, digite sua escolha (0, 1 ou 2): "))
        
        if escolha_jogador2 == 0:
            escolha2 = "Pedra"
        elif escolha_jogador2 == 1:
            escolha2 = "Papel"
        elif escolha_jogador2 == 2:
            escolha2 = "Tesoura"
        else:
            print("Opção inválida! Tente novamente.")
            continue
        
        print("\nJogador 1 escolheu:",escolha1)
        print("Jogador 2 escolheu:",escolha2)

        if escolha1 == escolha2:
            print("Empate!")
        elif (escolha1 == "Pedra" and escolha2 == "Tesoura") or \
             (escolha1 == "Papel" and escolha2 == "Pedra") or \
             (escolha1 == "Tesoura" and escolha2 == "Papel"):
            print("Jogador 1 ganhou!")
        else:
            print("Jogador 2 ganhou!")
        
        jogar_novamente = input("\nVamos jogar novamente? (Sim/Não): ")
        if jogar_novamente != "sim":
            print("Jogo encerrado. Até logo!")
            break

jogar()
[]