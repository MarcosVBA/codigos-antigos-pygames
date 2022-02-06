import random

############################################### CLASSES #######################################################

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
            gameplay = False
        else:
            print("O", self.nome, "esta morto!")
            print("Você venceu!\n------------------")

#Contador<--------------------------------------
class Contador:
    def __init__(self, alvo, atr, eq, tempo):
        self.alvo = alvo
        self.atr = atr
        self.eq = eq
        self.tempo = tempo
        self.original = eval("alvo."+atr)
        self.terminou = False

    def Iniciar(self):
       self.alvo.ataque += eval(self.eq)

    def Checar(self):
            print(self.alvo.ataque)
            print(self.tempo)
            self.tempo -= 1
            if self.tempo <= 0:
                self.alvo.ataque -= eval(self.eq)
                self.terminou = True
            
#Magicas<--------------------------------------
class Magia:
    def __init__(self, nome, calc, tipo, plus = None):
        self.nome = nome
        self.calc = calc
        self.tipo = tipo
        self.plus = plus

    def Usar(self, usuario, alvo):
        if self.tipo == "Dano":
            usuario.mana -= 1
            dado = random.randint(1, 6)
            dano = eval(self.calc)
            alvo.Dano(dano)
            if self.plus != None: eval(self.plus)
        elif self.tipo == "Invencibilidade":
            usuario.mana -= 1
            dado = random.randint(1, 6)
            turnos = round(eval(self.calc)+1)
            usuario.invencibilidade = 1
            usuario.invencibilidadeTurnos = abs(turnos)
            if self.plus != None: eval(self.plus)
        elif self.tipo == "Ataque":
            usuario.mana -= 1
            alvo.Dano(usuario.Atacar()+eval(self.calc))
            if self.plus != None: eval(self.plus)

class MagiaBuff(Magia):
    def __init__(self, nome, calc, buff, plus = None):
        self.nome = nome
        self.calc = calc
        self.buff = buff
        self.tipo = "Buff"
        self.plus = plus

    def Usar(self, usuario, alvo):
        global contadores
        negar = False
        for contador in contadores:
            if contador.alvo == usuario and contador.terminour == False:
                negar = True
        if negar == False:
            usuario.mana -= 1
            
            dado = random.randint(1, 6)
            turnos = round(eval(self.calc)+1)
            
            contadores.append(Contador(usuario, "ataque", self.buff, turnos))
            contadores[len(contadores)-1].Iniciar()
            
            if self.plus != None: eval(self.plus)
        
#Itens<-------------------------------------------
class Item:
    def __init__(self, nome, tipo, desc, poder = 0, qtd = 1):
        self.nome = nome
        self.tipo = tipo
        self.poder = poder
        self.desc = desc
        self.qtd = qtd

    def Usar(self, alvo):
        if self.tipo == "Poção":
            alvo.vida += self.poder
            if alvo.vida > alvo.vidaMax:
                alvo.vida = alvo.vidaMax
        elif self.tipo == "Elixir":
            alvo.mana += self.poder
            if alvo.mana > alvo.inteligencia:
                alvo.mana = alvo.inteligencia
        elif self.tipo == "Texto":
            print("\n",self.desc,"\n")
            self.qtd += 1
        self.qtd -= 1
        if self.qtd <= 0:
            alvo.inventario.remove(self)

    def Deletar(self, pessoa):
        pessoa.inventario.remove(self)

#Chaves<----------------------------------------------
class Chave:
    def __init__(self, nome, desc, lugar, porta, destino):
        self.nome = nome
        self.lugar = lugar
        self.porta = porta
        self.desc = desc
        self.destino = destino
        self.tipo = "Chave"
        self.qtd = 1

    def Usar(self, alvo):
        print("\nA porta foi desbloqueada\n")
        Destrancar(self.lugar, self.porta, self.destino)

    def Deletar(self, pessoa):
        pessoa.inventario.remove(self)

#Locais<-----------------------------------------------
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

    def OlharLocal(self):
        global local, localAnterior
        if self.monstro != None and self.temMonstro == True:
            print("Você encontra um", self.monstro.nome,"no caminho, ele te ataca!")
            Batalhar(self.monstro)
            self.temMonstro = False
        if player.morto == False:
            print("\n*"+self.nome+":", self.desc)
            print("\nVida:","<"+"X"*round(player.vida/player.vidaMax*10)+"*"*(10 - round(player.vida/player.vidaMax*10))+">")
            print("Mana:","<"+"X"*round(player.mana/player.inteligencia*10)+"*"*(10 - round(player.mana/player.inteligencia*10))+">")
            print("-----------------")
            while 1:
                agir = 0
                esc = input("\nO que você faz: ")
                if esc == "ir para o norte" and self.norte != None or esc == "ir para frente" and self.norte != None:
                    localAnterior = local
                    local = self.norte
                    break
                elif esc == "ir para o sul" and self.sul != None or esc == "ir para tras" and self.sul != None:
                    localAnterior = local
                    local = self.sul
                    break
                elif esc == "ir para o leste" and self.leste != None or esc == "ir para direita" and self.leste != None:
                    localAnterior = local
                    local = self.leste
                    break
                elif esc == "ir para o oeste" and self.oeste != None or esc == "ir para esquerda" and self.oeste != None:
                    localAnterior = local
                    local = self.oeste
                    break
                elif esc == "voltar":
                    lixo = local
                    local = localAnterior
                    localAnterior = lixo
                    break
                elif esc == "procurar item":
                    if self.bau != 0:
                        Bau(self.bau)
                        self.bau = 0
                    else: print("Não tem item nesta região")
                elif esc == "magias": MostrarMagias()
                elif esc == "inventario": MostrarInventario()
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
                    if agir == 2: break

