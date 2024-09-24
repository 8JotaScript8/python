import pygame
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()