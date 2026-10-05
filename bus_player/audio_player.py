import pygame
import time

AUDIO_FILE = "audio/advertisements/test_ad.mp3"

pygame.mixer.init()

print("================================")
print(" Rwanda Bus Media Audio Player")
print("================================")

print("Loading advertisement...")

pygame.mixer.music.load(AUDIO_FILE)

print("Playing advertisement...")

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Advertisement finished.")

pygame.mixer.quit()