################################################# FUNÇÕES ###########################################################
                    
def Bau(tipo):
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
    
#<----------------------------------------------------------------
def Destrancar(lugar, porta, destino):
        if porta == "norte":
            locais[lugar].norte = destino
        if porta == "sul":
            locais[lugar].sul = destino
        if porta == "leste":
            locais[lugar].leste = destino
        if porta == "oeste":
            locais[lugar].oeste = destino

#<----------------------------------------------------------------        
def MostrarMagias():
    print("\n------ MAGICAS ------")
    for magia in player.magias:
        print("->", magia.nome)

#<----------------------------------------------------------------
def MostrarInventario():
    print("\n------ INVENTARIOS ------")
    for item in player.inventario:
        print("->", item.nome, "| Tipo:", item.tipo,"| Descrição:", item.desc, "| Qtd:", item.qtd)

#<----------------------------------------------------------------
def MostraStatusBatalha(inimigo):
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

#Sistema de Batalha<----------------------------------------------
def Batalhar(inimigo):
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
        MostraStatusBatalha(inimigo)
        while 1:
            agir = 0
            esc = input("\nO que você faz? ")
            if esc == "atacar":
                inimigo.Dano(player.Atacar())
                break
            elif esc == "correr": break
            elif esc == "magias": MostrarMagias()
            elif esc == "inventario": MostrarInventario()
            else:
                for magia in player.magias:
                    if esc == "usar "+magia.nome:
                        if player.mana > 0:
                            magia.Usar(player, inimigo)
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

################################################# VARIAVEIS ###########################################################

gameplay = True
locais = []
local = 1
localAnterior = 1
lixo = 0
contadores = []

############################################### ITENS E MAGIAS #########################################################

sombra = Magia("sombra", "dado/2", "Invencibilidade")
bolaDeFogo = Magia("bola de fogo", "dado*4 + 35", "Dano")
faisca = Magia("faisca", "dado*3 + 20", "Dano")
investida = Magia("investida", "10", "Ataque")
corteFantasma = Magia("corte fantasma", "10", "Ataque", "sombra.Usar(player,alvo)")
ataqueExplosivo = Magia("ataque explosivo", "10", "Ataque", "faisca.Usar(player,alvo)")
escudoExplosivo = Magia("escudo explosivo", "dado*4 + 6", "Dano", "sombra.Usar(player,alvo)")
ataqueDuplo = Magia("ataque duplo", "10", "Ataque", "investida.Usar(player,alvo)")
tempestadeDeChamas = Magia("tempestade de chamas", "dado*5 + 40", "Dano")
laminaDivina = Magia("lamina divina", "30", "Ataque")
ninjutsu = Magia("ninjutsu", "dado", "Invencibilidade")
furia = MagiaBuff("furia", "dado", "5")

pocaoPequena = Item("pocao pequena", "Poção", "Cura 35 pontos de vida", 35)
pocaoMedia = Item("pocao media", "Poção", "Cura 60 pontos de vida", 60)
pocaoGrande = Item("pocao grande", "Poção", "Cura 120 pontos de vida", 120)
pocaoDeAdrenalina = Item("pocao de adrenalina", "Poção", "Cura 80 pontos de vida", 80)
elixirMedio = Item("elixir medio", "Elixir", "Restaura 5 de mana perdina", 5)
elixirGrande = Item("elixir grande", "Elixir", "Restaura 15 de mana perdina", 15)
elixirDoMago = Item("elixir do mago", "Elixir", "Restaura 30 de mana perdina", 30)

chaveDoPortaoDoCastelo = Chave("chave do portao do castelo", "Usada para abrir o portão do castelo", 4, "norte", 10)

################################################## MONSTROS ###########################################################

goblin = Personagem("Goblin", 80, 7, 5, 12, 1)
goblin.AdquirirMagia(investida)

minotauro = Personagem("Minotauro", 200, 10, 10, 3, 3)

lobo = Personagem("Lobo", 100, 10, 20, 10, 1)
lobo.AdquirirMagia(investida)

zumbi = Personagem("Zumbi", 200, 3, 1, 1, 1)

