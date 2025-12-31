import socket
import argparse
import requests
import threading

parser = argparse.ArgumentParser()

parser.usage = "TODO"

parser.add_argument("mode", help="TODO", choices=["start", "connect"])
parser.add_argument("--ip", help="TODO", default="0.0.0.0")
parser.add_argument("--port", help="TODO", default="1010")
parser.add_argument("--nickname", help="TODO", default="user")

args = parser.parse_args()

def print_recived_mess(client, nickname):
    while True:
        print("<"+nickname+">", client.recv(1024).decode())

print(" __  __   __ __   __ __   __  ")
print("|   |  | |  |  | |  |  | |__  ")
print("|   |  | |  |  | |  |  |    | ")
print("|__ |__| |  |  | |  |  |  __| ")

print("Thank you for using comms project!")

if args.mode == "start":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((args.ip, int(args.port)))

    public_ip_url = "https://checkip.amazonaws.com"
    response = requests.get(public_ip_url)
    public_ip = response.text

    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)

    print("The current public ip is,", public_ip, ", or if the computers are in the same network then the private ip is,", private_ip, " and the port is,", args.port)

    server.listen(1)

    client, adress = server.accept()

    client.send(args.nickname.encode())
    client_nickname = client.recv(1024).decode()
    print("connected to ",client_nickname)

    while True:  
        thread = threading.Thread(target=print_recived_mess, args=(client, client_nickname), daemon=True)
        thread.start()
        message = input()
        client.send(message.encode())

if args.mode == "connect":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((args.ip, int(args.port)))

    server_nickname = client.recv(1024).decode()
    client.send(args.nickname.encode())
    print("connected to ",server_nickname)

    while True:
        thread = threading.Thread(target=print_recived_mess, args=(client, server_nickname), daemon=True)
        thread.start()
        message = input()
        client.send(message.encode())