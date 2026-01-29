import App.CrossAppHelper as Comms
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication
from PyQt6.QtMultimedia import QMediaDevices
from App import AudioSystem_PyQt6 as AudioEngine
import sys

## Gemini assisted because i also have no idea how to threading
# but i managed to figure out that the ServerHost is blocking QT from
# loading the audio file so no audio is being played
# i might be able to modularise this ServerWorker and QThread stuff

# 1. Create a Worker class for the Server
class ServerWorker(QObject):
    connectionClosed = pyqtSignal()  # Signal to notify the main thread
    def __init__(self, host_obj, parser_func):
        super().__init__()
        self.host_obj = host_obj
        self.parser_func = parser_func

    def run(self):
        # This blocks, but it's now in a separate thread!
        print("Server is listening...")
        self.host_obj.serveHost(self.parser_func, False)
        
        print("Server connection closed. Shutting down...")
        self.connectionClosed.emit()
        

def main():
    app = QApplication([]) # Initialize app properly

    # Initialize Audio
    DEVICE = QMediaDevices.defaultAudioOutput()
    audioEngine = AudioEngine.AudioManager(DEVICE)
    outputDevices = QMediaDevices.audioOutputs()
    deviceList = [f'[{outputDevices.index(device)}] {device.description()} \n' for device in outputDevices]

    def parser(data:str):
        data = data.split(':')
        try:
            match data[0]:
                case 'status':
                    # Host.send(audioEngine.status(False))
                    return audioEngine.status(False)
                    
                case 'volume':
                    type, volume = data[1:len(data)]
                    audioEngine.setVolume(type, float(volume))
                    return audioEngine.settings.get('volume')
                
                case 'setDevice':
                    device = outputDevices[int(data[1])]
                    audioEngine.setDevice(device)
                    return f"Device set to <{device.description()}>"
                
                # Impossible unless re-written this whole script to use QT Signals and or QT TCP stuff, which tbh might be better
                # Impossible because "QTimers cannot be started from another thread."
                case 'mediaPos':
                    index = int(data[1])
                    return audioEngine.audioMediaPos(index)
                
                case 'listDevices':
                    dataFormatted = ''.join(deviceList)
                    return dataFormatted # Host.send(dataFormatted) # fancy return
                        
                case 'audioIndex':
                    optype, type, path  = data[1:len(data)]
                    
                    if optype.lower() not in ('add', 'remove'):
                        print(f'Unknown "{optype}"')
                        return 'Neither add/remove.'
                    
                    if optype.lower() == 'add':
                        audioEngine.addIndex(type, path)
                        return f'<{path}> inserted into index {type}'
                    else:
                        audioEngine.removeIndex(type, path)
                        return f'<{path}> popped off index {type}'
                    
                case 'toggle':
                    match data[1].lower():
                        case 'audioloop':
                            audioEngine.toggleState('audio','loop')
                        case 'audiomulti':
                            audioEngine.toggleState('audio','multi')
                        case 'soundloop':
                            audioEngine.toggleState('sound','loop')
                        case 'soundmulti':
                            audioEngine.toggleState('sound','multi')
                        case toggle:
                            return f'Unknown Toggle {toggle}'
                    return f'Toggled {data[1]} : {audioEngine.loopMode}'
                
                case 'play':
                    audioEngine.play(data[1], data[2])
                    return 'Played'
                case unhandled:
                    if unhandled.lower() == 'empty':
                        return 'No Command Provided.'
                    return f'Unhandled data {data}'
        except ValueError:
            return 'Not enough Arguments'
        
        del data
    
    # 2. Setup Networking in a Thread
    Host = Comms.ServerObj('127.0.2.1', 2222, 'AudioEngine')
    
    server_thread = QThread()
    worker = ServerWorker(Host, parser)
    worker.moveToThread(server_thread)
    worker.connectionClosed.connect(app.quit)
    
    # Start the server logic when the thread starts
    server_thread.started.connect(worker.run)
    server_thread.start()

    # 3. Start the Qt Event Loop
    # This thread stays responsive for the AudioEngine
    sys.exit(app.exec())


main()
