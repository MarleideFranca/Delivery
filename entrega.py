import pika
import json
import time

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Garantir que a fila "pedidos" existe
channel.queue_declare(queue="pedidos")

# Função de callback para processar os pedidos
def callback(ch, method, properties, body):
    pedido = json.loads(body)
    print(f"[>] Recebido pedido: {pedido}")
    print(f"Entregando {pedido['produto']} para {pedido['cliente']}...")
    time.sleep(2)
    print("Entrega concluída!\n")

# Consumidor escutando a fila
channel.basic_consume(queue="pedidos", on_message_callback=callback, auto_ack=True)

print(" [*] Aguardando pedidos. Pressione CTRL+C para sair.")
channel.start_consuming()