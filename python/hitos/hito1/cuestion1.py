"""""
Mostrar figuras por pantalla (2,5 puntos): a través de un menú solicitaremos al
usuario que tipo de figura quiere mostrar (1-Cuadrado|2-Rectángulo), si la opción no es
correcta, se mostrará mensaje de error y se volverá a solicitar hasta que se correcta. 
▪ Si ha seleccionada un cuadrado, pediremos su lado y mostraremos la figura, su área y
perímetro
▪ Si ha seleccionada un rectángulo, pediremos base y altura y mostraremos la figura, su área y
perímetro.
Ejemplos de ejecución:

"""""

#Creamos las variables
base = 0
altura = 0
area = 0
perimetro = 0

#Creamos un bucle
while True:

#Pedimos que nos diga 1 o 2. Si elige 3 se cerrara el bucle
    numero = int(input("Dame un número(1 Cuadrado, 2 Rectangulo):"))

#Pedimos los datos para el cuadrado
    if numero ==1:
        base = int(input("Dame la base del cuadrado:"))
        area = base * base
        perimetro = base * 4
        print(f"El area del cuadrado es {area}")
        print(f"El perimetro del cuadrado es {perimetro}")

        for esquema in range(0,base):
            for i in range(0,base):
                print("*", end="")
            print()
#Pedimos los datos para el rectangulo
    elif numero == 2:
        base = int(input("Dame la base del rectangulo:"))
        altura = int("Dame la altura del rectangulo:")
        area = base * altura
        print(f"El area del rectangulo es {area}")

        for esquema in range(0,base):
            for i in range(0,altura):
                print("*",end="")
                print()
#Terminamos el bucle si ponemos 3
    elif numero ==3:
        break
#Si es otro numero que no es ni 1 ni 2, ponemos que pongan otro numero
    else:
        print("Opcion no valida, escribe 1 o2")