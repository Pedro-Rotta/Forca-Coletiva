import random
import os
palavra_oculta = ''
letra_escolhida = ''
print(r'''_____________                                                                                  ____  
\  _________/                                                                    ______________|  |
 |  |       |                           ____________________________________    |--------------|  |   
 |  |_____  O                          / -      Digite 1 para jogar!     -  \    |||           |  |
 |  _____/ (||)                        | - Digite 2 para ver  as regras-  - |    |/|           |  |
 |  |   ___.||.   _______   ______   __\_-______Número de jogadores:3-____-_/   (/ /)          |  |
 |  |  /   _   \  \  \ __/ /  ___/  /   _   _/                                  ( / )          |  |  
 |  |  |  |_|  |   |  |    |  |__   |  |_|  |                                   / _ \          |  |
/___\  \_______/   /__\    \_____/  \_____/__\                                 / / \ \         |  |
  ______     ______    ______    _________  __________  _____  _____   ____   _\_\ / /         |  |
 /  ____\   /  __  \   \    /    \   ____/  \__    __/  \   /  \   /   \  /  /  _ \_/          |  |
/  /       /  /  \  \   |  |      |  |___      |  |      | |    \  \   / /  /  /_\ \           |  |
\  \_____  \  \__/  /   |  |__    |  |___      |  |      | |     \  \_/ /  /  /   \ \   _______|__|__
 \______/   \______/   /______\  /_______\    /____\    /___\     \____/  /___\   /__\ |____________|
Trabalho Bimestral de Ambientes de Programação - 1º Termo de BSI
Alunos: 
Luiz Carlos Lucas Júnior
Pedro Augusto Rotta e Silva
Ryan Correa Morais''')
op1 = int(input('Digite aqui:\n'))
os.system('cls')
while op1!=1:
    if op1==2:
        print(r'''    ____________________________________
 __/                                     \__
/  |===========  R E G R A S  ===========|  \
|  \_____________________________________/  |
|  |                                     |  |
|  |  ● 3 Jogadores / 3 Rodadas.         |  |
|  |                                     |  |
|  |  ● O jogador com maior quantidade   |  |
|  |    de pontos acumulados ao final    |  |
|  |    das 3 rodadas, ganha.            |  |
|  |                                     |  |
|  |  ● Até 3 temas sorteados por rodada.|  |
|  |    Um único tema por palavra.       |  |
|  |                                     |  |
|  |  ● 3 vidas por jogador. Cada erro   |  |
|  |    vale uma vida. Cada jogador      |  |
|  |    tem direito a um chute por       |  |
|  |	palavra, ao custo de todas as    |  |
|  |    suas vidas caso errado.          |  |
|  |                                     |  |
|  |  ● Acertar um caracter equivale à   |  |
|  |    um ponto, completar a palavra    |  |
|  |    vale o número de letras que      |  |
|  |    faltam ser descobertas, mais     |  |
|  |    5.                               |  |
\__|_____________________________________|__/

   Aperte enter para voltar a tela inicial                                              
''')
        enter = input()
    else:
        print("Opção Inválida. Aperte enter para voltar a tela inicial.")
        enter = input()
    os.system('cls')
    print(r'''_____________                                                                                  ____  
\  _________/                                                                    ______________|  |
 |  |       |                           ____________________________________    |--------------|  |   
 |  |_____  O                          / -      Digite 1 para jogar!     -  \    |||           |  |
 |  _____/ (||)                        | - Digite 2 para ver  as regras-  - |    |/|           |  |
 |  |   ___.||.   _______   ______   __\_-______Número de jogadores:3-____-_/   (/ /)          |  |
 |  |  /   _   \  \  \ __/ /  ___/  /   _   _/                                  ( / )          |  |  
 |  |  |  |_|  |   |  |    |  |__   |  |_|  |                                   / _ \          |  |
/___\  \_______/   /__\    \_____/  \_____/__\                                 / / \ \         |  |
  ______     ______    ______    _________  __________  _____  _____   ____   _\_\ / /         |  |
 /  ____\   /  __  \   \    /    \   ____/  \__    __/  \   /  \   /   \  /  /  _ \_/          |  |
/  /       /  /  \  \   |  |      |  |___      |  |      | |    \  \   / /  /  /_\ \           |  |
\  \_____  \  \__/  /   |  |__    |  |___      |  |      | |     \  \_/ /  /  /   \ \   _______|__|__
 \______/   \______/   /______\  /_______\    /____\    /___\     \____/  /___\   /__\ |____________|
Trabalho Bimestral de Ambientes de Programação - 1º Termo de BSI
Alunos: 
Luiz Carlos Lucas Júnior
Pedro Augusto Rotta e Silva
Ryan Correa Morais''')
    op1 = int(input('Digite aqui:\n'))
