#Un juego para mi hijo Luciano para reforzar las tablas de multiplicar versión voz electrónica

#Si no está instalado el motor de voz en windows
#py -m pip install pyttsx3 
#bash python3 -m pip install pyttsx3
#Además de hacer falta verificar si están todas las dependencias
#pip install pywin32
#pip install pyttsx3


import random
import pyttsx3
import time

# Inicializar el motor de voz
motor = pyttsx3.init()
motor.setProperty('rate', 160)  # Velocidad de habla


def hablar(digo):
    motor.say(str(digo))
    motor.runAndWait()
    #time.sleep(0.5)  # Segundos


def chicken_jockey():
    # ASCII art simple de "CHICKEN JOCKEY !"
    mensaje = [
    "####### #      # # ####### #    # ###### #      #",
    "#       #      # # #       #  #   #      # #    #",
    "#       ######## # #       # #    ###### #  #   #",
    "#       #      # # #       #  #   #      #    # #",
    "####### #      # # ####### #    # ###### #     ##",
    "   J        O      C      K     E       Y     ! !"]
   
    for linea in mensaje:
        print('\033[91m' + linea + '\033[0m') #solo funciona la secuncia de color rojo desde la consola

def zombie_face():
    # Zombie face (8x8 style)
    zombie_face = [
    "  █░█░█░█░█",
    " █░░░░░░░░░█",
    "█░░███░███░░█",
    "█░░░░██░░░░░█",
    " █░░░░░░░░░█",
    "  ░█░█░█░█░"]
    
    for fila in zombie_face:
        print(fila)

#main()
print("Hola Luciano!")
hablar("Hola Luciano!")

print("¿Es cierto que sabes las tablas de multiplicar?")
hablar("¿Es cierto que sabes las tablas de multiplicar?, ¡ya lo veremos!")
#wait = input('')


#construir tabla del 1 al 10
tmult = []

for i in range(1,11):
    for j in range(1,11):
        tmult.append([i,j,i*j])

# aleatorios entre 1 y 10 preguntar la tablas axb
nA = random.randint(1, 10)
nB = random.randint(1, 10)

hablar("Empezamos el juego, sales al pulsar la letra s")
print(f"...Dime cuánto es {nA} multiplicado por {nB}?", end='')
hablar(f"...Dime cuánto es {nA} multiplicado por {nB}?")
R = input('')


while ( R != 's'):

    if ( R.isdigit() ):

        R = int(R)

        if [nA,nB,R] in tmult:
            hablar(f"Es correcto! {nA} por {nB} es igual a {nA*nB} ...GANAS UN POLLO MONTADO !!")
            chicken_jockey()
        else:
            hablar(f"No es correcto! {nA} por {nB} es {nA*nB} ...TIENES CARA DE ZOMBIE")
            zombie_face()
    else:
        hablar("Continuamos el juego, sales al pulsar la letra s")

    nA = random.randint(1, 10)
    nB = random.randint(1, 10)
    print(f"...Dime cuánto es {nA} multiplicado por {nB}?", end='')
    hablar(f"...Dime cuánto es {nA} multiplicado por {nB}?")
    R = input('')
    
