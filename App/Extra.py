import App.Core as Core

def Fun(Case):
    match Case:
        case "test":
            Core.popup.image('Background','.\\Assets\\test\\Char_Full_BG.png')
        case "Lmfao":
            print('ayo wtf')
            Core.wait(2)
        case "Debug":
            Core.cli.dialog(char='SYSTEM CALL', str='Performing the series of tests!')
            Core.cli.dialog(newline=2)
            Core.cli.dialog(char="Testing this poggers feature", str="hmmmm....... we are still waiting.... for the thing to load...... sad. unpoggers.", richmd="red")
            Core.wait(4, msg=True)
            Core.cli.dialog(char="[green]Minecraft Mod[/green]", str="System Info of the mod is", dur=15)
            Core.cli.dialog(str="currently, unavailable.", richmd="red", dur=15)
            Core.cli.dialog(str="This is something we plan to work on in the future!", dur=15)
            Core.cli.dialog(str="Stay Tuned!", richmd="green")
            Core.cli.dialog(char='system', str='this is a testing typing string!', dur=25)
            Core.cli.dialog(char='[green]system style[/green]', str='character dialogue style', dur=25)
            Core.cli.dialog(char='[red]system style[/red]', str='character dialogue', dur=25)
            Core.cli.dialog(char='no-style', str='gamer gaming', dur=25)
            Core.cli.dialog(str='No character no style', dur=25)
            long_text = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Sed adipiscing diam donec adipiscing tristique risus. Sed lectus vestibulum mattis ullamcorper velit sed ullamcorper.
            Volutpat ac tincidunt [red] vitae semper quis lectus nulla.
            Integer feugiat scelerisque varius morbi enim nunc faucibus.
            Rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat.
            Fermentum odio eu feugiat pretium nibh ipsum consequat.
            Adipiscing elit pellentesque [/red] habitant morbi tristique senectus et.
            Vel pharetra vel turpis nunc eget lorem.
            Purus faucibus ornare suspendisse sed nisi lacus. Donec massa sapien faucibus et molestie.
            """
            long = """            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"""
            
            # While it is possible to render these block of text with dialog(), it does not support colors and breaks formatting.
            # instead, use rendertext() which supports formatting directly in the string.
            Core.cli.rendertxt(title='[green]Lorem Ipsum[/green]', str=f'{long_text}', dur=10) # dur == milliseconds
            # Example of in-text Formatting breaking.
            Core.cli.dialog(char='[green]EXAMPLE[/green]', str=f'{long_text}', dur=1) # dur == milliseconds
            # 
            Core.cli.dialog(char='[green]Lorem Ipsum[/green]', str=f'{long}', dur=3.125, newline=1) # dur == milliseconds
            
            Core.wait(4)
            Core.cli.dialog(char='TEST CHARACTER', str='this is a testing poggers poggers')
            Core.cli.dialog(bkspc=19, dur=80)
            Core.cli.dialog(str='ing of the function to delete and write new text on the same line.')
            Core.cli.dialog(newline=2, bkspc=2)
            Core.popup.system('warning','Poggers')
            Core.popup.system('critical','Poggers')
            Core.popup.system('question','Poggers')
            Core.popup.system('neutral','Poggers')