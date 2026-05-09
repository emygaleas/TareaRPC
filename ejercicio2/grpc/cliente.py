import grpc
import conversion_pb2
import conversion_pb2_grpc

cliente = grpc.insecure_channel('localhost:5000')
stub = conversion_pb2_grpc.ConversionStub(cliente)

def menu():
    print(" ---------- MENÚ CONVERSIONES ---------- ")
    print("1. De Celsius a Fahrenheit \n2. De Fahrenheit a Celsius")
    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Debes ingresar un número del (1-2)")
        exit()
    if opcion < 1 or opcion > 2:
        print("Opción no válida")
        exit()
    else:
        return opcion

def conversion(opcion):
    try:
        valor = float(input("Ingresa el valor a convertir: "))
    except ValueError:
        print("Debes ingresar un número válido")
        exit()
    if opcion == 1:
        r1 = stub.CelsiusFahrenheit(conversion_pb2.Operacion(a=valor))
        print("El resultado de la conversión es:", r1.r)
    elif opcion == 2:
        r1 = stub.FahrenheitCelsius(conversion_pb2.Operacion(a=valor))
        print("El resultado de la conversión es:", r1.r)

opcion = menu()
conversion(opcion)