import os, time, rich, sys, json
from PyQt6.QtMultimedia import QMediaDevices
from PyQt6.QtWidgets import QApplication
from rich.console import Console
from App import GuiBox
import App.AudioSystem_PyQt6 as AudioEngine

APP = QApplication([]) # Mandatory.

# When the music loops, it has that notification on CLI about updating timestamps for discarded samples.
# find a way to make it STFU. OR USE .WAV /Shrug ATP use "sound" if using .WAV :skull:
# 
# [vorbis @ 0x4f7db00] Could not update timestamps for discarded samples. 71-Char line
#             ^^^^^^ im sure this thing stays at a consistent length

DEVICE = QMediaDevices.defaultAudioOutput()
audioEngine = AudioEngine.AudioManager(DEVICE)
CONSOLE = Console()

class Cli():
    def __init__(self, text:str=''):
        self.text = text
        pass
    
    def clear():
        os.system('cls' if os.name=='nt' else 'clear')
        
    def print(self, newline=False):
        rich.print(f'{self.text}', end=f'{'\n' if newline else ''}')
class Common():
    def wait(Duration, verbose=False):
        if verbose:
            Cli(f'\n[yellow]Waiting... [{Duration if Duration < 60 else Duration/60}{'s' if Duration < 60 else 'min/s'}][/yellow]').print()
            time.sleep(Duration)
            return
        
        time.sleep(Duration)
        
    def ask(text:str) -> str:
        Cli(text).print()
        return input()
        
        
    