import os, time, rich, json
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
    os.system(f'.\App\MessageBox.pyw "{TITLE}" "{SUBTITLE}" "{MESSAGE}" {Duration} "{BUTTON}"')

def SystemMsg(Type, Message, Sfx=''):
    Type = Type.lower()
    match Type:
        case "warning": 
            AudSys.SoundFX(filename='ErrExclamation.wav').Play()
            MessageBox('System','Warning',f"{Message}")
        case "critical":
            AudSys.SoundFX(filename='ErrCritStop.wav').Play()
            MessageBox('System','Critical',f"{Message}")
        case "question":
            AudSys.SoundFX(filename='ErrQuestion.wav').Play()
            MessageBox('System','Question',f"{Message}")
        case "neutral":
            AudSys.SoundFX(filename='ErrAsterisk.wav').Play()
            MessageBox('System','Information',f"{Message}")
        case _:
            MessageBox('System','Message',f"{Message}")

def ImageBox():
    print('work in progress')

def printmd(String):
    rich.print(String)

# perform loading save data (which chapter, perhaps where in the chapter(might add a counter for that), reputation for each character)
# show loading screen showing a list of save-SaveName.json files in SAVES folder

## MENUSCREENS.PY MIGHT RENDER THIS NOT REQUIRED.
def Settings():
    print('Settings Shown')

def LoadFile():
    print('File loaded')

def SaveFile():
    print('File Saved')

def NewGame():
    print('New game, new name')
