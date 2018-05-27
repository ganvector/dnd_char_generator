from dado import Dice


class Barbarian:

    def __init__(self, level):
        self.level = level
        self.hitdice = 12
        self.proficiencia = ["armaduras leves","armaduras medias", "escudos", "armas simples", "armas marciais"]

class Bard:

    def __init__(self, level):
        self.level = level
        self.hitdice = 8
        self.proficiencia = ["armaduras leves", "armas simples", "bestas de mao", "espadas longa", "rapieiras", "espadas curtas"]

class Warlock:

    def __init__(self, level):
        self.level = level
        self.hitdice = 8
        self.proficiencia = ["armaduras leves", "armas simples"]

class Cleric:

    def __init__(self, level):
        self.level = level
        self.hitdice = 8
        self.proficiencia = ["armaduras leves", "armaduras medias", "escudos", "armas simples"]

class Druid:

    def __init__(self, level):
        self.level = level
        self.hitdice = 8
        self.proficiencia = ["armaduras leves", "armaduras medias", "escudos", "clavas", "adagas", "dardos", "azagaias", "macas", "bordoes", "cimitarras", "foices", "fundas", "lancas"]

class Sorcerer:

    def __init__(self, level):
        self.level = level
        self.hitdice = 6
        self.proficiencia = ["adagas", "dardos", "fundas", "bordoes", "bestas leves"]

class Fighter:

    def __init__(self, level):
        self.level = level
        self.hitdice = 10
        self.proficiencia = ["armaduras leves", "armaduras medias", "armaduras pesadas", "armas simples", "armas marciais"]

class Rogue:

    def __init__(self, level):
        self.level = level
        self.hitdice = 8
        self.proficiencia = ["armaduras leves", "armas simples", "bestas de mao", "espadas longas", "rapieiras", "espadas curtas"]

class Mage:

    def __init__(self, level):
        self.level = level
        self.hitdice = 6
        self.proficiencia = ["adagas", "dardos", "fundas", "bastoes", "bestas leves"]

class Monk:

    def __init__(self, level):
        self.level = level
        self.hitdice = 8
        self.proficiencia = ["armas simples", "espadas curtas"]

class Paladin:

    def __init__(self, level):
        self.level = level
        self.hitdice = 10
        self.proficiencia = ["armaduras simples", "armaduras medias", "armaduras pesadas", "escudos", "armas simples", "armas marciais"]

class Ranger:

    def __init__(self, level):
        self.level = level
        self.hitdice = 10
        self.proficiencia = ["armaduras leves", "escudos", "armas simples", "armas marciais"]