os.system('cls')
jogador1 = input('Digite o nome do primeiro jogador\n')
os.system('cls')
jogador2 = input('Digite o nome do segundo jogador\n')
os.system('cls')
jogador3 = input('Digite o nome do terceiro jogador\n')
os.system('cls')
jogador1 = jogador1[0].upper() + jogador1[1:]
jogador2 = jogador2[0].upper() + jogador2[1:]
jogador3 = jogador3[0].upper() + jogador3[1:]
pontos_j1 = 0
pontos_j2 = 0
pontos_j3 = 0
j = 0
tema2 = ''
tema3 = ''
nome_vida1 = ''
nome_vida2 = ''
achou = 0
letras_repetidas = ''
while j < 3:
    vida1 = 3
    vida2 = 3
    escolha_tema = 3
    if j == 0:
        print('Vez do %s escolher o tema e a palavra' % jogador1)
    if j == 1:
        print('Vez do %s escolher o tema e a palavra' % jogador2)
    if j == 2:
        print('Vez do %s escolher o tema e a palavra' % jogador3)

    vetor_strings = ["Filmes clássicos", "Cidades do mundo", "Bandas e artistas musicais",
                     "Palavras em diferentes idiomas", "Personagens de livros", "Alimentos e gastronomia", "Mitologia",
                     "Profissões", "Esportes e atletas", "Tecnologia e inovação", "Animais exóticos",
                     "Palavras relacionadas ao espaço", "Palavras da natureza", "Nomes de países", "Marcas famosas",
                     "Personagens de desenhos animados", "Instrumentos musicais", "Nomes de super-heróis",
                     "Estados do Brasil", "Nomes de frutas", "Nomes de planetas"]
    tema = random.choice(vetor_strings)
    tema1 = tema
    print(f'Tema sugerido: {tema}')

    escolha = input('Aceitar tema? <sim/nao>\n')
    os.system('cls')
    while escolha == 'nao' and escolha_tema >= 0:
        escolha_tema -= 1
        if escolha_tema > 0:
            cont = 0
            while(cont == 0 or tema == tema1 or tema == tema2 or tema == tema3):
                cont +=1
                vetor_strings = ["Filmes clássicos", "Cidades do mundo", "Bandas e artistas musicais",
                                 "Palavras em diferentes idiomas", "Personagens de livros", "Alimentos e gastronomia",
                                 "Mitologia", "Profissões", "Esportes e atletas", "Tecnologia e inovação",
                                 "Animais exóticos", "Palavras relacionadas ao espaço", "Palavras da natureza", "Nomes de países", "Marcas famosas",
                     "Personagens de desenhos animados", "Instrumentos musicais", "Nomes de super-heróis",
                     "Estados do Brasil", "Nomes de frutas", "Nomes de planetas"]
                tema = random.choice(vetor_strings)
            if escolha_tema == 2:
                tema2 = tema
            else:
                if escolha_tema == 1:
                    tema3 = tema
            print(f'Tema sugerido: {tema}')
            escolha = input('Aceitar tema? <sim/nao>\n')
            os.system('cls')
        else:
            print('Não é possível sortear mais temas.')
            print('Deseja utilizar qual dos temas sorteados?')
            print('1-%s\n2-%s\n3-%s' % (tema1, tema2, tema3))
            escolha = int(input('Digite sua escolha\n'))
    if int(escolha == 1):
        tema = tema1
    if int(escolha == 2):
        tema = tema2
    if int(escolha == 3):
        tema = tema3
    os.system('cls')
    print("Tema escolhido: %s"%tema)

    # escolha da palavra
    cont = 0
    palavra_escolhida= ""
    while cont == 0 or len(palavra_escolhida) < 5:
        if cont > 0:
            os.system('cls')
            print('A palavra precisa ter mais que 5 caracteres:')
        print('Digite a palavra dentro do tema(Digite com atenção):')
        palavra_escolhida = input('\033[0;30;40m')
        palavra_escolhida = palavra_escolhida.lower()
        print('\033[m')
        cont += 1
    os.system('cls')
    quantidade_caracter = len(palavra_escolhida)
    palavra_oculta = '_ ' * quantidade_caracter
    palavra_verificacao = ' '.join(palavra_escolhida) + ' '

    if j == 0:
        enter = input('Jogadores %s e %s digitem uma letra ou advinhem a palavra.\nDigite enter para continar.' % (jogador2, jogador3))
        nome_vida1 = jogador2
        nome_vida2 = jogador3
    elif j == 1:
        enter = input('Jogadores %s e %s digitem uma letra ou advinhem a palavra.\nDigite enter para continar.' % (jogador3, jogador1))
        nome_vida1 = jogador3
        nome_vida2 = jogador1
    elif j == 2:
        enter = input('Jogadores %s e %s digitem uma letra ou advinhem a palavra.\nDigite enter para continar.' % (jogador1, jogador2))
        nome_vida1 = jogador1
        nome_vida2 = jogador2
    # inicio da repetição até acertar ou errar a palavra
    os.system('cls')
    print('''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |                                              |#|| |                                              
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1, jogador2, pontos_j2,jogador3, pontos_j3, palavra_oculta))
    letras_repetidas = []
    print('Letras usadas:')
    print(letras_repetidas)
    while (vida1 > 0 or vida2 > 0) and palavra_oculta != palavra_verificacao:
        if vida1 > 0 and palavra_oculta != palavra_verificacao:
            cont = 0
            while cont == 0 or (not (len(letra_escolhida) == 1) and (len(letra_escolhida) < len(palavra_escolhida))) or (not (len(letra_escolhida) == 1) and (len(letra_escolhida) > len(palavra_escolhida))):
                if cont > 0:
                    os.system('cls')
                    print('Você não pode digitar uma palavra menor que a palavra escolhida.')
                    print('''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |                                              |#|| |                                              
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                    print('Letras usadas:')
                    print(letras_repetidas)
                letra_escolhida = input('Jogador %s, digite uma letra ou advinhe a palavra:\n' % (nome_vida1))
                letra_escolhida = letra_escolhida.lower()
                cont += 1
            os.system('cls')
            for i in range(quantidade_caracter):
                if letra_escolhida == palavra_escolhida[i]:
                    palavra_oculta = palavra_oculta[:i * 2] + palavra_escolhida[i] + palavra_oculta[i * 2 + 1:]
            if letra_escolhida == palavra_escolhida:
                f = 0
                for t in range(quantidade_caracter):
                    if letra_escolhida[t] == palavra_escolhida[t] and letra_escolhida[t] != palavra_oculta[f]:
                        if j == 0:
                            pontos_j2 += 1
                        elif j == 1:
                            pontos_j3 += 1
                        elif j == 2:
                            pontos_j1 += 1
                    f += 2
                palavra_oculta = palavra_verificacao
            repetida = 0
            for m in range(len(letras_repetidas)):
                if letra_escolhida == letras_repetidas[m]:
                    repetida += 1

            if letra_escolhida != palavra_escolhida:
                if repetida == 0:
                    if len(letra_escolhida) == 1:
                        for i in range(quantidade_caracter):
                            if letra_escolhida == palavra_escolhida[i]:
                                achou += 1
                                if j == 0:
                                    pontos_j2 += 1
                                elif j == 1:
                                    pontos_j3 += 1
                                elif j == 2:
                                    pontos_j1 += 1
                            else:
                                if i == len(palavra_escolhida) - 1 and achou == 0:
                                    vida1 -= 1
                    else:
                        vida1 = 0
                else:
                    vida1 -= 1
            if repetida == 0:
                if len(letra_escolhida) == 1:
                    letras_repetidas.append(letra_escolhida)
            if vida1 == 3 and vida2 == 3:
                os.system('cls')
                print('''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |                                              |#|| |                                              
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif (vida1 == 2 and vida2 == 3):
                os.system('cls')
                print('''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |                                              
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif (vida1 == 3 and vida2 == 2):
                os.system('cls')
                print('''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |                                              |#|| |   (;_;)                                      
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 2 and vida2 == 2:
                os.system('cls')
                print('''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |   (;_;)                                      
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 3 and vida2 == 1:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |                                              |#|| |   (;_;)                                      
| |                                              |#|| |   /| |\     ________________________________
| |                                              |#|| |  / |-| \   |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif (vida1 == 3 and vida2 == 0):
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                -GAME-                  
| |                                              |#|| |   (x_x)              -OVER-                  
| |                                              |#|| |  \/| |\/    ________________________________
| |                                              |#|| |    |-|     |-Placar-------------------------
| |                                              |#|| |  _/   \_   |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif (vida1 == 2 and vida2 == 1):
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |   (;_;)                                      
| |                                              |#|| |   /| |\     ________________________________
| |                                              |#|| |  / |-| \   |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif (vida1 == 2 and vida2 == 0):
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                -GAME-                  
| |   (;_;)                                      |#|| |   (X_X)              -OVER-                  
| |                                              |#|| |  \/| |\/    ________________________________
| |                                              |#|| |    |-|     |-Placar-------------------------
| |                                              |#|| |  _/   \_   |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif (vida1 == 1 and vida2 == 3):
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |                                              
| |   /| |\                                      |#|| |             ________________________________
| |  / |-| \                                     |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif (vida1 == 1 and vida2 == 2):
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |   (;_;)                                      
| |   /| |\                                      |#|| |             ________________________________
| |  / |-| \                                     |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 1 and vida2 == 1:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |   (;_;)                                      
| |   /| |\                                      |#|| |   /| |\     ________________________________
| |  / |-| \                                     |#|| |  / |-| \   |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 1 and vida2 == 0:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                -GAME-                  
| |   (;_;)                                      |#|| |   (X_X)              -OVER-                  
| |   /| |\                                      |#|| |  \/| |\/    ________________________________
| |  / |-| \                                     |#|| |    |-|     |-Placar-------------------------
| |                                              |#|| |  _/   \_   |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 0 and vida2 == 3:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                -GAME-                  |#|| |/    Y                                        
| |   (X_X)              -OVER-                  |#|| |                                              
| |  \/| |\/                                     |#|| |             ________________________________
| |    |-|                                       |#|| |            |-Placar-------------------------
| |  _/   \_                                     |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 0 and vida2 == 2:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                -GAME-                  |#|| |/    Y                                        
| |   (X_X)              -OVER-                  |#|| |   (;_;)                                      
| |  \/| |\/                                     |#|| |             ________________________________
| |    |-|                                       |#|| |            |-Placar-------------------------
| |  _/   \_                                     |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 0 and vida2 == 1:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                -GAME-                  |#|| |/    Y                                        
| |   (X_X)              -OVER-                  |#|| |   (;_;)                                      
| |  \/| |\/                                     |#|| |   /| |\     ________________________________
| |    |-|                                       |#|| |  / |-| \   |-Placar-------------------------
| |  _/   \_                                     |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            if (palavra_oculta == palavra_verificacao):
                if j == 0:
                    pontos_j2 += 5
                elif j == 1:
                    pontos_j3 += 5
                elif j == 2:
                    pontos_j1 += 5
        achou = 0

        ##############################################################################################################
        if vida2 > 0 and palavra_oculta != palavra_verificacao:
            cont = 0
            while cont == 0 or (not (len(letra_escolhida) == 1) and len(letra_escolhida) < len(palavra_escolhida)):
                if cont > 0:
                    os.system('cls')
                    print('Você não pode digitar uma palavra menor que a palavra escolhida.')
                    print('''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |                                              |#|| |                                              
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (
                    nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1, jogador2, pontos_j2, jogador3, pontos_j3,
                    palavra_oculta))
                    print('Letras usadas:')
                    print(letras_repetidas)
                letra_escolhida = input('Jogador %s, digite uma letra ou advinhe a palavra:\n' % (nome_vida2))
                letra_escolhida = letra_escolhida.lower()
                cont += 1
            os.system('cls')
            for i in range(quantidade_caracter):
                if letra_escolhida == palavra_escolhida[i]:
                    palavra_oculta = palavra_oculta[:i * 2] + palavra_escolhida[i] + palavra_oculta[i * 2 + 1:]
            if letra_escolhida == palavra_escolhida:
                f = 0
                for t in range(quantidade_caracter):
                    if letra_escolhida[t] == palavra_escolhida[t] and letra_escolhida[t] != palavra_oculta[f]:
                        if j == 0:
                            pontos_j3 += 1
                        elif j == 1:
                            pontos_j1 += 1
                        elif j == 2:
                            pontos_j2 += 1
                    f += 2
                palavra_oculta = palavra_verificacao
            repetida = 0
            for m in range(len(letras_repetidas)):
                if letra_escolhida == letras_repetidas[m]:
                    repetida += 1

            if letra_escolhida != palavra_escolhida:
                if repetida == 0:
                    if len(letra_escolhida) == 1:
                        for i in range(quantidade_caracter):
                            if letra_escolhida == palavra_escolhida[i]:
                                achou += 1
                                if j == 0:
                                    pontos_j3 += 1
                                elif j == 1:
                                    pontos_j1 += 1
                                elif j == 2:
                                    pontos_j2 += 1
                            elif i == len(palavra_escolhida) - 1 and achou == 0:
                                vida2 -= 1
                    else:
                        vida2 = 0
                else:
                    vida2 -= 1
            if repetida == 0:
                if len(letra_escolhida) == 1:
                    letras_repetidas.append(letra_escolhida)
            if vida1 == 3 and vida2 == 3:
                os.system('cls')
                print('''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |                                              |#|| |                                              
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1,jogador2, pontos_j2,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 2 and vida2 == 3:
                os.system('cls')
                print('''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |                                              
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 3 and vida2 == 2:
                os.system('cls')
                print('''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |                                              |#|| |   (;_;)                                      
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 2 and vida2 == 2:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |   (;_;)                                      
| |                                              |#|| |             ________________________________
| |                                              |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 3 and vida2 == 1:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |                                              |#|| |   (;_;)                                      
| |                                              |#|| |   /| |\     ________________________________
| |                                              |#|| |  / |-| \   |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 3 and vida2 == 0:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                -GAME-                  
| |                                              |#|| |   (X_X)              -OVER-                  
| |                                              |#|| |  \/| |\/    ________________________________
| |                                              |#|| |    |-|     |-Placar-------------------------
| |                                              |#|| |  _/   \_   |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 2 and vida2 == 1:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |   (;_;)                                      
| |                                              |#|| |   /| |\     ________________________________
| |                                              |#|| |  / |-| \   |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 2 and vida2 == 0:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                -GAME-                  
| |   (;_;)                                      |#|| |   (X_X)              -OVER-                  
| |                                              |#|| |  \/| |\/    ________________________________
| |                                              |#|| |    |-|     |-Placar-------------------------
| |                                              |#|| |  _/   \_   |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 1 and vida2 == 3:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |                                              
| |   /| |\                                      |#|| |             ________________________________
| |  / |-| \                                     |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 1 and vida2 == 2:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |   (;_;)                                      
| |   /| |\                                      |#|| |             ________________________________
| |  / |-| \                                     |#|| |            |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 1 and vida2 == 1:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                                        
| |   (;_;)                                      |#|| |   (;_;)                                      
| |   /| |\                                      |#|| |   /| |\     ________________________________
| |  / |-| \                                     |#|| |  / |-| \   |-Placar-------------------------
| |                                              |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1, jogador2, pontos_j2, jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 1 and vida2 == 0:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                                        |#|| |/    Y                -GAME-                  
| |   (;_;)                                      |#|| |   (X_X)              -OVER-                  
| |   /| |\                                      |#|| |  \/| |\/    ________________________________
| |  / |-| \                                     |#|| |    |-|     |-Placar-------------------------
| |        _                                     |#|| |  _/   \_   |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1, jogador2, pontos_j2, jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 0 and vida2 == 3:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                -GAME-                  |#|| |/    Y                                        
| |   (X_X)              -OVER-                  |#|| |                                              
| |  \/| |\/                                     |#|| |             ________________________________
| |    |-|                                       |#|| |            |-Placar-------------------------
| |  _/   \_                                     |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1, jogador2, pontos_j2, jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 0 and vida2 == 2:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                -GAME-                  |#|| |/    Y                                        
| |   (X_X)              -OVER-                  |#|| |   (;_;)                                      
| |  \/| |\/                                     |#|| |             ________________________________
| |    |-|                                       |#|| |            |-Placar-------------------------
| |  _/   \_                                     |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1, jogador2, pontos_j2, jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            elif vida1 == 0 and vida2 == 1:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                -GAME-                  |#|| |/    Y                                        
| |   (X_X)              -OVER-                  |#|| |   (;_;)                                      
| |  \/| |\/                                     |#|| |   /| |\     ________________________________
| |    |-|                                       |#|| |  / |-| \   |-Placar-------------------------
| |  _/   \_                                     |#|| |            |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Palavra - %s\t''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3, palavra_oculta))
                print('Letras usadas:')
                print(letras_repetidas)
            if palavra_oculta == palavra_verificacao:
                if j == 0:
                    pontos_j3 += 5
                elif j == 1:
                    pontos_j1 += 5
                elif j == 2:
                    pontos_j2 += 5

            if vida1 == 0 and vida2 == 0:
                os.system('cls')
                print(r'''            %s- %d Vidas                                        %s- %d Vidas
 ___________                                         ___________ 
|=|=X===x==|/                                    |#||=|=X===x==|/ 
|=|//   ¿                                        |#||=|//   ¿    
| |/    Y                -GAME-                  |#|| |/    Y                -GAME-                  
| |   (X_X)              -OVER-                  |#|| |   (X_X)              -OVER-                  
| |  \/| |\/                                     |#|| |  \/| |\/    ________________________________
| |    |-|                                       |#|| |    |-|     |-Placar-------------------------
| |  _/   \_                                     |#|| |  _/   \_   |#|%s - %d pts                  
|_|_                                             |#||_|_           |#|%s - %d pts                  
____|                                            |#|____|          |#|%s - %d pts                  
####################################################################################################
Nenhum dos jogadores encontrou a palavra...''' % (nome_vida1, vida1, nome_vida2, vida2, jogador1, pontos_j1 ,jogador2, pontos_j2 ,jogador3, pontos_j3))
                prosseguir = (input('Tecle qualquer tecla para continuar\n'))
                os.system('cls')
        achou = 0
    os.system('cls')
    j += 1
maior = 0
if pontos_j1 > maior:
    maior = pontos_j1
if pontos_j2 > maior:
    maior = pontos_j2
if pontos_j3 > maior:
    maior = pontos_j3
os.system('cls')
if pontos_j1 == maior and (pontos_j2 < maior and pontos_j3 < maior):
    print(r'''        _________
   _.-'' _______ ''-._                   ___                           ___ 
  _\_.-''  __   ''-._/_                -' _ '-                       -' _ '- 
 / \      /  | __    / \             /' -' '- '\                   /' -' '- '\        
/ / \.   /_| ||_|  ./ \ \           / /'     '\ \                 / /'     '\ \
\ \_  \.   | |   ./  _/ /          ' '    |    ' '               ' '    |    ' '
 \_ ''--\ _| |_ /--'' _/          / /   --+--   \ \             / /   --+--   \ \
   ''--\ ||___|| /--''            | |     |     | |             | |     |     | |
        \ |   | /                 | |     |     | |             | |     |     | |
       / |     | \                | |           | |             | |           | |
       \/_______\/                | |-----------| |             | |-----------| |
        %s                           %s                            %s
    /---------------\             | |-----------| |             | |-----------| |
   /_________________\           _|_|___________|_|_           _|_|___________|_|_
 _|___________________|_       _|___________________|_       _|___________________|_
|_______________________|     |_______________________|     |_______________________|''' % (jogador1, jogador2, jogador3))
    print('O vencedor foi %s! parabéns!' % jogador1)
elif pontos_j2 == maior and (pontos_j1 < maior and pontos_j3 < maior):
    print(r'''                                      _________
           ___                   _.-'' _______ ''-._                   ___ 
         -' _ '-                _\_.-''  __   ''-._/_                -' _ '- 
       /' -' '- '\             / \      /  | _     / \             /' -' '- '\ 
      / /'     '\ \           / / \.   /_| ||_|  ./ \ \           / /'     '\ \
     ' '    |    ' '          \ \_  \.   | |   ./  _/ /          ' '    |    ' '
    / /   --+--   \ \          \_ ''--\ _| |_ /--'' _/          / /   --+--   \ \
    | |     |     | |            ''--\ ||___|| /--''            | |     |     | |
    | |     |     | |                 \ |   | /                 | |     |     | |
    | |           | |                / |     | \                | |           | |
    | |-----------| |                \/_______\/                | |-----------| |
      %s                              %s                          %s
    | |-----------| |             /---------------\             | |-----------| |
   _|_|___________|_|_           /_________________\           _|_|___________|_|_
 _|___________________|_       _|___________________|_       _|___________________|_
|_______________________|     |_______________________|     |_______________________|''' % (jogador1, jogador2, jogador3))
    print('O vencedor foi %s! parabéns!' % jogador2)
elif pontos_j3 == maior and pontos_j1 < maior and pontos_j2 < maior:
    print(r'''                                                                    _________
           ___                           ___                   _.-'' _______ ''-._
         -' _ '-                       -' _ '-                _\_.-''  __   ''-._/
       /' -' '- '\                   /' -' '- '\             / \      /  | _     / \
      / /'     '\ \                 / /'     '\ \           / / \.   /_| ||_|  ./ \ \
     ' '    |    ' '               ' '    |    ' '          \ \_  \.   | |   ./  _/ /
    / /   --+--   \ \             / /   --+--   \ \          \_ ''--\ _| |_ /--'' _/
    | |     |     | |             | |     |     | |            ''--\ ||___|| /--''
    | |     |     | |             | |     |     | |                 \ |   | /   
    | |           | |             | |           | |                / |     | \
    | |-----------| |             | |-----------| |                \/_______\/ 
      %s                             %s                             %s
    | |-----------| |             | |-----------| |             /---------------\
   _|_|___________|_|_           _|_|___________|_|_           /_________________\
 _|___________________|_       _|___________________|_       _|___________________|_
|_______________________|     |_______________________|     |_______________________|
''' % (jogador1, jogador2, jogador3))
    print('O vencedor foi %s! parabéns!' % jogador3)
elif pontos_j1 == pontos_j2 and pontos_j3 < maior:
    print(r'''        _________                     _________
   _.-'' _______ ''-._           _.-'' _______ ''-._                   ___ 
  _\_.-''       ''-._/_         _\_.-''       ''-._/_                -' _ '- 
 / \                 / \       / \                 / \             /' -' '- '\ 
/ / \.             ./ \ \     / / \.             ./ \ \           / /'     '\ \
\ \_  \.         ./  _/ /     \ \_  \.         ./  _/ /          ' '    |    ' '
 \_ ''--\ _   _ /--'' _/       \_ ''--\       /--'' _/          / /   --+--   \ \
   ''--\ ||   || /--''           ''--\ |     | /--''            | |     |     | |
        \ |   | /                     \ |   | /                 | |     |     | |
       / |     | \                   / |     | \                | |           | |
       \/_______\/                   \/_______\/                | |-----------| |
       %s                             %s                          %s
    /---------------\             /---------------\             | |-----------| |
   /_________________\           /_________________\           _|_|___________|_|_
 _|___________________|_       _|___________________|_       _|___________________|_
|_______________________|     |_______________________|     |_______________________|''' % (jogador1, jogador2, jogador3))
    print('Os vencedores foram %s e %s! parabéns!' % (jogador1, jogador2))
elif pontos_j1 == pontos_j3 and pontos_j2 < maior:
    print(r'''
        _________ 													_________
   _.-'' _______ ''-._                   ___                   _.-'' _______ ''-._
  _\_.-''       ''-._/_                -' _ '-                _\_.-''       ''-._/_
 / \                 / \             /' -' '- '\             / \                 / \ 
/ / \.             ./ \ \           / /'     '\ \           / / \.             ./ \ \
\ \_  \.         ./  _/ /          ' '    |    ' '          \ \_  \.         ./  _/ /
 \_ ''--\       /--'' _/          / /   --+--   \ \          \_ ''--\       /--'' _/
   ''--\ |     | /--''            | |     |     | |            ''--\ |     | /--''    
        \ |   | /                 | |     |     | |                 \ |   | /   
       / |     | \                | |           | |                / |     | \   
       \/_______\/                | |-----------| |                \/_______\/               
        %s                           %s                             %s
    /---------------\             | |-----------| |             /---------------\ 
   /_________________\           _|_|___________|_|_           /_________________\
 _|___________________|_       _|___________________|_       _|___________________|_
|_______________________|     |_______________________|     |_______________________|''' % (jogador1, jogador2, jogador3))
    print('Os vencedores foram %s e %s! parabéns!' % (jogador1, jogador3))
elif pontos_j2 == pontos_j3 and pontos_j1 < maior:
    print(r'''                                      _________                     _________
           ___                   _.-'' _______ ''-._           _.-'' _______ ''-._
         -' _ '-                _\_.-''       ''-._/_         _\_.-''       ''-._/_
       /' -' '- '\             / \                 / \       / \                 / \
      / /'     '\ \           / / \.             ./ \ \     / / \.             ./ \ \
     ' '    |    ' '          \ \_  \.         ./  _/ /     \ \_  \.         ./  _/ /
    / /   --+--   \ \          \_ ''--\       /--'' _/       \_ ''--\       /--'' _/
    | |     |     | |            ''--\ |     | /--''           ''--\ |     | /--''
    | |     |     | |                 \ |   | /                     \ |   | /   
    | |           | |                / |     | \                   / |     | \
    | |-----------| |                \/_______\/                   \/_______\/ 
      %s                              %s                            %s
    | |-----------| |             /---------------\             /---------------\
   _|_|___________|_|_           /_________________\           /_________________\
 _|___________________|_       _|___________________|_       _|___________________|_
|_______________________|     |_______________________|     |_______________________|''' % (jogador1, jogador2, jogador3))
    print('Os vencedores foram %s e %s! parabéns!' % (jogador2, jogador3))
elif pontos_j1 == pontos_j2 and pontos_j2 == pontos_j3:
    print(r'''           ___                           ___                           ___ 
         -' _ '-                       -' _ '-                       -' _ '- 
       /' -' '- '\                   /' -' '- '\                   /' -' '- '\        
      / /'     '\ \                 / /'     '\ \                 / /'     '\ \
     ' '    |    ' '               ' '    |    ' '               ' '    |    ' '
    / /   --+--   \ \             / /   --+--   \ \             / /   --+--   \ \
    | |     |     | |             | |     |     | |             | |     |     | |
    | |     |     | |             | |     |     | |             | |     |     | |
    | |           | |             | |           | |             | |           | |
    | |-----------| |             | |-----------| |             | |-----------| |
       %s                            %s                            %s
    | |-----------| |             | |-----------| |             | |-----------| |
   _|_|___________|_|_           _|_|___________|_|_           _|_|___________|_|_
 _|___________________|_       _|___________________|_       _|___________________|_
|_______________________|     |_______________________|     |_______________________|''' % (jogador1, jogador2, jogador3))
    print('Opa! Parece que os três jogadores empataram!!')
print('Jogador1: %s\nJogador2: %s\nJogador3: %s\n' % (jogador1, jogador2, jogador3))
print('''####################################################################################################
--------------------------------------------PLACAR FINAL--------------------------------------------
####################################################################################################
Jogador 1 - %s - %d pts
Jogador 2 - %s - %d pts
Jogador 3 - %s - %d pts''' % (jogador1, pontos_j1, jogador2, pontos_j2, jogador3, pontos_j3))
enter = input()
os.system('cls')
print(r'''  ______       ____     ___      ___ _________    ______
 /  ____\     /  _ \    \  \    /  / \  _____/   /      \
/  /  ____   /  /_\ \    |  \  /  |   | |__      |.    .|
\  \__/  /  /  /   \ \   | | \/ | |   | |____    '|    |'
 \______/  /___\   /__\ /__\\__//__\ /_______\    |.  .|
  ______   _____   ____  _________  _________     '|  |'
 /  __  \  \   /   \  /  \   ____/  \   ___  \     |__|
/  /  \  \  \  \   / /    | |___     | |___/ /      __
\  \__/  /   \  \_/ /     | |____    | |   \ \     /  \
 \______/     \____/     /_______\  /___\  /__\    \__/

 Obrigado por jogar!!! ''')