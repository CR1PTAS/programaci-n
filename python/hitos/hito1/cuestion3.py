"""""
Simular el funcionamiento de una cuenta bancaria (2.5 puntos): al iniciar el
programa, pediremos el saldo inicial de la cuenta (puede ser un número decimal), si el saldo es
menor que 0 se volverá a pedir hasta que sea correcto. 
Posteriormente mostraremos un menú con las opciones, 1-ingresar dinero, 2-retirar dinero y
3- mostrar saldo y 4-salir, si la opción no es correcta se volver a pedir de nuevo hasta que sea
correcta. No se pueden ingresar cantidades negativas y no podemos retirar dinero si nos
quedamos en números rojos. 
Máxima puntuación (3 puntos): incluir una opción más en el menú, estadísticas, que nos
muestre cuantos ingresos y retiradas se han efectuado

"""""
#Creamos las variables
ingresar_dinero = 0
retirar_dinero = 0
ingresar_saldo = 0
saldo = 0
contar_ingresos = 0
contar_retiradas = 0

saldo = int(input("Dame el saldo de tu cuenta bancaria, que no sea 0: "))
if saldo ==0:
    print("Dame otro saldo, por favor")
while True:
    menu_opciones = int(input("Dime que deseas hacer. 1-Ingresar dinero, 2-Retirar dinero, 3-Mostrar saldo, 4- salir o 5 - Estadísticas:"))
    if menu_opciones == 1:
        contar_ingresos +=1
        ingresar_dinero = int(input("Cuanto dinero deseas ingresar?:"))
        saldo = saldo + ingresar_dinero
    elif ingresar_dinero <0:
        ingresar_dinero = int(input("Numeros negativos no se pueden entregar, dame otra cantidad:"))
    else:
        menu_opciones == 0

    if menu_opciones == 2:
        contar_retiradas +=1
        retirar_dinero = int(input("Cuento dinero deseas retirar?:"))
        saldo = saldo - retirar_dinero
    elif retirar_dinero <0:
        retirar_dinero = int(input("Numeros negativos no se pueden retirar, dame otra cantidad:"))
    else:
        menu_opciones == 0
    
    if menu_opciones == 3:
        print(f"Tu saldo es de {saldo} euros")

    elif menu_opciones == 3:
        print("Hasta pronto")
        break

    elif menu_opciones == 5:
        print(f"Has efectuado un ingreso {contar_ingresos} veces")
        print(f"Has efectuado una retirada {contar_retiradas} veces")