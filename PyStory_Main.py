import os
from rich import pretty
from App.Generic import console
import App.Generic as Generic
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

Generic.cmdline.clearscreen()
if os.name=='nt':
    os.system('title PyStory - Junkynioy#2408')
    os.system('mode con cols=210 lines=45') # does not work with w11 terminal
else:
    Generic.printmd("\n[green]PyStory - Junkynioy#2408[/green]\n")

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
    Generic.cmdline.printmd(splashText)

def gameinit():
    global menuloop
    # load volume from settings
    # Generic.LoadSave() somewhere in the main menu
    Generic.AudSys.audiosysteminit(25*0.50) # 25% == 100%
    menuloop = True

    # use [['text1'],[text2]] .py list for Dialogues
    # ChapterX.py which contains a list of dialogue for that chapter

def selection(Option):
    global menuloop
    match Option:
        case 1:
            Generic.cmdline.clearscreen()
            Generic.NewGame()
        case 2:
            Generic.cmdline.clearscreen()
            Generic.LoadFile()
        case 3:
            Generic.cmdline.clearscreen()
            Generic.Settings()
        case 4:
            if Generic.ask('[yellow]Are you[/yellow] [green]Sure?[/green] [[green]y[/green]/[red]n[/red]] [pink]>>[/pink] ').lower() == 'y':
                menuloop = False
            else:
                Generic.cmdline.clearscreen()
                print('Returning to Menu')
                splash()
        case _:
            Generic.cmdline.clearscreen()
            splash()
            console.log("Invalid Selection!", highlight=True)

def gameloop():
    global menuloop
    while menuloop:
        if Generic.AudSys.audio.music.get_busy() == True:
            pass
        else:
            Generic.AudSys.music.load("Dark-main-menu-song-REV1.ogg", True)
        MainMenu =  """
                    [bold green][1] New Game[/bold green]
                    [bold yellow][2] Load Game[/bold yellow]
                    [bold blue][3] Settings[/bold blue]
                    [bold red][4] Exit[/bold red]
                    \n"""
        # printmd(f"[italic red]{MainMenu}[/italic red] Poggers")

        # Print()
        console.log("Generic.AudSys.audio.music.get_busy() is " + str(Generic.AudSys.audio.music.get_busy())) ####
        Generic.cmdline.rendertxt(title="[bright_cyan]Select[/bright_cyan] an [bright_blue]option[/bright_Blue]",str=MainMenu, dur=0.5)
        ans = Generic.ask('                    >>  ')
        # Extra.Fun(selection) is for funny
        Extra.Fun(ans)
        try:
            selection(int(ans))
        except Exception as ERR:
            Generic.cmdline.clearscreen()
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

Generic.cmdline.printmd("[red]Game Closed[/red]")
Generic.wait(2)
