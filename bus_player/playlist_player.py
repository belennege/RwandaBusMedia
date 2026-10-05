import pygame
import time

PLAYLIST_FILE = "playlists/default_playlist.txt"

pygame.mixer.init()

print("================================")
print("   RWANDA BUS MEDIA PLAYLIST")
print("================================")

# Read the playlist
with open(PLAYLIST_FILE, "r") as file:
    playlist = [line.strip() for line in file if line.strip()]

print("\nPlaylist loaded:")
print("----------------")

for number, song in enumerate(playlist, start=1):
    print(f"{number}. {song}")

print("\nStarting playlist...\n")

# Keep playing the playlist continuously
while True:

    for number, song in enumerate(playlist, start=1):

        print(f"▶ Playing advertisement {number}")
        print(f"File: {song}")

        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        # Wait until the advertisement finishes
        while pygame.mixer.music.get_busy():
            time.sleep(1)

        print(f"✓ Advertisement {number} finished.\n")