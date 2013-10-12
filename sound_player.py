import pygame

def start():
    print "Start"
    pygame.mixer.init()
    pygame.mixer.music.load('/Users/sam/code/morsecode-karaoke/sample1.ogg')
    pygame.mixer.music.play()
    while True:
        pass