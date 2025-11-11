# to be reworked as a class and migrated to CrossAppComms.py
# currently this is NOT CLOSING any connections.
import socket, os, time
os.system('title "Junkynioy#2408 CLIENT"')

HOST = input("\nIP > ")  # HOST IP or HOSTNAME (e.g. 127.0.0.1 or host.name.com)
PORT = int(input("\nPort > "))  # The port used by the server

def Connect():
    try:
        print(f"Connecting to {HOST}:{PORT}...")
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        os.system('cls' if os.name=='nt' else 'clear')
        print(f'Connection to {HOST}:{PORT} Established!')
    except Exception as ERR:
        print(ERR)
        time.sleep(0.8)
        Connect()
    return

def Text():
    global Message
    Message = input("\nMessage > ")
    if Message == '':
        Message = 'Empty'
    try:
        s.sendall(bytes(Message, 'utf-8')) # Error when sending to an already connected adress but reciever is not active ????????????
    except:
        print(f'Lost Connection to {HOST}:{PORT}')
        Connect()
        Text()

Connect()

while True:
    time.sleep(0.25)
    Text()
    data = s.recv(1024)
    print(data.decode())
    # time.sleep(1)
