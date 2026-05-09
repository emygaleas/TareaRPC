import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8000")

def menu():
    print("----- MENÚ OPERACIONES -----")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    try:
        opcion = int(input("Ingresa una opción (1-4): "))
    except ValueError:
        print("Debes ingresar un número del 1 al 4.")
        return menu()
    if (opcion > 5 or opcion < 1):
        print("Opción incorrecta")
        return menu()
    else:
        return opcion

def opciones(opcion):
    if (opcion == 5):
        print("Saliendo del programa...")
        exit()
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Debes ingresar números válidos, no letras/caracteres especiales.")
        return
    if (opcion == 1):
        r = cliente.sumar(a,b)
        print("El resultado de la suma es:", r)
    elif (opcion == 2):
        r = cliente.restar(a,b)
        print("El resultado de la resta es:", r)
    elif (opcion == 3):
        r = cliente.multiplicar(a,b)
        print("El resultado de la multiplicación es:", r)
    elif (opcion == 4):
        r = cliente.dividir(a,b)
        print("El resultado de la división es:", r)

while True:
    opcion = menu()
    opciones(opcion)
