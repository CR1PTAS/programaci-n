"""""
Juego de piedra papel o tijera (2,5 puntos). El usuario introduce un valor (1-
Piedra|2- Papel|3-Tijera), si no es correcto se volver a pedir de nuevo hasta que se correcta.
La “maquina” generará un valor aleatorio (de 1 a 3) para elegir piedra, papel o tijera. Al
finalizar, mostrará la opción del usuario y de la máquina e indicará si hemos ganado, perdido o
empatado. 
Máxima puntuación (3 puntos): el juego finalizará cuando la máquina o el usuario gane 3
partidas
"""""
import random 
maquina = 0
contar_maquina = 0
contar_numero = 0


while True:
    numero = int(input(f"Seleccione una opcion, 1 piedra, 2 papel, 3 tijeras:"))
    maquina = random.randint(1,3)
    if numero == 1 and maquina == 3:
        contar_numero +=1
        print("Enhorabuena,punto para usted")
    elif numero == 1 and maquina == 2:
        contar_maquina +=1
        print("Lo siento, punto para mi")
    elif numero == 2 and maquina == 1:
        contar_numero +=1
        print("Enhorabuena, punto para usted")
    elif numero == 2 and maquina == 2:
        contar_maquina +=1
        print("Lo siento,punto para mi")
    elif numero == 3 and maquina == 2:
        contar_maquina +=1
        print("Enhorabuena, punto para usted")
    elif numero == 3 and maquina == 1:
        contar_maquina +=1
        print("Lo siento,punto para mi")
    elif numero == 1 and maquina == 1:
        print("Empate")
    elif numero == 2 and maquina == 2:
        print("Empate")
    elif numero == 3 and maquina == 3:
        print("Empate")
    if contar_numero == 3:
        print("Enhorabuena, me has ganado")
        break
    elif contar_maquina == 3:
        print("Te he ganado, intentalo otra vez") 
        break