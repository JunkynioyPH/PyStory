import App.Core as Core

long_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Sed adipiscing diam donec adipiscing tristique risus. Sed lectus vestibulum mattis ullamcorper velit sed ullamcorper.
Volutpat ac tincidunt .[red] vitae semper quis lectus nulla.
Integer feugiat scelerisque varius morbi enim nunc faucibus.
Rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat.
Fermentum odio eu feugiat pretium nibh ipsum consequat.
Adipiscing elit pellentesque ./ habitant morbi tristique senectus et.
Vel pharetra vel turpis nunc eget lorem.
Purus faucibus ornare suspendisse sed nisi lacus. Donec massa sapien faucibus et molestie.
"""
long = """            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"""


def Fun(Case):
    match Case:
        case "test":
            Core.Cli('This is a test').print(True)
            # Core.Cli('.').print(True)
            Core.Common.wait(5, verbose=True)
            Core.Cli('Lorem ipsum dolor sit amet, .[red b i] consectetur adipiscing ./_p_2 elit, sed do ]]eiusmod tempor incididunt ./ ut labore et ./_a_x dolore magna aliqua. Sed adipiscing diam donec... adipiscing tristique risus.').fancyPrint(10, True)
            Core.Cli(long_text).fancyPrint(20, True)
            Core.Common.wait(5, verbose=True)
            # Core.popup.image('Background','./Assets\\test\\Char_Full_BG.png')
        case "Lmfao":
            print('ayo wtf')
            Core.wait(2)
        case "Debug":
            Core.Character('SYSTEM CALL').say(str='Performing the series of tests!')
            # Core.Character.say(newline=2)
            Core.Character('Testing this poggers feature').say(str=".[red] hmmmm....... we are still waiting.... for the thing to load...... sad. unpoggers.")
            Core.Common.wait(4, verbose=True)
            Core.Character('.[green] Minecraft Mod ./').say(str="System Info of the mod is .[red] currently, unavailable. ./ This is something we plan to work on in the future! .[green b] Stay Tuned! ./")
            
            # Core.Character.say(char='system', str='this is a testing typing string!', dur=25)
            # Core.Character.say(char='[green]system style[/green]', str='character dialogue style', dur=25)
            # Core.Character.say(char='[red]system style[/red]', str='character dialogue', dur=25)
            # Core.Character.say(char='no-style', str='gamer gaming', dur=25)
            # Core.Character.say(str='No character no style', dur=25)

            # make bulk text rendering?
            # Core.Cli.renderTxtBlock(title='[green]Lorem Ipsum[/green]', str=f'{long_text}', dur=10) # dur == milliseconds

            # Core.Character.say(char='[green]Lorem Ipsum[/green]', str=f'{long}', dur=3.125, newline=1) # dur == milliseconds
            
            # Core.Common.wait(4)
            # Core.Character.say(char='TEST CHARACTER', str='this is a testing poggers poggers')
            # Core.Character.say(bkspc=19, dur=80)
            # Core.Character.say(str='ing of the function to delete and write new text on the same line.')
            # Core.Character.say(newline=2, bkspc=2)
            # Core.popup.system('warning','Poggers')
            # Core.popup.system('critical','Poggers')
            # Core.popup.system('question','Poggers')
            # Core.popup.system('neutral','Poggers')