import socket, os, time, sys, socket
from App.Core import Common, Cli
# import App.xpfpath as xpfpath

###
## Gemini Optimised
###
# Im not familiar with these type of stuff
# but i did got it to work the first time
## See ./App/OLD_SOURCE
# i just cbf to look through docs on how to 
# properly handle edge cases and i want
# to move on and get some progress done
class ServerObj():
    def __init__(self, hostAddr='', port=0, name=''):
        # Dynamic hostname lookup or override
        self.host = socket.gethostbyname(socket.gethostname()) if hostAddr == '' else hostAddr
        self.port = 1024 if port < 1024 else port
        self.name = f'{self.host}:{self.port}' if name == '' else name
        
        self.listener = None
        self.connection = None
        self.clientAddr = None
        self.cli = Common.Character(f"[{self.name}]", 5, True)

    def _init_listener(self):
        """Initializes the listener socket with local-safety flags."""
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Allow immediate reboot of the script without 'Address already in use'
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Windows-specific fix for rapid local restarts
        if sys.platform == 'win32':
            self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 0)
            
        self.listener.bind((self.host, self.port))
        self.listener.listen(1) # Allow a small backlog of local connections
        self.cli.say(f"Listening on {self.host}:{self.port} ({self.name})")

    def serveHost(self, callableFunc, reconnect: bool = True):
        """Main loop that survives client disconnects without recursion."""
        self._init_listener()
        
        try:
            while True:
                self.cli.say("Awaiting Local Client...")
                self.connection, self.clientAddr = self.listener.accept()
                
                with self.connection:
                    self.cli.say(f"Connection from {self.clientAddr}")
                    while True:
                        try:
                            data = self.connection.recv(1024)
                            if not data: 
                                self.cli.say(f"Client Disconnected")
                                break # Client closed gracefully
                            
                            message = data.decode('utf-8').replace('"', '\\"')
                            self.cli.say(f"Data: {message}")
                            # Process and reply
                            result = callableFunc(message)
                            response = f'[{self.name}] Reply: {result}'
                            self.cli.say(f"{result}")
                            self.connection.sendall(response.encode('utf-8'))
                            
                        except (ConnectionResetError, BrokenPipeError):
                            self.cli.say("Client Abruptly Disconnected")
                            break
                
                # Cleanup reference for the next loop
                self.connection = None
                if not reconnect:
                    self.cli.say(f"Reconnect is disabled")
                    break
                    
        finally:
            if self.listener:
                self.listener.close()

class ClientObj():
    def __init__(self, hostAddr='', port=0, name=''):
        self.host = socket.gethostbyname(socket.gethostname()) if hostAddr == '' else hostAddr
        self.port = 1024 if port < 1024 else port
        self.name = f'{self.host}:{self.port}' if name == '' else name
        
        self.conn = None
        self.cli = Common.Character(f"[{self.name}]", 5, True)

    def _ensure_connection(self):
        """Internal helper to connect if the socket is dead."""
        if self.conn is None:
            try:
                self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Local connections should be nearly instant
                self.conn.settimeout(2.0)
                self.conn.connect((self.host, self.port))
                self.conn.settimeout(None) # Reset to blocking
                return True
            except (ConnectionRefusedError, socket.timeout):
                self.cli.say("Connection Failed: Server not ready.")
                self.conn = None
                return False
        return True

    def send(self, data: str):
        """Sends a message and waits for the reply."""
        if not self._ensure_connection():
            return None
            
        try:
            self.cli.say(f"Sending: {data}", 0.1)
            self.conn.sendall(data.encode('utf-8'))
            
            reply = self.conn.recv(1024)
            if not reply:
                self.cli.say("Server closed connection.")
                self.conn = None
                return None
                
            return Cli(reply.decode('utf-8')).print(True)
            
        except (ConnectionResetError, BrokenPipeError):
            self.cli.say("Lost connection during send. Resetting...")
            self.conn = None
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None