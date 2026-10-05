import pygame

# Advertisement files
advertisements = {
    "1": "audio/advertisements/ad_01.mp3",
    "2": "audio/advertisements/ad_02.mp3",
    "3": "audio/advertisements/ad_03.mp3",
    "4": "audio/advertisements/test_ad.mp3"
}

pygame.mixer.init()

current_ad = None

print("================================")
print("     RWANDA BUS MEDIA PLAYER")
print("================================")

while True:

    print("\nAdvertisement Library")
    print("----------------------")
    print("1. Advertisement 1")
    print("2. Advertisement 2")
    print("3. Advertisement 3")
    print("4. Test Advertisement")
    print("5. Exit")

    ad_choice = input("\nChoose an advertisement: ")

    if ad_choice == "5":
        pygame.mixer.stop()
        pygame.mixer.quit()
        print("Rwanda Bus Media Player closed.")
        break

    if ad_choice in advertisements:

        current_ad = advertisements[ad_choice]

        print(f"\nSelected: {current_ad}")
        print("Loading advertisement...")

        pygame.mixer.music.load(current_ad)

        print("Advertisement loaded.")

        while True:

            print("\nControls")
            print("--------")
            print("1. Play")
            print("2. Pause")
            print("3. Resume")
            print("4. Stop")
            print("5. Volume")
            print("6. Back to Advertisement Library")

            choice = input("\nChoose an option: ")

            if choice == "1":
                pygame.mixer.music.play()
                print("▶ Advertisement playing.")

            elif choice == "2":
                pygame.mixer.music.pause()
                print("⏸ Advertisement paused.")

            elif choice == "3":
                pygame.mixer.music.unpause()
                print("▶ Advertisement resumed.")

            elif choice == "4":
                pygame.mixer.music.stop()
                print("⏹ Advertisement stopped.")

            elif choice == "5":

                try:
                    volume = float(input("Enter volume (0-100): "))

                    if 0 <= volume <= 100:
                        pygame.mixer.music.set_volume(volume / 100)
                        print(f"🔊 Volume set to {volume}%.")

                    else:
                        print("Please enter a number between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "6":
                pygame.mixer.music.stop()
                print("Returning to Advertisement Library...")
                break

            else:
                print("Invalid option. Please choose 1-6.")

    else:
        print("Invalid advertisement choice.")