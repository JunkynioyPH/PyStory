from pygame import mixer as audio

def AudioSystemInitialise(Volume):
    audio.init()
    audio.music.set_volume(Volume) # Manipulated with LOAD SETTINGS such as in py soundboard
    # THE VOLUME @ 0.125 IS SOMHOW LOUD. DIVIDE THE VOLUME BY 1000 (eg 100% / 1000 = 0.1)

    # there was another thing that specialises sound effects rather than music in pygame
    # check the docs!

def AudioMusicPlay(FileName):
    # Find a way to play multiple sounds at once!
    # String
    audio.music.load(f".\Assets\Audio\Music\{FileName}")
    audio.music.play(loops=-1)

def AudioSoundPlay(FileName):
    # Find a way to play multiple sounds at once!
    # String
    audio.music.load(f".\Assets\Audio\Sfx\{FileName}")
    audio.music.play()
