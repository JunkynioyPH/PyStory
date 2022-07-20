import os, time, rich
import App.AudSys as AudSys
from rich.console import Console
console = Console()

def Wait(Duration):
    # Integer or Float.
    time.sleep(Duration)

def ClearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def MessageBox(Title, Subtitle, Message, Button="OK", Duration=120):
    TITLE, SUBTITLE, MESSAGE, BUTTON = Title.replace('"','\\"'), Subtitle.replace('"','\\"'), Message.replace('"','\\"'), Button.replace('"','\\"')
    os.system(f'python .\App\MessageBox.pyw "{TITLE}" "{SUBTITLE}" "{MESSAGE}" {Duration} "{BUTTON}"')

def SystemMsg(Type, Message, Sfx=''):
    Type = Type.lower()
    match Type:
        case "warning":
            AudSys.AudioSoundPlay('ErrExclamation.wav')
            MessageBox('System','Warning',f"{Message}")
        case "critical":
            AudSys.AudioSoundPlay('ErrCritStop.wav')
            MessageBox('System','Critical',f"{Message}")
        case "question":
            AudSys.AudioSoundPlay('ErrQuestion.wav')
            MessageBox('System','Question',f"{Message}")
        case "neutral":
            AudSys.AudioSoundPlay('ErrAsterisk.wav')
            MessageBox('System','Information',f"{Message}")
        case _:
            MessageBox('System','Message',f"{Message}")

def ImageBox():
    print('work in progress')

def printmd(String):
    rich.print(String)

def Settings():
    print('Settings Shown')

# perform loading save data (which chapter, perhaps where in the chapter(might add a counter for that), reputation for each character)
# show loading screen showing a list of save-SaveName.json files in SAVES folder
def LoadFile():
    print('File loaded')

def SaveFile():
    print('File Saved')

def NewGame():
    print('New game, new name')
