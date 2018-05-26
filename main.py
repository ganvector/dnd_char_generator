from raca import *
from classe import *

if __name__ == "__main__":
    p_raca = Human()
    p_raca2 = Dwarf()

    atributos = [1, 2, 3, 4, 5, 6]
    atributos2 = [1, 2, 3, 4, 5, 6]

    atributos = [x + y for x, y in zip(atributos, p_raca.atributos)]

    print(atributos)

    atributos2 = [x + y for x, y in zip(atributos2, p_raca2.atributos)]

    print(atributos2)

    p_classe = Barbarian(1)

    print(p_classe.level)
    print(p_classe.hitdice)
