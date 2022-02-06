

def MostrarMagias(player):
    print("\n------ MAGICAS ------")
    for magia in player.magias:
        print("->", magia.nome)

def MostrarInventario(player):
    print("\n------ INVENTARIOS ------")
    for item in player.inventario:
        print("->", item.nome, "| Tipo:", item.tipo,"| Descrição:", item.desc, "| Qtd:", item.qtd)
def MostraStatusBatalha(player, inimigo):
    print("\n-----------------\n->"+inimigo.nome+"<-")
    if inimigo.invencibilidade == 1: print("~invencibilidade")
    print("Vida:","<"+"X"*round(inimigo.vida/inimigo.vidaMax*10)+"*"*(10 - round(inimigo.vida/inimigo.vidaMax*10))+">")
    print("Mana:","<"+"X"*round(inimigo.mana/inimigo.inteligencia*10)+"*"*(10 - round(inimigo.mana/inimigo.inteligencia*10))+">")
    print("\n------X-----\n")
    print("->"+player.nome+"<-")
    if player.invencibilidade == 1: print("~invencibilidade")
    print("Vida:","<"+"X"*round(player.vida/player.vidaMax*10)+"*"*(10 - round(player.vida/player.vidaMax*10))+">")
    print("Mana:","<"+"X"*round(player.mana/player.inteligencia*10)+"*"*(10 - round(player.mana/player.inteligencia*10))+">")
    print("-----------------")
