from src.batalha import *
from src.status import *
from src.bau import *

class Local:
    def __init__(self, nome, desc, norte, sul, leste, oeste, monstro = None, bau = 0):
        self.nome = nome
        self.desc = desc
        
        self.norte = norte
        self.sul = sul
        self.leste = leste
        self.oeste = oeste
        
        self.monstro = monstro
        self.temMonstro = True
        self.bau = bau

    def OlharLocal(self, player, local, localAnterior, contadores):
        if self.monstro != None and self.temMonstro == True:
            print("Você encontra um", self.monstro.nome,"no caminho, ele te ataca!")
            Batalhar(player, self.monstro, contadores)
            self.temMonstro = False
        if player.morto == False:
            print("\n*"+self.nome+":", self.desc)
            print("\nVida:","<"+"X"*round(player.vida/player.vidaMax*10)+"*"*(10 - round(player.vida/player.vidaMax*10))+">")
            print("Mana:","<"+"X"*round(player.mana/player.inteligencia*10)+"*"*(10 - round(player.mana/player.inteligencia*10))+">")
            print("-----------------")
            while 1:
                agir = 0
                esc = input("\nO que você faz: ")
                if esc == "ir para o norte" and self.norte != None or esc == "ir para frente" and self.norte != None or esc == "norte" and self.norte != None:
                    localAnterior = local
                    return self.norte
                    break
                elif esc == "ir para o sul" and self.sul != None or esc == "ir para tras" and self.sul != None or esc == "sul" and self.sul != None:
                    localAnterior = local
                    return self.sul
                    break
                elif esc == "ir para o leste" and self.leste != None or esc == "ir para direita" and self.leste != None or  esc == "leste" and self.leste != None or esc == "ir para a direita" and self.leste != None:
                    localAnterior = local
                    return self.leste
                    break
                elif esc == "ir para o oeste" and self.oeste != None or esc == "ir para esquerda" and self.oeste != None or esc == "oeste" and self.oeste != None or esc == "ir para a esquerda" and self.oeste != None:
                    localAnterior = local
                    return self.oeste
                    break
                elif esc == "voltar":
                    lixo = local
                    local = localAnterior
                    localAnterior = lixo
                    return local
                    break
                elif esc == "procurar item":
                    if self.bau != 0:
                        Bau(self.bau, player)
                        self.bau = 0
                    else: print("Não tem item nesta região")
                elif esc == "magias": MostrarMagias(player)
                elif esc == "inventario": MostrarInventario(player)
                else:
                    for item in player.inventario:
                        if esc == "deletar " + item.nome:
                            item.Deletar(player)
                            agir = 1
                            break
                    for item in player.inventario:
                        if esc == "usar "+item.nome:
                            item.Usar(player)
                            agir = 2;
                            break
                    if agir == 0: print("*Comando invalido! Tente 'ir para o' ou 'procurar item'")
                    if agir == 2: return local
