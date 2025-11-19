import socket, os, time, sys
from App.Core import Common
# import App.xpfpath as xpfpath

class ServerObj():
    def __init__(self, hostAddr='', port=0, name=''):
        # use 127.0.0.1 if no host address is specified
        self.host = socket.gethostbyname(socket.gethostname()) if hostAddr == '' else hostAddr
        # Port to listen on (non-privileged ports are > 1023)
        # use default Port 1024 if no port specified
        self.port = 1024 if port < 1024 else port
        self.name = f'{self.host}:{self.port}' if name == '' else name
        
        self.connection:socket.socket|None = None
        self.clientAddr:socket._RetAddress|None = None
        
        self.cli = Common.Character(f"[{self.name}]",20)
        
    def start(self):
        self.cli.say("Awaiting Client...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen()
        self.connection, self.clientAddr = s.accept()
        self.cli.say(f"Connection Established by {self.clientAddr}")
    
    def reset(self):
        self.connection.shutdown(2)
        self.connection.close()
        self.start()
        
    def send(self, data:str):
        self.cli.say(f"Replying with data: {data}",0.1)
        self.connection.sendall(bytes(data,'utf8'))
    
    def serveHost(self, callableFunc, reconnect:bool=True):
        while True:
            with self.connection:
                # print(f'with {host.connection}:')
                # nested While loops looks so terrible
                while True:
                    try:
                        data = self.connection.recv(1024)
                        Message = data.decode('utf-8')
                        Message = Message.replace('"','\\"')
                        if not data:
                            self.cli.say('Lost Connection: Awaiting reconnection.')
                            self.reset()
                            break
                        elif not data and reconnect == False:
                            self.cli.say(f'Lost Connection to {self.clientAddr}! Aborting.')
                            Common.wait(2)
                            sys.exit()
                        print(f"{self.clientAddr} Data: {Message if Message != '' else 'None'}")
                        # message client back
                        self.connection.sendall(bytes(f'[{self.name}] Reply: {callableFunc(Message)}','utf-8'))
                    except Exception as ERR:
                        self.cli.say(f"{repr(ERR)}\nException: Attempt Host reset.")
                        self.reset()
                        break

class ClientObj():
    def __init__(self, hostAddr='', port=0, name=''):
        # use 127.0.0.1 if no host address is specified
        self.host = socket.gethostbyname(socket.gethostname()) if hostAddr == '' else hostAddr
        # Port to listen on (non-privileged ports are > 1023)
        # use default Port 1024 if no port specified
        self.port = 1024 if port < 1024 else port
        self.name = f'{self.host}:{self.port}' if name == '' else name
        
        self.cli = Common.Character(f"[{self.name}]",20)
        
    def start(self):
        while True:
            try:
                print()
            except Exception as ERR:
                self.cli.say(f"{repr(ERR)}\nException: Attempt Host reset.")
    
    def sendMessage(self):
        ...