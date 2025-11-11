import socket, os, time
# import App.xpfpath as xpfpath
os.system('title "Junkynioy#2408 SERVER"')

class HostObj():
    def __init__(self, hostAddr='', port=0, name=''):
        # use 127.0.0.1 if no host address is specified
        self.host = socket.gethostbyname(socket.gethostname()) if hostAddr == '' else hostAddr
        # Port to listen on (non-privileged ports are > 1023)
        # use default Port 1024 if no port specified
        self.port = 1024 if port < 1024 else port
        self.name = f'{self.host}:{self.port}' if name == '' else name
        
        self.connection:socket.socket|None = None
        self.clientAddr:socket._RetAddress|None = None
        
    def start(self):
        print(f'\nHost [{self.host}:{self.port}]\nAwaiting Client...')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen()
        self.connection, self.clientAddr = s.accept()
        print(f"Connection Established by {self.clientAddr}")
    
    def reset(self):
        self.connection.shutdown(2)
        self.connection.close()
        self.start()
    
    def serveHost(self, callableFunc):
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
                            print('Lost Connection: Awaiting reconnection.')
                            self.reset()
                            break
                        # print(f"{self.clientAddr} Data: {Message if Message != '' else 'None'}")
                        self.connection.sendall(bytes(f'[{self.name}] Ack: {callableFunc(Message)}','utf-8'))
                    except Exception as ERR:
                        print(f"\nFatalError: {repr(ERR)}\nException: Attempt Host reset.")
                        self.reset()
                        break

if __name__ == '__main__':
    def parser(data:str):
        data = data.split(':')
        try:
            match data[0].lower():
                case 'empty':
                    print('empty command.')
                    return 'no command supplied.'
                case 'audio':
                    print(f'parsing command audio: adding {data[1]} to audio index')
                    return f'parsing command audio: adding {data[1]} to audio index'
                case _:
                    print(f'Unhandled Command, "{data[0]}"')
        except IndexError:
            print('no syntax provided.')
            
    
    Host = HostObj('127.0.1.1',2222,'AudioEngine')
    Host.start()
    Host.serveHost(parser)