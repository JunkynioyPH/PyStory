import App.CrossAppComms as Comms
from PyQt6.QtWidgets import QApplication
from PyQt6.QtMultimedia import QMediaDevices
from App import AudioSystem_PyQt6 as AudioEngine

APP = QApplication([]) # Mandatory.
DEVICE = QMediaDevices.defaultAudioOutput()
audioEngine = AudioEngine.AudioManager(DEVICE)

    # Core.audioEngine.addIndex('audio','./Assets/Audio/Music/mainMenu.ogg')
    # Core.audioEngine.toggleState('audio','loop')
    # Core.audioEngine.play('audio','mainMenu')

def parser(data:str):
    data = data.split(':')
    try:
        try: data[1] = data[1].lower() 
        except: pass
        
        match data[0]:
            case 'empty':
                print('Empty command.')
                return 'no command supplied.'
            case 'status':
                Host.send(audioEngine.status(False))
            case 'volume':
                type, volume = data[1:len(data)]
                if type not in ('audio','sound'):
                    return "Unknown Type"
                audioEngine.setVolume(type, float(volume))
                print(audioEngine.settings.get('volume'))
                del type, volume
                    
            case 'audioIndex':
                optype, type, path  = data[1:len(data)]
                if optype not in ('add', 'remove'):
                    print(f'unknown "{optype}"')
                    return 'neither add/remove.'
                if optype == 'add':
                    audioEngine.addIndex(type, path)
                    return f'{type} < {path} index'
                else:
                    audioEngine.removeIndex(type, path)
                del optype, type, path
                
            case _:
                print(f'Unhandled data, {data}')
                return f'Unhandled, {data}'
    except IndexError:
        print('no syntax provided.')
    del data

Host = Comms.ServerObj('127.0.2.1',2222,'AudioEngine')
Host.start()
Host.serveHost(parser,False)