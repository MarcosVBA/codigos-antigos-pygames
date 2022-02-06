from src.status import *

def Batalhar(player, inimigo, contadores):
    inimigo.vida = inimigo.vidaMax
    inimigo.mana = inimigo.inteligencia
    if inimigo.destreza >= player.destreza:
        print("O",inimigo.nome,"atacou você!")
        player.Dano(inimigo.Atacar())
        if player.vida <= 0:
            player.Morrer()
            return
    while 1:
        if player.vida <= 0:
            player.Morrer()
            break
        MostraStatusBatalha(player, inimigo)
        while 1:
            agir = 0
            esc = input("\nO que você faz? ")
            if esc == "atacar":
                inimigo.Dano(player.Atacar())
                break
            elif esc == "correr": break
            elif esc == "magias": MostrarMagias(player)
            elif esc == "inventario": MostrarInventario(player)
            else:
                for magia in player.magias:
                    if esc == "usar "+magia.nome:
                        if player.mana > 0:
                            if magia.tipo != "Buff":
                                magia.Usar(player, inimigo)
                                agir = 1;
                                break
                            else:
                                magia.Usar(player, inimigo, contadores)
                                agir = 1;
                                break
                        else: print("Sem mana!")
                for item in player.inventario:
                    if esc == "usar "+item.nome:
                        item.Usar(player)
                        agir = 1;
                        break
                if agir == 0: print("*Comando invalido! Tente 'atacar' ou 'correr'")
                else: break
        if player.vida <= 0:
            player.Morrer()
            break
        if inimigo.vida <= 0:
            inimigo.Morrer()
            break
        else:
            try:
                if inimigo.mana > 0 and inimigo.magias[0]:
                    print("O",inimigo.nome, "usou", inimigo.magias[0].nome,"!")
                    inimigo.magias[0].Usar(inimigo,player)
                else:
                    print("O",inimigo.nome,"atacou você!")
                    player.Dano(inimigo.Atacar())
                    
            except:
                print("O",inimigo.nome,"atacou você!")
                player.Dano(inimigo.Atacar())
            finally:
                for contador in contadores:
                    if contador.terminou == False: contador.Checar()
                player.invencibilidadeTurnos -= 1
                if player.invencibilidadeTurnos <= 0: player.invencibilidade = 0
                
                inimigo.invencibilidadeTurnos -= 1
                if inimigo.invencibilidadeTurnos <= 0: inimigo.invencibilidade = 0
