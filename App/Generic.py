import os, time, rich, sys, json
import App.AudSys as AudSys
from rich.console import Console
console = Console()

class cmdline:
    def clearscreen():
        os.system('cls' if os.name=='nt' else 'clear')

    def printmd(String, end=''):
        rich.print(String, end=f"{end}")
    
    # this is so scuffeds
    #
    # implement this counting thing:
    # https://stackoverflow.com/questions/28802417/how-to-count-lines-in-multi-lined-strings
    #
    def dialog(char='', str='', dur=60, spc=0):
        if spc < 1:
            line_count = len(list(str.split('\n'))) - 2
            full_str = f"<{char}>  {str}"
            letter = 1
            while letter <= len(str):
                new_str = full_str[letter-1:letter]
                cmdline.printmd(new_str)
                sys.stdout.flush()
                letter += 1 
                time.sleep(float(dur)/1000)
            cmdline.printmd(line_count)

            # might be able to be written better with code below:
            # print('\b' * len(positionStr), end='', flush=True)
            sys.stdout.write('\r\x1b[1A\x1b[2K' * line_count) if line_count != -1 else sys.stdout.write('\r\x1b[2K') # \x1b[2K == delete \x1b[1A == UP ARROW ---- \r\x1b[2K
            ##

            cmdline.printmd(f"\r{full_str}") if line_count != -1 else cmdline.printmd(f"\r{full_str}\n")
        else:
            cmdline.printmd('\n'*spc)


def wait(Duration, msg=False,):
    # Integer or Float.
    if msg == False:
        time.sleep(Duration)
    else:
        cmdline.dialog(char='SYSTEM CALL', str=f'Waiting... [{Duration}s]')
        cmdline.dialog(spc=1)
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
