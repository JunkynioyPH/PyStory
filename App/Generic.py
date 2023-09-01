import os, time, rich, sys, json
import App.AudSys as AudSys
from rich.console import Console
from App.MessageBox import MsgBox
console = Console()

class cmdline:
    def clearscreen():
        os.system('cls' if os.name=='nt' else 'clear')

    def printmd(String, end=''):
        rich.print(String, end=f"{end}", flush=True)
    
    # this is so scuffeds
    # https://stackoverflow.com/questions/28802417/how-to-count-lines-in-multi-lined-strings
    #
    #
    #
    # ** then print out each item in list then remove unformatted then print out formatted item
    # implement deleting 1 character at a time instead of a full line [apr 7 2023]
    #
    # when char is undefined, omit <{char}>
    #
    # dialog(char="test", str="poggers") \n dialog(str="poggers" richmd="")
    #

    def dialog(char="", str="", dur=60, newline=0, bkspc=0, richmd="", voice=''):
        debug = 1
        if newline < 1 and bkspc < 1:
            print() if char != "" == richmd else ""
            # raw = f"<{char}> " + str if char != "" else str
            strbuffer = str.split()
            charbuffer = f"<{char}>"
            if char != "":
                for letter in charbuffer:
                    cmdline.printmd(letter)
                    time.sleep(float(dur)/1000)
                print()
                cmdline.printmd(f"\x1b[1A\x1b[2K<{char}>  ") ## issue in windows terminal
            # for each word in buffer
            for word in strbuffer:
                letter = 1
                ## for each letter in word
                while letter <= len(word):
                    _ = word[letter-1:letter]
                    cmdline.printmd(_)
                    letter += 1
                    try:
                        if word[letter-1] == "." and word[letter-2] != ".":
                            cmdline.printmd("[green].[/green]") if debug == 1 else ''
                            pass
                    except:
                        if _ == "." and richmd == "":
                            print()
                            cmdline.printmd(f"[yellow]<{_}[/yellow][blue]{word[letter-2]}>[/blue]") if debug == 1 else ''
                        else:
                            cmdline.printmd(f"[red]<{_}>[/red]") if debug == 1 else ''
                        pass 
                    time.sleep(float(dur)/1000)
                print('\b \b'*len(word), end="", flush=True) if richmd != "" else ""
                cmdline.printmd(f"[{richmd}]{word}[/{richmd}]") if richmd != "" else ""
                cmdline.printmd(" ")
            pass
        elif newline >= 1 and bkspc < 1:
            cmdline.printmd('\n'*newline)
        elif bkspc >= 1 and newline < 1:
            for _ in range(bkspc+1):
                print('\b \b', end="", flush=True)
                # sys.stdout.write("\010")
                # cmdline.printmd('\010')
                time.sleep(float(dur)/1000)
        else:
            cmdline.printmd("[red]You cannot use both \[newline] and \[bkspc] in dialog...[/red] [yellow]u dum? :clown:[/yellow]")
    
    # repurposed for JUST rendering on screen graphics art/menus unless until further notice
    def rendertxt(char='', str='', dur=60, newline=0):
        if newline < 1:
            line_count = len(list(str.split('\n')))
            full_str = f"[{char}]  {str}" if char != "" else ""
            letter = 1
            for letter in full_str:
                cmdline.printmd(letter)
                time.sleep(float(dur)/1000)
            print()
            cmdline.printmd(f"\x1b[1A\x1b[2K"*line_count + full_str) ## issue in windows terminal
        else:
            cmdline.printmd('\n'*newline)


def wait(Duration, msg=False,):
    # Integer or Float.
    if msg == False:
        time.sleep(Duration)
    else:
        print()
        cmdline.dialog(char='SYSTEM CALL', str=f'Waiting... [{Duration}s]', richmd="yellow")
        cmdline.dialog(newline=1)
        time.sleep(Duration)

def ask(string):
    cmdline.printmd(string)
    return input()


class popup:
    def message(Title, Subtitle, Message, Button="OK", Duration=120):
        TITLE, SUBTITLE, MESSAGE, BUTTON = Title.replace('"','\\"'), Subtitle.replace('"','\\"'), Message.replace('"','\\"'), Button.replace('"','\\"')
        MsgBox(TITLE, SUBTITLE, MESSAGE, BUTTON, Duration)

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
