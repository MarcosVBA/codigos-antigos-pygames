import random

gameplay = True
local = 8
localAnterior = 1
contadores = []

from src.personagem import *
from src.magia import *
from src.item import *
from src.local import *
from src.batalha import *
from src.bau import *
from src.contador import *
from src.status import *

from src.obj.itens import *
from src.obj.magias import *
from src.obj.monstros import *
from src.obj.locais import *


##################################################### GAMEPLAY ########################################################

print("\n################ Whatever ###################\n")

print("Em um castelo no meio de uma floresta densa e perigosa nos arredores da cidade de Westwood mora um mago necromante, este mago tem o objetivo de levantar um enorme exercito de zumbis para atacar o emperio, e para isso ele utiliza o castelo como seu laboratório, revivendo antigos guerreiros que serviram lá. você é um aventureiro que estava de passagem pelos arredores e ouviu sobre esta historia, acreditando que poderia ajudar a se livrando do mago, oque também traria alguma recompensa, você se prepara e no dia seguinte você adentra a floresta atrás do antigo castelo...")

escNome = input("\n*Qual é o seu nome, aventureiro? ")
while 1:
    escClasse = input("\n*Qual é a sua profisão?\n*guerreiro\n*mago\n*ladino\n\n-> ")
    if escClasse == "guerreiro":
        player = Personagem(escNome, 150, 14, 10, 4, 8, 1)
        player.AdquirirMagia(furia)
        break
    elif escClasse == "mago":
        player = Personagem(escNome, 100, 6, 10, 6,  20, 1)
        player.AdquirirMagia(Magia("bola de fogo", "dado*4 + 35", "Dano"))
        break
    elif escClasse == "ladino":
        player = Personagem(escNome, 80, 8, 5, 25, 15, 1)
        player.AdquirirMagia(Magia("sombra", "dado/2", "Invencibilidade"))
        player.AdquirirMagia(investida)
        break
    else:
        print("+Comando invalido!")
player.PegarItem(Item("pocao media", "Poção", "Cura 50 pontos de vida", 50))
player.PegarItem(Item("manual", "Texto", "Digite 'usar' para usar itens do 'inventario' ou para magias do menu de 'magias'. Se você quiser deletar algum item use 'deletar' fora de batalha, tente deletar este item."))

while gameplay:
    if(player.morto == False): local = locais[local].OlharLocal(player, local, localAnterior, contadores)
    else:
        input()
        gameplay = False


