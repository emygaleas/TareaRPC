import grpc
import calculadora_pb2_grpc
import calculadora_pb2

cliente = grpc.insecure_channel('localhost:5000')
# Permite llamar a las funciones remotas
stub = calculadora_pb2_grpc.CalculadoraStub(cliente)

def menu():
    print(" ---------- MENÚ CALCULADORA ---------- ")
    print("1. Sumar \n2. Restar \n3. Multiplicar \n4. Dividir")
    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Debes ingresar un número del 1 al 4.")
        exit()
    if opcion < 1 or opcion > 4:
        print("Opción no válida")
        exit()
    else:
        return opcion

def operacion(opcion):
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Debes ingresar un número válido")
        exit()
    if opcion == 1:
        r1 = stub.Sumar(
            calculadora_pb2.Operacion(a=a, b=b)
        )
        print("El resultado de la suma es:", r1.r)
    elif opcion == 2:
        r1 = stub.Restar(
            calculadora_pb2.Operacion(a=a, b=b)
        )
        print("El resultado de la resta es:", r1.r)
    elif opcion == 3:
        r1 = stub.Multiplicar(
            calculadora_pb2.Operacion(a=a, b=b)
        )
        print("El resultado de la multiplicación es:", r1.r)
    elif opcion == 4:
        if(b == 0):
            print("No se puede dividir para 0")
        r1 = stub.Dividir(
            calculadora_pb2.Operacion(a=a, b=b)
        )
        print("El resultado de la división es:", r1.r)

opcion = menu()
operacion(opcion)