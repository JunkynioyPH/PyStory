from pygame import mixer as audio
from App.xpfpath import *

def audiosysteminit(Volume1):
    audio.init()
    audio.music.set_volume(Volume1/100) # Manipulated with LOAD SETTINGS such as in py soundboard # temp change to 100
    
    # THE VOLUME @ 0.125 IS SOMEHOW LOUD. DIVIDE THE VOLUME BY 1000 (eg 100% / 1000 = 0.1)

class music:
    def load(filename, play):
        # String
        audio.music.load(xpfp(f".\Assets\Audio\Music\{filename}"))
        if play == True:
            music.play()

    def unload():
        audio.music.unload()
  
    def play():
        audio.music.play(loops=-1)

    def stop():
        audio.music.stop()

    def fadeout(s):
        audio.music.fadeout(float(s * 100)) # temp change to 100

    def pause():
        audio.music.pause()

    def resume():
        audio.music.unpause()

# might turn into a class that makes its own sfx instances, in reference to how i did the buttons on pysoundboard project.
class soundfx:
    def play(filename):
        # What the actual heck,  thought you cant chain them together?????? ".play().set_volume(float)"
        # if adding pause when spamming, it's inconsistent at <0.54s delay, use >0.55 
        audio.Sound(xpfp(f".\Assets\Audio\Sfx\{filename}")).play().set_volume(0.25) # again, 0.25 is somehow loud, * by 1000 (25 * 1000) # temp change to 0.25 (/100)