# from PyQt6.QtCore import QObject, pyqtSignal
# from PyQt6.QtNetwork import QTcpSocket

# class ClientWorkerObject(QObject):
#     read_finished = pyqtSignal()
#     data_received = pyqtSignal(str)
#     connection_info = pyqtSignal(str)
#     def __init__(self, dataParser, hostAddress:str):
#         super().__init__()
#         self.processor = dataParser
#         self.ip, self.port = tuple(hostAddress.split(':'))
#         self.port = int(self.port)
        
#         self.socket = QTcpSocket()
#         self.socket.readyRead.connect(self.read)
#         self.socket.connectToHost(self.ip, self.port)
#         # self.socket.hostFound.connect()
#         # self.socket.connected.connect()
#         # self.socket.disconnected.connect()
#         # self.socket.errorOccurred.connect()
#         # self.socket.stateChanged.connect()
#     def read(self):
#         self.connection_info.emit(self.socket)
#         with self.socket.bytesAvailable():
#             data = self.socket.readAll().data().decode()
#             self.processor(data)
#             self.data_received.emit(data)
#         self.read_finished.emit()
        
# if __name__ == '__main__':
#     from PyQt6.QtWidgets import QApplication
#     app = QApplication([]) # Initialize app properly
    
#     # start a client
#     while True:
#         Client = ClientWorkerObject(print,'127.0.0.1:2222')
#         Client.connection_info.connect(lambda info: print(info))
#         Client.read_finished.connect(lambda: print('read OK'))
#         Client.data_received.connect(lambda data: print(f'data OK: {data}'))