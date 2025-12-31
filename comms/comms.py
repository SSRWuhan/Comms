import socket
import argparse
import requests
import threading

parser = argparse.ArgumentParser()

parser.usage = "Comms is a terminal based program made for communication between 2 computers."

parser.add_argument("mode", help="select which option you want to start Comms in. Start initializes a server for the other person to connect to and connect allows you to connect to a existing server. When starting a server the --ip and --port can be left to the default values unless change is wanted. But, they are absolutely needed for when connecting.", choices=["start", "connect"])
parser.add_argument("--ip", help="Sets the ip address to use. Defaults to 0.0.0.0", default="0.0.0.0")
parser.add_argument("--port", help="Sets the port to use. Defaults to 1010", default="1010")
parser.add_argument("--nickname", help="Sets the nickname to use. Defaults to user", default="user")

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