import xmlrpc.client

# Se establece un canal de comunicación
cliente = xmlrpc.client.ServerProxy("http://localhost:8000")

def menu():
    print(" ---------- MENÚ CONVERSIONES ---------- ")
    print("1. Celsius a Fahrenheit \n2. Fahrenheit a Celsius")
    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Debes ingresar una opción válida (1-2)")
        exit()
    if opcion < 1 or opcion > 2:
        print("Opción no válida")
        exit()
    else:
        return opcion
    
def operacion(opcion):
    try:
        a = float(input("Ingresa el número a convertir: "))
    except ValueError:
        print("Debes ingresar un número válido.")
        exit()
    if opcion == 1:
        r = cliente.CelsiusFahrenheit(a)
        print("La conversión de Celsius a Fahrenheit es: ", r)
    elif opcion == 2:
        r = cliente.FahrenheitCelsius(a)
        print("La conversión de Fahrenheit a Celsius es: ", r)

opcion = menu()
operacion(opcion)