import os, time, rich
from rich.console import Console

console = Console()

class cli:
    def clear():
        os.system('cls' if os.name=='nt' else 'clear')

    def printmd(String, end='', multiLine=True):
        ## Wtf is this???
        print(f"\b \b"*len(String), end='', flush=True) if multiLine == False else ''
        rich.print(String, end=f"{end}", flush=True)
    
    # this is so scuffeds
    # https://stackoverflow.com/questions/28802417/how-to-count-lines-in-multi-lined-strings
    #
    # dialog(char="test", str="poggers") \n dialog(str="poggers" richmd="")
    #
    # rich library ( cli.printmd() ) ABSOLUTELY HATES " \b " or similar ESCAPE CODES.  (doesnt on windows 11? but it works in windows 10???)
    #

    def dialog(char="", str="", dur=60, newline=0, bkspc=0, richmd="", voice=''):
        def delete():
            for _ in range(bkspc+1):
                print('\b \b', end="", flush=True)
                time.sleep(float(dur)/1000) # milliseconds
        def write():
            print() if char != "" == richmd else ""
            strbuffer = str.split()
            charbuffer = f"<{char}>"
            if char != "":
                for letter in charbuffer:
                    cli.printmd(letter)
                    time.sleep(float(dur)/1000) # milliseconds
                cli.printmd(f"<{char}>  ", multiLine=False)
            # for each word in buffer
            for word in strbuffer:
                letter = 1
                ## for each letter in word
                while letter <= len(word):
                    _ = word[letter-1:letter]
                    cli.printmd(_)
                    letter += 1
                    #voice here, maybe soon ill add that, kinda like undertale's thingy when they talk
                    time.sleep(float(dur)/1000) # milliseconds
                print('\b \b'*len(word), end="", flush=True) if richmd != "" else "" ## figure how to get rid of this line
                cli.printmd(f"[{richmd}]{word}[/{richmd}]") if richmd != "" else ""
                cli.printmd(" ")
        # yeah it looks nicer but it's kinda no different to the regular if-elif-else statements
        cli.printmd('\n'*newline) if newline >= 1 and bkspc < 1 else ''
        cli.printmd("\n[red]You cannot use both \[newline] and \[bkspc] in dialog...[/red] [yellow]u dum? :clown:[/yellow]") if newline > 1 and bkspc > 1 else ''
        write() if bkspc < 1 else ''
        delete() if bkspc >= 1 and newline < 1 else ''

    # Render Blocks of Graphics, and Paragraph wall of text with styling, all in one go unlike dialog(), which you have to define styling in Function, not style in string block.
    def rendertxt(title='', str='', dur=0.5, newline=0):
        if newline < 1:
            print()
            line_count = len(list(str.split('\n')))
            full_str = f"[{title}]  {str}" if title != "" else ""
            letter = 1
            for letter in full_str:
                cli.printmd(letter)
                time.sleep(float(dur)/1000) # milliseconds
            print(f"\n" + "\x1b[1A\x1b[2K" * line_count, end='', flush=True)
            cli.printmd(f"{full_str}")
        else:
            cli.printmd('\n'*newline)
