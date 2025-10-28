import os
# FOOK OFF!!, STFU!!!
os.environ["QT_FFMPEG_LOG_LEVEL"] = "fatal"
os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.multimedia.*=false"
from rich import pretty
from App import Core, Extra
pretty.install()

# # https://stackoverflow.com/questions/64376497/disable-resizing-for-python-console-application-in-windows
# def lock_resize():
#     while True:
#         os.system('mode con cols=210 lines=45')
# # threading.Thread(target=lock_resize(), args=(1,), daemon=True).start()
# _thread.start_new_thread(lock_resize,()) #using the _thread module to keep everything else running
#
# I Guess I know how to Multithread now, i guess. or atleast i know how to start one

if os.name=='nt':
    os.system('title PyStory - Junkynioy#2408')
    os.system('mode con cols=210 lines=45') # does not work with w11 terminal
else:
    Core.Cli("\n[green]PyStory - Junkynioy#2408[/green]\n").print()

# Settings(): function, Perhaps use JSON

def splash():
    # Core.Cli.clear()
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
    Core.Cli(splashText).print()

def gameinit():
    global mainMenuLoop
    mainMenuLoop = True
    # load volume from settings
    # Core.LoadSave() somewhere in the main menu
    
    # find a way to silence the fking thing that pops up
    # when it plays an audio file
    # temp
    Core.audioEngine.addIndex('audio','./Assets/Audio/Music/mainMenu.ogg')
    Core.audioEngine.toggleState('audio','loop')
    Core.audioEngine.play('audio','mainMenu')
    

    # use [['text1'],[text2]] .py list for Dialogues
    # ChapterX.py which contains a list of dialogue for that chapter

def selection(Option):
    global mainMenuLoop
    match Option:
        case 1:
            Core.Cli.clear()
            # Core.NewGame()
        case 2:
            Core.Cli.clear()
            # Core.LoadFile()
        case 3:
            Core.Cli.clear()
            # Core.Settings()
        case 4:
            if Core.Common.ask('[yellow]Are you[/yellow] [green]Sure?[/green] [[green]y[/green]/[red]n[/red]] [pink]>>[/pink] ').lower() == 'y':
                mainMenuLoop = False
            else:
                splash()
        case _:
            Core.Cli.clear()
            splash()
            Core.Cli("[red]Invalid Selection![/red]").print()

def gameloop():
    # Main Loop
    while mainMenuLoop:
        MainMenu =  """
                    [bold green][1] New Game[/bold green]
                    [bold yellow][2] Load Game[/bold yellow]
                    [bold blue][3] Settings[/bold blue]
                    [bold red][4] Exit[/bold red]
                    \n"""
        
        Core.Cli(f"\n[bright_cyan]Select[/bright_cyan] an [bright_blue]option[/bright_Blue]{MainMenu}").print()
        answer = Core.Common.ask('                    >>  ')
        Extra.Fun(answer)
        try:
            selection(int(answer))
        except ValueError:
            Core.Cli.clear()
            Core.Cli(f'[red]"{answer}" is not an Integer.[/red]').print()
            splash()

    # then the game stuff initialises here


# Game will be based on a reputation system, reputation of the player to each character introduced.

# Use json for saving reputation in Global Use inside .\Assets\GlobalVariables
# instead of the above use of json for reputation, create some sort of json save-file format for saving
# data, and use a separate folder in .\Assets for loading in saves to keep the saves un-altered unless
# the player saved the game

# create a separate .py file to display images perhaps using tkinter's GUI !

gameinit()
splash()
gameloop()

Core.Cli("[red]Game Closed[/red]").print()
Core.Common.wait(2)
