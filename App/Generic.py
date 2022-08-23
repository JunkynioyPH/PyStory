import os, time, rich, sys, json
import App.AudSys as AudSys
from rich.console import Console
console = Console()

class cmdline:
    def clearscreen():
        os.system('cls' if os.name=='nt' else 'clear')

    def printmd(String):
        rich.print(String, end="")
    
    # this is so scuffed
    #
    # implement this counting thing:
    # https://stackoverflow.com/questions/28802417/how-to-count-lines-in-multi-lined-strings
    #
    def dialog(string, dur=125, how="typing"):
        letter = 1
        while letter <= len(string):
            new_string = string[letter-1:letter]
            cmdline.printmd(new_string)
            sys.stdout.flush()
            letter += 1 
            time.sleep(float(dur)/1000)
        sys.stdout.write('\r\x1b[1A\x1b[2K' * (len(string.split('\n')) - 1)) if how.lower() == "menu" else sys.stdout.write("\r\x1b[2K")
        cmdline.printmd(f"\r{string}")


def wait(Duration):
    # Integer or Float.
    time.sleep(Duration)

def ask(string):
    cmdline.printmd(string)
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
