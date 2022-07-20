import os, time, json
# from rich import pretty
# pretty.install()
import App.Generic as Generic
from App.Generic import console
import App.AudSys as AudSys

os.system('cls' if os.name=='nt' else 'clear')
os.system('title PyStory - Junkynioy#2408')

# Settings(): function, Perhaps use JSON

def Splash():
    global SplashText
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
    Generic.Wait(2)

def GameInit():
    # load volume from settings
    # Generic.LoadSave() somewhere in the main menu
    AudSys.AudioSystemInitialise(0.250/10)

    # use [['text1'],[text2]] .py list for Dialogues
    # ChapterX.py which contains a list of dialogue for that chapter

def Selection(Option):
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
        # case _:
        #     Generic.ClearScreen()
        #     Generic.SystemMsg('warning','Poggers')
        #     Generic.SystemMsg('critical','Poggers')
        #     Generic.SystemMsg('question','Poggers')
        #     Generic.SystemMsg('neutral','Poggers')

def GameLoop():
    while True:
        SongPos = int(AudSys.audio.music.get_pos()/1000)
        if SongPos != 0:
            pass
        else:
            AudSys.AudioMusicPlay("Dark-MainMenu-Song.ogg")
        MainMenu = """
                            [green][1] New Game[/green]
                            [yellow][2] Load Game[/yellow]
                            [3] Settings
                        """
        # print(f"[italic red]{MainMenu}[/italic red] Poggers",locals())
        try:
            Generic.printmd(MainMenu)
            Selection(int(input('>> ')))
        except Exception as ERR:
            Generic.ClearScreen()
            print(SplashText)
        # x = input("\nCurrently in Mainloop : ")
        # if x == '':
        #     Generic.MessageBox('Title','Subtitle','Message',3,'ContinueButton')
        #     break

# Game will be based on a reputation system, reputation of the player to each character introduced.
# Use json for saving reputation in Global Use inside .\Assets\GlobalVariables

# create a separate .py file to display images perhaps using tkinter's GUI !

Splash()
GameInit()

GameLoop()

# after gameloop ends
Generic.Wait(5)
