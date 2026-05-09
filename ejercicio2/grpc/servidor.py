import grpc
from concurrent import futures

import conversion_pb2
import conversion_pb2_grpc

class ConversionServidor(
    conversion_pb2_grpc.ConversionServicer
):
    def CelsiusFahrenheit(self, request, context):
        resultado = (request.a*9/5) + 32
        return conversion_pb2.Resultado(r = resultado)
    
    def FahrenheitCelsius(self, request, context):
        resultado = (request.a-32) * 5/9
        return conversion_pb2.Resultado(r = resultado)
    
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

conversion_pb2_grpc.add_ConversionServicer_to_server(
    ConversionServidor(),
    servidor
)

# Indicar en que puerto va a trabajar
servidor.add_insecure_port('[::]:5000') # localhost

#Inicializar el servidor
servidor.start()

print("Servidor gRPC ejecutándose")

# Mantener encendido el servidor
servidor.wait_for_termination()