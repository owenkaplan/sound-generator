import pygame, sys, glob, random
from pygame.locals import *
pygame.init()
DISPLAYFURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Baxter ')


oggFiles = glob.glob('mp3/*.ogg')
print "There are currently", len(oggFiles), "tracks available."

def getNumTracks():
    choice = -1
    while not isValidFileName(choice):
        choice = raw_input('number of tracks: ')

    return int(choice)

def isValidFileName(choice):
    if not isNumeric(choice):
        return False

    choice = int(choice)
    if choice <= len(oggFiles) and choice > 0:
        return True
    else:
        return False

def isNumeric(choice):
    try:
        float(choice) * 2 > float(choice)
        return True
    except:
        return False
    






pygame.mixer.init()
sounds = []

choice = getNumTracks()


n = 0

while n < choice:
    indexToGet = 0
    if len(oggFiles) > 1:
        indexToGet = random.randrange(0,len(oggFiles) - 1)

    py_play = oggFiles[indexToGet]
    oggFiles.remove(py_play)    
    sounds.append(pygame.mixer.Sound(py_play))
    n += 1

print sounds

sounds[0].play()
sounds[1].play()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
