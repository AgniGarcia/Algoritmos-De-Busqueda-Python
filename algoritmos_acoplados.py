def exhaustiva(objetivo):
    objetivo = int(input("Escoge un número: "))
    respuesta = 0
    while respuesta**2 < objetivo:
        respuesta += 1
    if respuesta**2 == objetivo:
        print(f"La raíz cuadrada de {objetivo} es {respuesta}")
    else: 
        print(f"{objetivo} no tiene raíz cuadrada")


def aproximacion(objetivo, epsilon):
    objetivo = int(input("Escoge un número: "))
    epsilon = float(input("Selecciona un margen de error: "))
    paso = epsilon**2
    respuesta = 0.0    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        if abs(respuesta ** 2 - objetivo) >= epsilon:
            print(respuesta **2 - objetivo)
        else: 
            print(f"La raíz cuadrada de {objetivo} es {respuesta}")
        


def binario(objetivo, epsilon):
    pass



seleccion = int(input(f"""Formas para resolver la raíz cuadrada: /n 
1.- Enumeración exhaustiva (Díficil)
2.- Aproximación de solución (Semi)
3.- Busqueda binaria (Fácil)
Selecciona la que más te agrade: """))

if seleccion == 1: 
    print("Seleccionaste Enumeración exhaustiva")
    objetivo = 0
    exhaustiva(objetivo)
elif seleccion == 2:
    print("Seleccionaste Aproximacion de solucion")
    objetivo = 0.0
    epsilon = 0.0
    aproximacion(objetivo, epsilon)
elif seleccion == 3:
    print("Seleccionaste Busqueda binaria")
    objetivo = 0.0
    epsilon = 0.0
    binario (objetivo = int(input("Escribe un numero: ")), epsilon = float(input("Margen de error: "))) 
else:
    print("Esta opción no existe, por favor selecciona una del menu")


