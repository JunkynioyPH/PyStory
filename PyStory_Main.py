import os
from rich import pretty
from App.Core import console
import App.Core as Core
import App.Extra as Extra
pretty.install()

# # https://stackoverflow.com/questions/64376497/disable-resizing-for-python-console-application-in-windows
# def lock_resize():
#     while True:
#         os.system('mode con cols=210 lines=45')
# # threading.Thread(target=lock_resize(), args=(1,), daemon=True).start()
# _thread.start_new_thread(lock_resize,()) #using the _thread module to keep everything else running
#
# I Guess I know how to Multithread now, i guess. or atleast i know how to start one

Core.cli.clear()
if os.name=='nt':
    os.system('title PyStory - Junkynioy#2408')
    os.system('mode con cols=210 lines=45') # does not work with w11 terminal
else:
    Core.cli.printmd("\n[green]PyStory - Junkynioy#2408[/green]\n")

# Settings(): function, Perhaps use JSON

def splash():
    # FONT SIZE : 16
    # FONT      : Cascadia
    splashText = """
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████    ▄▄▄█████▓ ██▓▄▄▄█████▓ ██▓    ▓█████
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▓  ██▒ ▓▒▓██▒▓  ██▒ ▓▒▓██▒    ▓█   ▀
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒ ▓██░ ▒░▒██▒▒ ▓██░ ▒░▒██░    ▒███
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ░ ▓██▓ ░ ░██░░ ▓██▓ ░ ▒██░    ▒▓█  ▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒     ▒██▒ ░ ░██░  ▒██▒ ░ ░██████▒░▒████▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░     ▒ ░░   ░▓    ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░       ░     ▒ ░    ░    ░ ░ ▒  ░ ░ ░  ░
░ ░   ░   ░   ▒   ░      ░      ░        ░       ▒ ░  ░        ░ ░      ░
      ░       ░  ░       ░      ░  ░             ░               ░  ░   ░  ░
http://www.patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Game%20Title\n"""
    Core.cli.printmd(splashText)

def gameinit():
    global menuloop
    # load volume from settings
    # Core.LoadSave() somewhere in the main menu

    # AudSys: change samplerate to 48000 or whatever, cuz it defaults to like 41000 and i can hear sus crackle noises
    Core.AudSys.audiosysteminit(25*0.50) # 25% == 100%
    menuloop = True

    # use [['text1'],[text2]] .py list for Dialogues
    # ChapterX.py which contains a list of dialogue for that chapter

def selection(Option):
    global menuloop
    match Option:
        case 1:
            Core.cli.clear()
            Core.NewGame()
        case 2:
            Core.cli.clear()
            Core.LoadFile()
        case 3:
            Core.cli.clear()
            Core.Settings()
        case 4:
            if Core.ask('[yellow]Are you[/yellow] [green]Sure?[/green] [[green]y[/green]/[red]n[/red]] [pink]>>[/pink] ').lower() == 'y':
                menuloop = False
            else:
                Core.cli.clear()
                print('Returning to Menu')
                splash()
        case _:
            Core.cli.clear()
            splash()
            console.log("Invalid Selection!", highlight=True)

def gameloop():
    global menuloop
    while menuloop:
        if Core.AudSys.audio.music.get_busy() == True:
            pass
        else:
            Core.AudSys.music.load("Dark-main-menu-song-REV1.ogg", True)
        MainMenu =  """
                    [bold green][1] New Game[/bold green]
                    [bold yellow][2] Load Game[/bold yellow]
                    [bold blue][3] Settings[/bold blue]
                    [bold red][4] Exit[/bold red]
                    \n"""
        # printmd(f"[italic red]{MainMenu}[/italic red] Poggers")

        # Print()
        console.log("Core.AudSys.audio.music.get_busy() is " + str(Core.AudSys.audio.music.get_busy())) ####
        Core.cli.rendertxt(title="[bright_cyan]Select[/bright_cyan] an [bright_blue]option[/bright_Blue]",str=MainMenu, dur=0.5)
        ans = Core.ask('                    >>  ')
        # Extra.Fun(selection) is for funny
        Extra.Fun(ans)
        try:
            selection(int(ans))
        except Exception as ERR:
            Core.cli.clear()
            console.log(f'{ERR}')
            splash()

    # then the game stuff initialises here


# Game will be based on a reputation system, reputation of the player to each character introduced.

# Use json for saving reputation in Global Use inside .\Assets\GlobalVariables
# instead of the above use of json for reputation, create some sort of json save-file format for saving
# data, and use a separate folder in .\Assets for loading in saves to keep the saves un-altered unless
# the player saved the game

# create a separate .py file to display images perhaps using tkinter's GUI !

splash()
gameinit()

gameloop()

Core.cli.printmd("[red]Game Closed[/red]")
Core.wait(2)
