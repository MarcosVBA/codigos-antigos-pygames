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
        global locais
        if self.porta == "norte":
            locais[self.lugar].norte = self.destino
        if self.porta == "sul":
            locais[self.lugar].sul = self.destino
        if self.porta == "leste":
            locais[self.lugar].leste = self.destino
        if self.porta == "oeste":
            locais[self.lugar].oeste = self.destino

    def Deletar(self, pessoa):
        pessoa.inventario.remove(self)
