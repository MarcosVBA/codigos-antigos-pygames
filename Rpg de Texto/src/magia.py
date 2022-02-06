import random
from src.contador import *

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

    def Usar(self, usuario, alvo, contadores):
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
            return contadores
