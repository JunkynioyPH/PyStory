import os
from rich import pretty
from App.Generic import console
import App.Generic as Generic
import App.Extra as Extra
pretty.install()

Generic.cmdline.clearscreen()
if os.name=='nt':
    os.system('title PyStory - Junkynioy#2408')
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
http://www.patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Game%20Title"""
    Generic.cmdline.printmd(splashText)

def gameinit():
    global menuloop
    # load volume from settings
    # Generic.LoadSave() somewhere in the main menu
    Generic.AudSys.audiosysteminit(25) # 25%
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
            # Send any number/string in the Main Menu to trigger this test
            Generic.cmdline.dialog('this is a testing typing string!',25)
            Generic.popup.system('warning','Poggers')
            Generic.popup.system('critical','Poggers')
            Generic.popup.system('question','Poggers')
            Generic.popup.system('neutral','Poggers')

def gameloop():
    global menuloop
    while menuloop:
        if Generic.AudSys.audio.music.get_busy() == True:
            pass
        else:
            Generic.AudSys.music.load("Dark-main-menu-song-REV1.ogg", True)
        MainMenu =  """
                            [green][1] New Game[/green]
                            [yellow][2] Load Game[/yellow]
                            [blue][3] Settings[/blue]
                            [red][4] Exit[/red]
                    \n"""
        # printmd(f"[italic red]{MainMenu}[/italic red] Poggers")
        try:
            print()
            console.log("Generic.AudSys.audio.music.get_busy() is " + str(Generic.AudSys.audio.music.get_busy()))
            Generic.cmdline.dialog(MainMenu, 5, "multi")
            Generic.cmdline.dialog('this is also vert poggers testing a string render thing',50)
            ans = input('\n>> ')
            # Extra.Fun(selection) is for funny
            Extra.Fun(ans)
            selection(int(ans))
        except Exception as ERR:
            Generic.cmdline.clearscreen()
            console.log(ERR)
            splash()
    # then the game stuff initialises here


# Game will be based on a reputation system, reputation of the player to each character introduced.

# Use json for saving reputation in Global Use inside .\Assets\GlobalVariables
# instead of the above use of jeson for reputation, create some sort of json save-file format for saving
# data, and use a separate folder in .\Assets for loading in saves to keep the saves un-altered unless
# the player saved the game

# create a separate .py file to display images perhaps using tkinter's GUI !

splash()
gameinit()

gameloop()

Generic.cmdline.printmd("[red]Game Closed[/red]")
Generic.wait(2)
