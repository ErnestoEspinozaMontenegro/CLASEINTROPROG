#Tirar un dado
from random import randint, choice

def tirar_dado():
    dado = [
                ["◙◙◙◙◙◙◙",
                 "◙     ◙",
                 "◙  *  ◙",
                 "◙     ◙",
                 "◙◙◙◙◙◙◙"],
                ["◙◙◙◙◙◙◙",
                 "◙  *  ◙",
                 "◙     ◙",
                 "◙  *  ◙",
                 "◙◙◙◙◙◙◙"],          
                ["◙◙◙◙◙◙◙",
                 "◙   * ◙",
                 "◙  *  ◙",
                 "◙ *   ◙",
                 "◙◙◙◙◙◙◙"],
                ["◙◙◙◙◙◙◙",
                 "◙ * * ◙",
                 "◙     ◙",
                 "◙ * * ◙",
                 "◙◙◙◙◙◙◙"],
                ["◙◙◙◙◙◙◙",
                 "◙ * * ◙",
                 "◙  *  ◙",
                 "◙ * * ◙",
                 "◙◙◙◙◙◙◙"],
                ["◙◙◙◙◙◙◙",
                 "◙ * * ◙",
                 "◙ * * ◙",
                 "◙ * * ◙",
                 "◙◙◙◙◙◙◙"]
            ]
    tirar = choice([0,1,2,3,4,5])
    for cara in dado[tirar]:
        print(cara)

while (True):
    tirar_dado()
    if (input("Otra tirada <ENTER> Salir con s:") == 's'): break
