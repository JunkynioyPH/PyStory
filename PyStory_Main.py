import os
from rich import pretty
from App.Generic import console
import App.Generic as Generic
import App.Extra as Extra
pretty.install()

Generic.clearscreen()
os.system('title PyStory - Junkynioy#2408')

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
    print(splashText)

def gameinit():
    global gamelooping
    # load volume from settings
    # Generic.LoadSave() somewhere in the main menu
    Generic.AudSys.audiosysteminit(25) # 25%
    gamelooping = True

    # use [['text1'],[text2]] .py list for Dialogues
    # ChapterX.py which contains a list of dialogue for that chapter

def selection(Option):
    global gamelooping
    match Option:
        case 1:
            Generic.clearscreen()
            Generic.NewGame()
        case 2:
            Generic.clearscreen()
            Generic.LoadFile()
        case 3:
            Generic.clearscreen()
            Generic.Settings()
        case 4:
            if input('Are you Sure? [y/n] >> ').lower() == 'y':
                gamelooping = False
            else:
                Generic.clearscreen()
                print('Returning to Menu')
                splash()
        case _:
            Generic.clearscreen()
            splash()
            # Send any number/string in the Main Menu to trigger this test
            Generic.popup.system('warning','Poggers')
            Generic.popup.system('critical','Poggers')
            Generic.popup.system('question','Poggers')
            Generic.popup.system('neutral','Poggers')

def gameloop():
    global gamelooping
    while gamelooping:
        if Generic.AudSys.audio.music.get_busy() == True:
            console.log("Generic.AudSys.audio.music.get_busy() is " + str(Generic.AudSys.audio.music.get_busy()))
            pass
        else:
            Generic.AudSys.music.load("Dark-main-menu-song-REV1.ogg", True)
        MainMenu = """
                            [green][1] New Game[/green]
                            [yellow][2] Load Game[/yellow]
                            [blue][3] Settings[/blue]
                            [red][4] Exit[/red]
                    """
        # printmd(f"[italic red]{MainMenu}[/italic red] Poggers")
        try:
            Generic.printmd(MainMenu)
            ans = input('>> ')
            # Extra.Fun(selection) is for funny
            Extra.Fun(ans)
            selection(int(ans))
        except Exception as ERR:
            Generic.clearscreen()
            console.log(ERR)
            splash()

# Game will be based on a reputation system, reputation of the player to each character introduced.

# Use json for saving reputation in Global Use inside .\Assets\GlobalVariables
# instead of the above use of jeson for reputation, create some sort of json save-file format for saving
# data, and use a separate folder in .\Assets for loading in saves to keep the saves un-altered unless
# the player saved the game

# create a separate .py file to display images perhaps using tkinter's GUI !

splash()
gameinit()

gameloop()

Generic.printmd("[red]Game Closed[/red]")
Generic.wait(2)
