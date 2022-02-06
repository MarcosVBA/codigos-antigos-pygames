from src.personagem import *
from src.obj.magias import *

goblin = Personagem("Goblin", 80, 7, 5, 12, 1)
goblin.AdquirirMagia(investida)

minotauro = Personagem("Minotauro", 200, 10, 10, 3, 3)

lobo = Personagem("Lobo", 100, 10, 20, 10, 1)
lobo.AdquirirMagia(investida)

zumbi = Personagem("Zumbi", 200, 3, 1, 1, 1)

nobreZumbi = Personagem("Nobre Zumbi", 200, 6, 1, 1, 2)