nobreZumbi = Personagem("Nobre Zumbi", 200, 6, 1, 1, 2)

##################################################### DESCRIÇÕES #####################################################

nSei = "Não sei como você veio parar aqui?"
fl0 = "Após a batalha você percebe que este lugar pode ter algo de especial, *Talves seja legal 'procurar item' nesta região."
fl1 = "Você esta no inicio da floresta que ira te levar ao castelo do mago, ao norte você vê uma trilha que pode te levar em direção de seu objetivo, ao sul existe um caminho para uma clareira."
fl2 = "Você caminha até encontrar uma divisa na trilha, ao norte você continua seu caminho para o seu objetivo, ao oeste tem outro caminho para o castelo adentrando ainda mais na floresta, ao sul você volta para o inicio."
fl3 = "Você se encontra em uma encruzilhada em que ao norte esta o portão do castelo porem parece que para abri-la precisa-se de uma chave, ao leste esta a entrada do jardim do castelo, ao oeste tem um caminho alternativo para a floresta, ao sul você volta pra a trilha."
fl4 = "A trilha alternativa te leva para um caminho no meio da floresta ao oeste do castelo, se seguir para o norte você entrara ainda mais na floresta e estara mais perto do castelo, ao leste você retorna a trilha principal."
fl5 = "Você esta dentrao da floresta, ao leste exite um caminho que te guia para uma encruzilhada, ao sul você volta pra a entrada da floresta"
fl6 = "Você esta na entrada para o jardim do castelo, o fato do castelo estar abandonado fez com que nesta região esteja tomada pelo mato, ao leste você entra no jardim, e se seguir para o oeste você volta para a encruzilhada."
jl1 = "O jardim do castelo esta totalmente destruido, tomado pela vegetação e entulhos das paredes que cairam no chão, talvez tenha algum item por aqui, ao norte você vê uma passa entre duas colunas que te guia para a parte central do jardim, ao oeste você volta para a entrada."
jl2 = "A parte central do jardim é ando ficava a estufa do castelo, que agora já nem coseguia-se distingui-la dos entulhos do castelo, a trilha ao redor da estufa leva para uma porta lateral do castelo, e para o sul você volta para a segunda parte do jardim."


###################################################### LOCAIS ########################################################

locais.insert(0, Local("???? - ??" , nSei, None, None, None, None, minotauro))
locais.insert(1, Local("Floresta - L1", fl1, 3, 2, None, None))
locais.insert(2, Local("Floresta - L0" , fl0, 1, None, None, None, goblin, 1))
locais.insert(3, Local("Floresta - L2" , fl2, 4, 1, None, 5, goblin, 1))
locais.insert(4, Local("Floresta - L3" , fl3, None, 3, 7, 6))
locais.insert(5, Local("Floresta - L4" , fl4, 6, None, 3, None))
locais.insert(6, Local("Floresta - L5" , fl5, None, 5, 4, None, lobo, 2))
locais.insert(7, Local("Floresta - L6" , fl6, None, None, 8, 4, goblin))
locais.insert(8, Local("Jardim - L1" , jl1, 9, None, None, 7, None, 3))
locais.insert(9, Local("Jardim - L2" , jl2, None, 8, None, 11, zumbi, 2))
locais.insert(10, Local("Castelo - L1" , "", 14, 4, 11, 12, nobreZumbi, 1))
locais.insert(11, Local("Castelo - L2" , "", 16, None, 9, 10))
locais.insert(12, Local("Castelo - L3" , "", 13, None, 10, None))
locais.insert(13, Local("Castelo - L4" , "", None, 12, None, 14))
locais.insert(14, Local("Castelo - L5" , "", None, 11, None, None, nobreZumbi, 2))

##################################################### GAMEPLAY ########################################################

print("\n################ Whatever ###################\n")

print("Em um castelo no meio de uma floresta densa e perigosa nos arredores da cidade de Westwood mora um mago necromante, este mago tem o objetivo de levantar um enorme exercito de zumbis para atacar o emperio, e para isso ele utiliza o castelo como seu laboratório, revivendo antigos guerreiros que serviram lá. você é um aventureiro que estava de passagem pelos arredores e ouviu sobre esta historia, acreditando que poderia ajudar a se livrando do mago, oque também traria alguma recompensa, você se prepara e no dia seguinte você adentra a floresta atrás do antigo castelo...")

escNome = input("\n*Qual é o seu nome, aventureiro? ")
while 1:
    escClasse = input("\n*Qual é a sua profisão?\n*guerreiro\n*mago\n*ladino\n\n-> ")
    if escClasse == "guerreiro":
        player = Personagem(escNome, 150, 14, 10, 5, 8, 1)
        player.AdquirirMagia(Magia("investida", "10", "Ataque"))
        player.AdquirirMagia(furia)
        break
    elif escClasse == "mago":
        player = Personagem(escNome, 100, 6, 10, 6,  25, 1)
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
    if(player.morto == False): locais[local].OlharLocal()



