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

DEVICE = QMediaDevices.defaultAudioOutput()
audioEngine = AudioEngine.AudioManager(DEVICE)

class Cli():
    def __init__(self, text:str=''):
        """Contains basic CLI text rendering implementations."""
        self.text = text
    
    def clear():
        """Clears text in CLI window."""
        os.system('cls' if os.name=='nt' else 'clear')
    
    def backspace(self, backspace:int, delay:int):
            for _ in range(backspace+1):
                self.print('\b \b', end="", flush=True)
                time.sleep(float(delay)/1000)
        
    def print(self, newline=False):
        """Simply print."""
        rich.print(f'{self.text}', end=f'{'\n' if newline else ''}')
        
    def fancyPrint(self, delay:int=60, newLineEnd:bool=False):
        """Printing text with style.
        - Simulating typing, backspace keystrokes.
        - Print text whilst supporting Rich's [ ] tags.
        - ' .[ ' marks TAG_START and ' .\\ ' marks TAG_END
        - there must be a space before AND after .[] & .\\
        > "this is sampletext. .[red b i] This is RED, BOLD, ITALICS .\ """
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
            if '.\\' in word:
                colorBuffer = []
                continue
            
            for letter in word:
                Cli(f"{''.join(colorBuffer)}{letter}").print()
                time.sleep(float(delay)/1000)
            else:
                Cli(' ').print() # Re-introduce per-word spaces
                # Re-implement newlines, when it finds a ' . ' as the last "letter"
                if word[-1] == '.':
                    print()
        else:
            print() if newLineEnd else ''
    
class Common():
    def wait(Duration, verbose=False):
        if verbose:
            Cli(f'.[yellow] Waiting <{Duration if Duration < 60 else Duration/60}{'s' if Duration < 60 else 'min/s'}> ... .\\').fancyPrint()
            time.sleep(Duration)
            print()
            return
        
        time.sleep(Duration)
        print()
        
    def ask(text:str) -> str:
        Cli(text).print()
        return input()
        
        
    