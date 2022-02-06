import random
from src.obj.itens import *

def Bau(tipo, player):
    if tipo == 1:
        n = random.randint(1,7)
        if n == 1:
            print("Você encontrou uma poção media!\n")
            player.PegarItem(pocaoMedia)
        elif n == 2:
            print("Você encontrou uma poção pequena!\n")
            player.PegarItem(pocaoPequena)
        elif n == 3:
            print("Você encontrou uma poção grande!\n")
            player.PegarItem(pocaoGrande)
        elif n == 4:
            print("Você encontrou um elixir medio!\n")
            player.PegarItem(elixirMedio)
        elif n == 5:
            print("Você encontrou um elixir grande!\n")
            player.PegarItem(elixirGrande)
        elif n == 6:
            print("Você encontrou uma pocao de adrenalina!\n")
            player.PegarItem(pocaoDeAdrenalina)
        elif n == 7:
            print("Você encontrou um elixir do mago!\n")
            player.PegarItem(elixirDoMago)
    elif tipo == 2:
        n = random.randint(1,4)
        if n == 1:
            print("Você encontrou uma espada nova! +Ataque\n")
            player.ataque += 2
        elif n == 2:
            print("Você encontrou uma armadura lendaria! ++Defesa\n")
            player.defesa += 4
        elif n == 3:
            print("Você encontrou uma espada lendaria! ++Ataque\n")
            player.ataque += 4
        elif n == 4:
            print("Você encontrou uma armadura nova! +Defesa\n")
            player.defesa += 2
    elif tipo == 3:
        print("Você encontrou uma chave!")
        player.PegarItem(chaveDoPortaoDoCastelo)
