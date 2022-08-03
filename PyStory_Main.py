import os
from rich import pretty
from App.Generic import console
import App.Generic as Generic
import App.Extra as Extra
pretty.install()

Generic.ClearScreen()
os.system('title PyStory - Junkynioy#2408')

# Settings(): function, Perhaps use JSON

def Splash():
    SplashText = """
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
    print(SplashText)

def GameInit():
    global looping
    # load volume from settings
    # Generic.LoadSave() somewhere in the main menu
    Generic.AudSys.AudioSystemInitialise(25) # 25%
    looping = True

    # use [['text1'],[text2]] .py list for Dialogues
    # ChapterX.py which contains a list of dialogue for that chapter

def Selection(Option):
    global looping
    match Option:
        case 1:
            Generic.ClearScreen()
            Generic.NewGame()
        case 2:
            Generic.ClearScreen()
            Generic.LoadFile()
        case 3:
            Generic.ClearScreen()
            Generic.Settings()
        case 4:
            if input('Are you Sure? [y/n] >> ').lower() == 'y':
                looping = False
            else:
                Generic.ClearScreen()
                print('Returning to Menu')
                Splash()
        case _:
            Generic.ClearScreen()
            Splash()
            # Send any number/string in the Main Menu to trigger this test
            Generic.SystemMsg('warning','Poggers')
            Generic.SystemMsg('critical','Poggers')
            Generic.SystemMsg('question','Poggers')
            Generic.SystemMsg('neutral','Poggers')

def GameLoop():
    global looping
    while looping:
        if Generic.AudSys.audio.music.get_busy() == True:
            console.log("Generic.AudSys.audio.music.get_busy() is " + str(Generic.AudSys.audio.music.get_busy()))
            pass
        else:
            Generic.AudSys.Music(filename="Dark-main-menu-song-REV1.ogg", play=True).Load()
        MainMenu = """
                            [green][1] New Game[/green]
                            [yellow][2] Load Game[/yellow]
                            [blue][3] Settings[/blue]
                            [red][4] Exit[/red]
                    """
        # printmd(f"[italic red]{MainMenu}[/italic red] Poggers")
        leaveterms = ["quit","leave","exit"]
        try:
            Generic.printmd(MainMenu)
            selection = input('>> ')
            # Extra.Fun(selection) is for funny
            Extra.Fun(selection)
            Selection(int(selection))
        except Exception as ERR:
            Generic.ClearScreen()
            console.log(f"Selection Error: {ERR} is given.")
            Splash()

# Game will be based on a reputation system, reputation of the player to each character introduced.

# Use json for saving reputation in Global Use inside .\Assets\GlobalVariables
# instead of the above use of jeson for reputation, create some sort of json save-file format for saving
# data, and use a separate folder in .\Assets for loading in saves to keep the saves un-altered unless
# the player saved the game

# create a separate .py file to display images perhaps using tkinter's GUI !

Splash()
GameInit()

GameLoop()

Generic.printmd("[red]Game Closed[/red]")
Generic.Wait(2)
