#Sheldon Cooper's rock, paper, scissor, lizard, spock game
from random import randint
from time import sleep
import emoji
print('Rock - Paper - Scissors - Lizard - Spock')
print(emoji.emojize('Options:\n1: Rock :punch:\n2: Paper :hand:\n3: Scissors :v:\n4: Lizard :pinching_hand:\n5: Spock :vulcan_salute:\n6: Rules :books:\n0: Exit :door:', use_aliases=True))
plays = ('ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK')
rules = """Rules:

Scissors cuts paper
paper covers rock
rock crushes lizard
lizard poisons Spock
Spock smashes scissors
scissors decapitates lizard
lizard eats paper
paper disproves Spock
Spock vaporizes rock
and, as it always has, rock crushes scissors."""
while True:
    print('--'*10)
    player = int(input('Insert your play: '))  #jogador insere o comando desejado
    if player == 0:  #ao digitar 0, o jogador sai do jogo
        print('==' * 22)
        print(emoji.emojize('See you next time. Live long and prosper! :vulcan_salute:', use_aliases=True))
        print('==' * 22)
        break
    elif player == 6:  #digitando 6, o jogador pede as regras do jogo
        print('==' * 10)
        print(rules)
    elif 5 >= player >= 1:  #ao inserir número válido, o jogador dá início ao jogo
        cpu = randint(1, 5)
        print('ROCK!')
        sleep(0.25)
        print('PAPER!')
        sleep(0.25)
        print('SCISSORS!')
        sleep(0.25)
        print('LIZARD!')
        sleep(0.25)
        print('SPOCK!')
        print(f'The computer chose {plays[cpu - 1]} and you chose {plays[player - 1]}')
        #condições de vitória do jogador
        if player == 1 and (cpu == 3 or cpu == 4):
            print('YOU WON!')
        elif player == 2 and (cpu == 1 or cpu == 5):
            print('YOU WON!')
        elif player == 3 and (cpu == 2 or cpu == 4):
            print('YOU WON!')
        elif player == 4 and (cpu == 5 or cpu == 2):
            print('YOU WON')
        elif player == 5 and (cpu == 3 or cpu == 1):
            print('YOU WON')
        #condições para vitória do computador
        elif cpu == 1 and (player == 3 or player == 4):
            print('YOU LOST')
        elif cpu == 2 and (player == 1 or player == 5):
            print('YOU LOST')
        elif cpu == 3 and (player == 2 or player == 4):
            print('YOU LOST')
        elif cpu == 4 and (player == 5 or player == 2):
            print('YOU LOST')
        elif cpu == 5 and (player == 3 or player == 1):
            print('YOU LOST')
        #empate
        elif player == cpu:
            print('DRAW')
    else:
        print('Invalid move. Try a number from 1 to 5. Insert 6 to see the rules.')
