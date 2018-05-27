from personagem import Personagem
from raca import *
from classe import *
from tkinter import *
from tkinter import ttk

racas = ["Anao", "Elfo", "Hafling", "Humano", "Draconato", "Gnomo", "Tiefling"]
dict_racas = {"Anao":1, "Elfo":2, "Hafling":3, "Humano":4, "Draconato":5, "Gnomo":6, "Tiefling":7}
classes = ["Barbaro", "Bardo", "Bruxo", "Clerigo", "Druida", "Feiticeiro", "Guerreiro", "Ladino", "Mago", "Monge", "Paladino", "Patrulheiro"]
dict_classes = {"Barbaro":1, "Bardo":2, "Bruxo":3, "Clerigo":4, "Druida":5, "Feiticeiro":6, "Guerreiro":7, "Ladino":8, "Mago":9, "Monge":10, "Paladino":11, "Patrulheiro":12}

def Cumprimente():
    hello.set("Olá, você!")

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

    print(racas)

    character = Personagem("Anao", "Guerreiro")

    print(character.raca)
    print(character.classe)
    #gui = Tk()

    #gui.title("Py5 - Python + Tkinter")
    #gui.geometry("400x300")
    #texto = Text(gui, width=30, height=1)
    #texto.pack()
    #btn = Button(gui, text="Cumprimente", command=Cumprimente)
    #btn.pack()

    #listaRaca = StringVar()
    #comboRaca = ttk.Combobox(gui, textvariable=listaRaca, text="Racas")
    #comboRaca["values"] = racas
    #comboRaca.pack()

    #listaClasse = StringVar()
    #comboClasse = ttk.Combobox(gui, textvariable=listaClasse, text="Classes")
    #comboClasse["values"] = classes
    #comboClasse.pack()

    #gui.mainloop()