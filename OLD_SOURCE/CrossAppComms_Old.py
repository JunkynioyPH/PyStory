import socket, os, time, sys, struct
from App.Core import Common
# import App.xpfpath as xpfpath
import socket
from App.Core import Common

class ServerObj():
    def __init__(self, hostAddr='127.0.0.1', port=1024, name='Server'):
        self.host = hostAddr
        self.port = port
        self.name = name
        self.listener = None
        self.connection = None
        self.cli = Common.Character(f"[{self.name}]", 20)

    def start(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind((self.host, self.port))
        self.listener.listen(1)
        
    def serve(self, callback):
        self.start()
        while True:
            self.cli.say("Awaiting local client...")
            self.connection, addr = self.listener.accept()
            
            with self.connection: # Auto-closes when loop breaks
                while True:
                    try:
                        data = self.connection.recv(1024)
                        if not data: break # Client disconnected
                        
                        msg = data.decode('utf-8')
                        reply = callback(msg)
                        self.connection.sendall(reply.encode('utf-8'))
                    except (ConnectionResetError, BrokenPipeError):
                        break
            
            self.connection = None # Clear reference
            self.cli.say("Client disconnected. Resetting...")
            
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
    
    def send(self):
        ...