import socket, time, random

server = socket.socket()
server.bind(("localhost", 7777))
server.listen()

print("Servidor levantado. Esperando conexión en localhost:7777...")

conn, addr = server.accept()
print("Cliente conectado desde:", addr)

try:
    while True:
        temp = random.randint(10, 35)
        msg = f"{temp},{time.time()}"

        print("Enviando:", msg)
        conn.send((msg + "\n").encode())

        time.sleep(1)
except KeyboardInterrupt:
    print("Cerrando servidor...")
    conn.close()
    server.close()