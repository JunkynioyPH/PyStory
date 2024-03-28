import App.Generic as Generic

def Fun(Case):
    match Case:
        case "test":
            Generic.popup.image('Background','.\\Assets\\test\\Char_Full_BG.png')
        case "Lmfao":
            print('ayo wtf')
            Generic.wait(2)
        case "Debug":
            Generic.cmdline.dialog(char='SYSTEM CALL', str='Performing the series of tests!')
            Generic.cmdline.dialog(newline=2)
            Generic.cmdline.dialog(char="Testing this poggers feature", str="hmmmm....... we are still waiting.... for the thing to load...... sad. unpoggers.", richmd="red")
            Generic.wait(4, msg=True)
            Generic.cmdline.dialog(char="[green]Minecraft Mod[/green]", str="System Info of the mod is", dur=15)
            Generic.cmdline.dialog(str="currently, unavailable.", richmd="red", dur=15)
            Generic.cmdline.dialog(str="This is something we plan to work on in the future!", dur=15)
            Generic.cmdline.dialog(str="Stay Tuned!", richmd="green")
            Generic.cmdline.dialog(char='system', str='this is a testing typing string!', dur=25)
            Generic.cmdline.dialog(char='[green]system style[/green]', str='character dialogue style', dur=25)
            Generic.cmdline.dialog(char='[red]system style[/red]', str='character dialogue', dur=25)
            Generic.cmdline.dialog(char='no-style', str='gamer gaming', dur=25)
            Generic.cmdline.dialog(str='No character no style', dur=25)
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
            Long = """            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"""
            
            # While it is possible to render these block of text with dialog(), it does not support colors and breaks formatting.
            # instead, use rendertext() which supports formatting directly in the string.
            Generic.cmdline.rendertxt(title='[green]Lorem Ipsum[/green]', str=f'{long_text}', dur=10)
            Generic.cmdline.dialog(char='[green]Lorem Ipsum[/green]', str=f'{Long}', dur=3.125)
            
            Generic.wait(4)
            Generic.cmdline.dialog(char='TEST CHARACTER', str='this is a testing poggers poggers')
            Generic.cmdline.dialog(bkspc=19, dur=80)
            Generic.cmdline.dialog(str='ing of the function to delete and write new text on the same line.')
            Generic.cmdline.dialog(newline=2, bkspc=2)
            Generic.popup.system('warning','Poggers')
            Generic.popup.system('critical','Poggers')
            Generic.popup.system('question','Poggers')
            Generic.popup.system('neutral','Poggers')