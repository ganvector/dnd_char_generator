from classe import *
from raca import *

dict_racas = {"Anao":1, "Elfo":2, "Hafling":3, "Humano":4, "Draconato":5, "Gnomo":6, "Tiefling":7}
dict_classes = {"Barbaro":1, "Bardo":2, "Bruxo":3, "Clerigo":4, "Druida":5, "Feiticeiro":6, "Guerreiro":7, "Ladino":8, "Mago":9, "Monge":10, "Paladino":11, "Patrulheiro":12}


class Personagem:

    def __init__(self, raca, classe):
        self.nome = ""
        self.escolha_raca(raca)
        self.escolha_classe(classe)
        self.alinhamento = ""
        self.atributos = ""
        self.ca = ""
        self.hitPoints = ""
        self.hitDice = ""
        self.velocidade = ""
        self.saveThrows = ""
        self.pericias = ""
        self.passivePerception = ""
        self.acoes = ""
        self.initiative = ""

    def escolha_raca(self, raca):
        if (raca == "Anao"):
            self.raca = Dwarf()
        elif (raca == "Elfo"):
            self.raca = Elf()
        elif (raca == "Halfing"):
            self.raca = Human()
        elif (raca == "Draconato"):
            self.raca = Dracronair()
        elif (raca == "Gnomo"):
            self.raca = Gnome()
        else:
            self.raca = Tiefling()

    def escolha_classe(self, classe):
        if(classe == "Barbaro"):
            self.classe = Barbarian(1)
        elif(classe == "Bardo"):
            self.classe = Bard(1)
        elif(classe == "Bruxo"):
            self.classe = Warlock(1)
        elif(classe == "Clerigo"):
            self.classe = Cleric(1)
        elif(classe == "Druida"):
            self.classe = Druid(1)
        elif(classe == "Feiticeiro"):
            self.classe = Sorcerer(1)
        elif(classe == "Guerreiro"):
            self.classe = Fighter(1)
        elif(classe == "Ladino"):
            self.classe = Rogue(1)
        elif(classe == "Mago"):
            self.classe = Mage(1)
        elif(classe == "Monge"):
            self.classe = Monk(1)
        elif(classe == "Paladino"):
            self.classe = Paladin(1)
        elif(classe == "Patrulheiro"):
            self.classe = Ranger(1)