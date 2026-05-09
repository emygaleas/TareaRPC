from xmlrpc.server import SimpleXMLRPCServer

def CelsiusFahrenheit(C):
    return (C*9/5) + 32

def FahrenheitCelsius(F):
    return (F-32) * 5/9

servidor = SimpleXMLRPCServer(('localhost', 8000))

servidor.register_function(CelsiusFahrenheit, "CelsiusFahrenheit")
servidor.register_function(FahrenheitCelsius, "FahrenheitCelsius")

print("El servidor está activo esperando conexiones...")
servidor.serve_forever()
