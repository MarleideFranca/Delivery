# Sistema Simples de Delivery com RabbitMQ e Python 🚀🍔🍕

---

## 🔹 Tecnologias Utilizadas

- **Python 3** – linguagem principal do sistema  
- **RabbitMQ** – broker de mensagens (fila de mensagens)  
- **Pika** – biblioteca Python para integração com RabbitMQ  
- **Docker (opcional)** – para rodar RabbitMQ rapidamente  
- **JSON** – formato de mensagens entre produtor e consumidor  

---

## 🔹 Objetivo

Simular um sistema de delivery onde:

1. O **produtor** envia pedidos para uma fila (`pedido.py`)  
2. O **consumidor** processa os pedidos (`entrega.py`)  
3. O fluxo é **assíncrono**, permitindo múltiplos consumidores  

---

## 🔹 Fluxo do Sistema

Fluxo do Delivery

1. O usuário faz um pedido  
2. O pedido vai para a **fila RabbitMQ** no **localhost:15672**  
3. O entregador consome o pedido da fila  
4. O pedido é entregue e marcado como concluído  

---

## 🔹 Pré-requisitos

- Python 3 instalado  
- RabbitMQ rodando no **localhost:15672** (local ou via Docker)  
- Biblioteca Python `pika` instalada:
```bash
pip install pika

# 🔹 Conceitos Aprendidos:

Fila de mensagens: comunicação assíncrona entre sistemas

Produtor: envia mensagens para a fila

Consumidor: processa mensagens da fila

RabbitMQ localhost: broker confiável e escalável

Assíncrono: permite múltiplos consumidores processando pedidos sem bloquear o sistema

## 🔹 Executando a Aplicação:

 Com o Docker Instalado na sua maquina você vai rodar o comando que vai acrescentar a imagem 
 do RabbitMQ 

1 - docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
2 - Executar os arquivos:
    python entrega.py 
    python pedido.py



