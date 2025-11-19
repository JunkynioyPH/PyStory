import os, time, rich, sys, json
from PyQt6.QtMultimedia import QMediaDevices
from PyQt6.QtWidgets import QApplication
from rich.console import Console
from App import GuiBox
import App.AudioSystem_PyQt6 as AudioEngine

APP = QApplication([]) # Mandatory.
CONSOLE = Console()

# When the music loops, it has that notification on CLI about updating timestamps for discarded samples.
# find a way to make it STFU. OR USE .WAV /Shrug ATP use "sound" if using .WAV :skull:
# 
# [vorbis @ 0x4f7db00] Could not update timestamps for discarded samples. 71-Char line
#             ^^^^^^ im sure this thing stays at a consistent length

# DEVICE = QMediaDevices.defaultAudioOutput()
# audioEngine = AudioEngine.AudioManager(DEVICE)

class Cli():
    def __init__(self, text:str=''):
        """Contains basic CLI text rendering implementations."""
        self.text = text
    
    def clear():
        """Clears text in CLI window."""
        os.system('cls' if os.name=='nt' else 'clear')
    
    def backspace(self, backspace:int, delay:int=60, replacementChar:str=''):
        # This will have alignment issues if the
        # window is too small for text that is too lengthy
        #
        # Idk how to get around that
        # For now it shall assume that the window is large enough
        for _ in range(backspace):
            print(f"\x1b[1D"+replacementChar+f"{'\x1b[1D'*len(replacementChar)}", end='', flush=True)
            time.sleep(float(delay)/1000)
    
    def backUpLine(self, lines:int):
        for _ in range(lines):
            print('\x1b[1A', end='', flush=True)
    
    def print(self, newline=False):
        """Simply print."""
        rich.print(f'{self.text}', end=f'{'\n' if newline else ''}')
        
    def fancyPrint(self, delay:int=60, newlines:bool=True, newLineEnd:bool=False):
        """Printing text with style.
        - Simulating typing, backspace keystrokes.
        - Print text whilst supporting Rich's [ ] tags.
        - Custom formatting tags, "Call-ins"
        
        ### There must be a space before AND after ' .[] ' & ' ./ '
        - ' .[tag] ' marks RICH_TAG_START and ' ./ ' marks RICH_TAG_END
        > "This is sampletext. .[red b i] This is RED, BOLD, ITALICS ./ 
        - Call-in functions in-string with ' ./_ ', syntax is split with ' _ '
        > "This is sampletext. ./_b_10 backspace 10 characters"
        
        - List of Call-ins:
        >- ./_p_x = pause for Float x seconds.
        >- ./_pt_x = pause with no trailing space.
        >- ./_b_x_y = backspace Int x times, (opt) delayed for Int y ms (1000ms = 1s)
        >- ./_bd_x_y = backspace, but delete as it goes back.
        >- ./_nl = newline without using ' . ' to trigger a newline
        
        """
        colorBuffer = []
        colorConstructMode = False
        wordsBuffer = self.text.split()
        for word in wordsBuffer:
            # for single-parameter tags
            if word.startswith('.[') and word.endswith(']'):
                colorBuffer.append(f"{word[1:len(word)]}")
                continue
            # Enable [format] Construction mode for fragmented tags
            if word.startswith('.[') and not word.endswith(']'):
                colorConstructMode = True
                colorBuffer.append(f"{word[1:len(word)]} ")
                continue
            # Disable Construction mode
            if word.endswith(']') and colorConstructMode:
                colorConstructMode = False
                colorBuffer.append(word)
                continue
            # Construct [formatA formatB formatC]
            if colorConstructMode:
                colorBuffer.append(f"{word} ")
                continue
            # Reset formatting
            if './' in word and len(word) < 3:
                colorBuffer = []
                continue
            # Perform known Call-in Tags
            elif './' in word and len(word) >= 3:
                # perfect place to parse custom tags and directly call functions
                # in-string without calling functions separately after/before printing
                # it's called-in mid-print
                parameters = word.split('_')[1:len(word.split('_'))] # omit ./
                match parameters[0].lower():
                    # offsets by 1 character is applied as in line 130, re-introduces per-word spaces.
                    case 'b':
                        # offset by 1 char
                        try: 
                            self.backspace(1,0)
                            self.backspace(int(parameters[1]), int(parameters[2]))
                        except IndexError:
                            self.backspace(1,0)
                            self.backspace(int(parameters[1]))
                    case 'bd':
                        # offset by 1 char
                        try:
                            self.backspace(int(parameters[1]), int(parameters[2]), ' ')
                            self.backspace(1,0)
                        except IndexError:
                            self.backspace(int(parameters[1]), replacementChar=' ')
                            self.backspace(1,0)
                    case 'pt':
                        # offset by 1 char
                        self.backspace(1,0)
                        Common.wait(float(parameters[1]))
                    case 'p':
                        Common.wait(float(parameters[1]))
                    case 'nl':
                        print(flush=True)
                    case _:
                        Cli('.[red b i u] ???').fancyPrint()
                continue
            
            for letter in word:
                Cli(f"{''.join(colorBuffer)}{letter}").print()
                time.sleep(float(delay)/1000)
            else:
                Cli(' ').print() # Re-introduce per-word spaces
                # Re-implement newlines, when it finds a ' . ' as the last "letter"
                # Gets disabled when newlines is set to FALSE
                if word[-1] == '.' and newlines:
                    print()
        else:
            print(flush=True) if newLineEnd else ''
    
class Common():
    def wait(Duration:int, verbose=False):
        if verbose:
            durationTick = Duration
            for _ in range(Duration):
                durationFormat = f"{durationTick if durationTick < 60 else durationTick/60}{'s' if durationTick < 60 else 'min/s'}"
                text = f'.[yellow] Waiting {durationFormat} ./'
                Cli(text).fancyPrint(25)
                time.sleep(1)
                durationTick -= 1
                Cli().backspace(len(text),10,' ')
            # print(flush=True)
            return
        time.sleep(Duration)
        
    def ask(text:str) -> str:
        Cli(text).print()
        return input()
    
    class Character():
        def __init__(self, name:str, delay:int):
            self.name:str = name+f'{' ' if name != '' else ''}'
            self.delay = delay
            # self.characterPFP = './...'
        def say(self, words:str, delay:int=0, newline:bool=True):
            delayValue:int = self.delay if delay == 0 else delay
            Cli(self.name).print()
            Cli(words).fancyPrint(delayValue, newlines=False, newLineEnd=newline)
        # def shout(self, words:str, delay:int=0, newline:bool=True):
        #     words = f".[b] {words} ./"
        #     self.say(words, delay, newline)
        # def ponder(self):
        #     ...
        
        
    