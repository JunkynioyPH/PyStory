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
    os.system('mode con cols=210 lines=45')
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
        case 20:
            Generic.cmdline.clearscreen()
            splash()
            # Send any number in the Main Menu to trigger this test
            Generic.cmdline.dialog(char='SYSTEM CALL', str='Performing the series of tests!')
            Generic.cmdline.dialog(spc=2)
            Generic.wait(4, msg=True)
            Generic.cmdline.dialog(char='system', str='this is a testing typing string!', dur=25)
            Generic.cmdline.dialog(char='[green]system style[/green]', str='character [red]dialogue style[/red]', dur=25)
            Generic.cmdline.dialog(char='[red]system style[/red]', str='character dialogue', dur=25)
            Generic.cmdline.dialog(char='no-style', str='gamer gaming', dur=25)
            Generic.cmdline.dialog(str='[red]No character[/red] [blue]no style[/blue]', dur=25)
            long_text = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Sed adipiscing diam donec adipiscing tristique risus. Sed lectus vestibulum mattis ullamcorper velit sed ullamcorper.
            Volutpat ac tincidunt vitae semper quis lectus nulla.
            Integer feugiat scelerisque varius morbi enim nunc faucibus.
            Rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat.
            Fermentum odio eu feugiat pretium nibh ipsum consequat.
            Adipiscing elit pellentesque habitant morbi tristique senectus et.
            Vel pharetra vel turpis nunc eget lorem.
            Purus faucibus ornare suspendisse sed nisi lacus. Donec massa sapien faucibus et molestie.
            """
            Generic.cmdline.dialog(char='[green]Lorem Ipsum[/green]', str=f'[red]{long_text}[/red]', dur=3.125)
            Generic.popup.system('warning','Poggers')
            Generic.popup.system('critical','Poggers')
            Generic.popup.system('question','Poggers')
            Generic.popup.system('neutral','Poggers')
        case _:
            Generic.cmdline.clearscreen()
            splash()
            Generic.cmdline.dialog(char='SYSTEM CALL', str='[red]Invalid Selection![/red]', dur=30)

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
        try:
            print()
            console.log("Generic.AudSys.audio.music.get_busy() is " + str(Generic.AudSys.audio.music.get_busy())) ####
            Generic.cmdline.dialog(str=MainMenu, dur=2.5)
            ans = Generic.ask('                        >>   ')
            # Extra.Fun(selection) is for funny
            Extra.Fun(ans)
            selection(int(ans))
        except Exception as ERR:
            Generic.cmdline.clearscreen()
            Generic.cmdline.dialog(char='SYSTEM CALL', str=f'[red]{ERR}[/red]', dur=15)
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
