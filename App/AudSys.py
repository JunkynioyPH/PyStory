from pygame import mixer as audio

def AudioSystemInitialise(Volume1):
    audio.init()
    audio.music.set_volume(Volume1/1000) # Manipulated with LOAD SETTINGS such as in py soundboard
    
    # THE VOLUME @ 0.125 IS SOMEHOW LOUD. DIVIDE THE VOLUME BY 1000 (eg 100% / 1000 = 0.1)

class Music:
    def __init__(self, filename="", s=0, play=False):
        self.filename = filename
        self.play = play
        self.s = s

    def Load(self):
        # String
        audio.music.load(f".\Assets\Audio\Music\{self.filename}")
        if self.play == True:
            Music.Play()

    def Unload():
        audio.music.unload()
  
    def Play():
        audio.music.play(loops=-1)

    def Stop():
        audio.music.stop()

    def FadeOut(self):
        audio.music.fadeout(float(self.s * 1000))

    def Pause():
        audio.music.pause()

    def Resume():
        audio.music.unpause()


class SoundFX:
    def __init__(self, filename="", s=0, play=False):
        self.filename = filename
        self.play = play
        self.s = s

    def Play(self):
        # What the actual heck,  thought you cant chain them together?????? ".play().set_volume(float)"
        # if adding pause when spamming, it's inconsistent at <0.54s delay, use >0.55 
        audio.Sound(f".\Assets\Audio\Sfx\{self.filename}").play().set_volume(0.025)