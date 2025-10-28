import App.Core as Core

long_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Sed adipiscing diam donec adipiscing tristique risus. Sed lectus vestibulum mattis ullamcorper velit sed ullamcorper.
Volutpat ac tincidunt .[red] vitae semper quis lectus nulla.
Integer feugiat scelerisque varius morbi enim nunc faucibus.
Rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat.
Fermentum odio eu feugiat pretium nibh ipsum consequat.
Adipiscing elit pellentesque .\ habitant morbi tristique senectus et.
Vel pharetra vel turpis nunc eget lorem.
Purus faucibus ornare suspendisse sed nisi lacus. Donec massa sapien faucibus et molestie.
"""
long = """            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"""


def Fun(Case):
    match Case:
        case "test":
            Core.Cli('This is a test').print(True)
            Core.Common.wait(5, verbose=True)
            Core.Cli('Lorem ipsum dolor sit amet, .[red b i] consectetur adipiscing elit, sed do ]]eiusmod tempor incididunt .\ ut labore et dolore magna aliqua. Sed adipiscing diam donec... adipiscing tristique risus.').fancyPrint(10, True)
            Core.Cli(long_text).fancyPrint(20, True)
            Core.Common.wait(5, verbose=True)
            # Core.popup.image('Background','.\\Assets\\test\\Char_Full_BG.png')
        case "Lmfao":
            print('ayo wtf')
            Core.wait(2)
        case "Debug":
            Core.Cli.dialog(char='SYSTEM CALL', str='Performing the series of tests!')
            Core.Cli.dialog(newline=2)
            Core.Cli.dialog(char="Testing this poggers feature", str="hmmmm....... we are still waiting.... for the thing to load...... sad. unpoggers.", richmd="red")
            Core.Common.wait(4, msg=True)
            Core.Cli.dialog(char="[green]Minecraft Mod[/green]", str="System Info of the mod is", dur=15)
            Core.Cli.dialog(str="currently, unavailable.", richmd="red", dur=15)
            Core.Cli.dialog(str="This is something we plan to work on in the future!", dur=15)
            Core.Cli.dialog(str="Stay Tuned!", richmd="green")
            Core.Cli.dialog(char='system', str='this is a testing typing string!', dur=25)
            Core.Cli.dialog(char='[green]system style[/green]', str='character dialogue style', dur=25)
            Core.Cli.dialog(char='[red]system style[/red]', str='character dialogue', dur=25)
            Core.Cli.dialog(char='no-style', str='gamer gaming', dur=25)
            Core.Cli.dialog(str='No character no style', dur=25)
            # While it is possible to render these block of text with dialog(), it does not support colors and breaks formatting.
            # instead, use rendertext() which supports formatting directly in the string.
            Core.Cli.rendertxt(title='[green]Lorem Ipsum[/green]', str=f'{long_text}', dur=10) # dur == milliseconds
            # Example of in-text Formatting breaking.
            Core.Cli.dialog(char='[green]EXAMPLE[/green]', str=f'{long_text}', dur=1) # dur == milliseconds
            # 
            Core.Cli.dialog(char='[green]Lorem Ipsum[/green]', str=f'{long}', dur=3.125, newline=1) # dur == milliseconds
            
            Core.wait(4)
            Core.Cli.dialog(char='TEST CHARACTER', str='this is a testing poggers poggers')
            Core.Cli.dialog(bkspc=19, dur=80)
            Core.Cli.dialog(str='ing of the function to delete and write new text on the same line.')
            Core.Cli.dialog(newline=2, bkspc=2)
            Core.popup.system('warning','Poggers')
            Core.popup.system('critical','Poggers')
            Core.popup.system('question','Poggers')
            Core.popup.system('neutral','Poggers')