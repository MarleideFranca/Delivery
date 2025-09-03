import pika
import json
import time

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Criar fila "pedidos"
channel.queue_declare(queue="pedidos")

# Lista simulada de pedidos
pedidos = [
    {"id": 1, "cliente": "João", "produto": "Pizza Calabresa"},
    {"id": 2, "cliente": "Maria", "produto": "Hambúrguer"},
    {"id": 3, "cliente": "Carlos", "produto": "Sushi"},
]

for pedido in pedidos:
    mensagem = json.dumps(pedido)
    channel.basic_publish(exchange="", routing_key="pedidos", body=mensagem)
    print(f"[x] Pedido enviado: {mensagem}")
    time.sleep(1)

connection.close()
