import random

class Personagem:
    def __init__(self, nome, vida, ataque, defesa, destreza, inteligencia, player = 0):
        self.nome = nome
        self.vida = vida
        self.vidaMax = vida
        self.ataque = ataque
        self.defesa = defesa
        self.destreza = destreza
        self.inteligencia = inteligencia
        self.player = player

        self.morto = False       
        self.invencibilidade = 0
        self.invencibilidadeTurnos = 0
        
        self.mana = inteligencia
        self.magias = []
        
        self.inventario = []

    def Atacar(self):
        dado = random.randint(1,6)
        dano = self.ataque * dado / 2
        if dado == 6: print(self.nome, "deu um Ataque Crítico!")
        return dano

    def Dano(self, dano):
        if self.invencibilidade == 0:
            if self.defesa/2 >= dano:
                self.vida -= 1
            else:
                self.vida -= dano - (self.defesa/2)

    def AdquirirMagia(self, novaMagia):
        self.magias.append(novaMagia)

    def PegarItem(self, novoItem):
        c = 0
        for item in self.inventario:
            if item.nome == novoItem.nome:
                item.qtd += 1
                break
            else: c += 1
        if c >= len(self.inventario): self.inventario.append(novoItem)

    def Morrer(self):
        global gameplay
        if self.player == 1:
            print("\n\n\n*Game Over! Você foi derrotado...\n\n\n")
            self.morto = True
        else:
            print("O", self.nome, "esta morto!")
            print("Você venceu!\n------------------")
