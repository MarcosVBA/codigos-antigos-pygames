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
            self.tempo -= 1
            if self.tempo <= 0:
                self.alvo.ataque -= eval(self.eq)
                self.terminou = True
