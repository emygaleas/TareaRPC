from xmlrpc.server import SimpleXMLRPCServer

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if(b == 0):
        return "No se puede dividir para 0"
    else:
        return a/b

# servidor = SimpleXMLRPCServer(("localhost", 8000))
servidor = SimpleXMLRPCServer(("0.0.0.0", 8000))

# Directorio:
servidor.register_function(sumar, "sumar")
servidor.register_function(restar, "restar")
servidor.register_function(multiplicar, "multiplicar")
servidor.register_function(dividir, "dividir")

print("El servidor está activo, esperando conexiones...")

servidor.serve_forever()