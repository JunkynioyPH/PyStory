import App.Core as Core
import App.Core_Legacy as CoreL
import App.CrossAppHelper as Comms

custom_tags = """
.[red b i] These all have optional syntaxes OMITTED! ./ ./_nl ./_nl
testing(BACKSPACE b_20 + Red Overwrite). 123456789ABCDEFGHIJK ./_b_20 .[red] 123456789ABCDEFGHIJK. ./ ./_nl
testing(BACKSPACE_DELETE bd_20 + Red Overwrite). 123456789ABCDEFGHIJK ./_bd_20 .[red] 123456789ABCDEFGHIJK. ./ .
testing(PAUSE p_2 + Red Bold Italics). Lorem ipsum dolor sit amet, .[red b i] consectetur adipiscing ./_p_2 elit, [[sed do []]]eiusmod tempor incididunt. ./ ./_nl
testing(PAUSE_TRAILING pt_2 + Red Overwrite). 123456789 ./_pt_2 .[red] ABCDEFGHIJK. ./ ./_nl
testing(UNKNOWN). This is a test of an unknown tag ./_a_x <<< This should be a '???' ./_nl
"""

long_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, ./_b_50_100 sed do eiusmod tempor incididunt ./_b_50 ut labore et dolore magna aliqua.
Sed adipiscing diam donec adipiscing tristique risus. Sed lectus vestibulum mattis ullamcorper velit sed ullamcorper.
Volutpat ac tincidunt .[red] vitae semper quis lectus nulla.
Integer feugiat scelerisque varius morbi enim nunc faucibus.
Rhoncus est pellentesque elit ullamcorper ./_bd_50 dignissim cras tincidunt lobortis feugiat.
Fermentum odio eu feugiat pretium nibh ipsum consequat.
Adipiscing elit pellentesque ./ habitant morbi ./_bd_50_150 tristique senectus et.
Vel pharetra vel turpis nunc eget lorem.
Purus faucibus ornare suspendisse sed nisi lacus. Donec massa sapien faucibus et molestie.
"""
long = """            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"""

    # Core.audioEngine.toggleState('audio','loop')
    # Core.audioEngine.play('audio','mainMenu')

# audioEngine = Comms.ClientObj("127.0.2.1",2222,"Game")

def Fun(Case):
    
    
    match Case:
        case "Lmfao":
            print('ayo wtf')
            Core.Common.wait(2)
        case 'music':
            audioEngine.send('mediaPos:0')
            audioEngine.send('status')
        case "test":
            Core.Cli('This is a test').print(True)
            Core.Common.wait(2, verbose=True)
            audioEngine.send("audioIndex:add:audio:./Assets/Audio/Music/mainMenu.ogg")
            audioEngine.send("listDevices")
            audioEngine.send("setDevice:3")
            audioEngine.send("toggle:audioLoop")
            audioEngine.send("play:audio:mainMenu")
            audioEngine.send('mediaPos:0')
            
            # Core.Cli(custom_tags).fancyPrint(10, True)
            # Core.Cli(long_text).fancyPrint(20, True)
            Core.Common.wait(10, verbose=True)
        
            # Core.popup.image('Background','./Assets\\test\\Char_Full_BG.png')
        case "debug":
            #
            SYSTEM = Core.Common.Character('<[yellow]SYSTEM CALL[/yellow]>', 80)
            TEST_FEATURE = Core.Common.Character("[[green]Testing Features[/green]]", 75)
            MINECRAFT = Core.Common.Character('[green][Minecraft Mod]', 85)
            LEGACY = Core.Common.Character('[magenta b]:LEGACY:',40)
            INLINE = Core.Common.Character('',0)
            TEST = Core.Common.Character("SingleWord",20)
            
            TEST.say('this is a character with only 1 wordName')
            SYSTEM.say('Performing the series of tests!')
            SYSTEM.say('.[red b] MY HEAD HURTS!!!!!!!!!! ./')
            SYSTEM.say('this is on a new line', newline=False)
            INLINE.say('.[red b i] this is slowed and in the same line ./ Poggers.',150)
            
            TEST_FEATURE.say(".[red] hmmmm....... we are still waiting.... for the thing to load...... sad. unpoggers.")
            MINECRAFT.say("System Info of the mod is .[red] currently, unavailable. ./ This is something we plan to work on in the future! .[green b] Stay Tuned! ./")
            Core.Common.wait(2, verbose=True)
            
            LEGACY.say('This is a test of legacy code.')
            LEGACY.say('This is how it used to be done before. Less features and janky.',80)
            Core.Common.wait(2, verbose=True)
            CoreL.cli.dialog(char='system', str='this is a testing typing string!', dur=25)
            CoreL.cli.dialog(char='[green]system style[/green]', str='character dialogue style', dur=25)
            CoreL.cli.dialog(char='[red]system style[/red]', str='character dialogue', dur=25)
            CoreL.cli.dialog(char='no-style', str='gamer gaming', dur=25)
            CoreL.cli.dialog(str='No character no style', dur=25)

            # make bulk text rendering?
            CoreL.cli.rendertxt(title='[green]Lorem Ipsum[/green]', str=f'{long_text}', dur=10) # dur == milliseconds
            Core.Common.wait(4)

            CoreL.cli.dialog(char='[green]Lorem Ipsum[/green]', str=f'{long}', dur=3.125, newline=1) # dur == milliseconds
            
            CoreL.cli.dialog(char='TEST CHARACTER', str='this is a testing poggers poggers')
            CoreL.cli.dialog(bkspc=19, dur=80)
            CoreL.cli.dialog(str='ing of the function to delete and write new text on the same line.')
            CoreL.cli.dialog(newline=2, bkspc=2)
            INLINE.say('')
            Core.Common.wait(4, verbose=True)
            # Core.popup.system('warning','Poggers')
            # Core.popup.system('critical','Poggers')
            # Core.popup.system('question','Poggers')
            # Core.popup.system('neutral','Poggers')