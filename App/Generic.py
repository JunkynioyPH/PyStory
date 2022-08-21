import os, time, rich, json
import App.AudSys as AudSys
from rich.console import Console
console = Console()

def wait(Duration):
    # Integer or Float.
    time.sleep(Duration)

def clearscreen():
    os.system('cls' if os.name=='nt' else 'clear')

def printmd(String):
    rich.print(String)

def ask(string):
    printmd(string)
    return input()

class popup:
    def message(Title, Subtitle, Message, Button="OK", Duration=120):
        TITLE, SUBTITLE, MESSAGE, BUTTON = Title.replace('"','\\"'), Subtitle.replace('"','\\"'), Message.replace('"','\\"'), Button.replace('"','\\"')
        os.system(f'.\App\MessageBox.pyw "{TITLE}" "{SUBTITLE}" "{MESSAGE}" {Duration} "{BUTTON}"')

    def system(Type, Message, Sfx=''):
        Type = Type.lower()
        match Type:
            case "warning": 
                AudSys.soundfx.play('ErrExclamation.wav')
                popup.message('System','Warning',f"{Message}")
            case "critical":
                AudSys.soundfx.play('ErrCritStop.wav')
                popup.message('System','Critical',f"{Message}")
            case "question":
                AudSys.soundfx.play('ErrQuestion.wav')
                popup.message('System','Question',f"{Message}")
            case "neutral":
                AudSys.soundfx.play('ErrAsterisk.wav')
                popup.message('System','Information',f"{Message}")
            case _:
                AudSys.soundfx.play(Sfx)
                popup.message('System','Message',f"{Message}")

    def image():
        print('work in progress')

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
