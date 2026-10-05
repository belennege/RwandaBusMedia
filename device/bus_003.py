import requests
import pygame
import time
import os


API_URL = "http://127.0.0.1:5000"

BUS_ID = "BUS-003"

AUDIO_FOLDER = "audio/advertisements"


pygame.mixer.init()

last_advertisement = None


def send_heartbeat():

    response = requests.post(
        f"{API_URL}/buses/{BUS_ID}/heartbeat"
    )

    if response.status_code == 200:

        print("Heartbeat sent: BUS ONLINE")


def get_bus_information():

    response = requests.get(
        f"{API_URL}/buses"
    )

    buses = response.json()

    for bus in buses:

        if bus["bus_id"] == BUS_ID:

            return bus

    return None


def play_advertisement(advertisement):

    global last_advertisement

    audio_file = os.path.join(
        AUDIO_FOLDER,
        advertisement
    )

    if not os.path.exists(audio_file):

        print("Advertisement file not found:")
        print(audio_file)

        return


    print()
    print("Playing advertisement:")
    print(advertisement)


    pygame.mixer.music.load(audio_file)

    pygame.mixer.music.play()

    last_advertisement = advertisement


def stop_audio():

    global last_advertisement

    print()
    print("Stopping advertisement...")

    pygame.mixer.music.stop()

    last_advertisement = "STOPPED"


print("================================")
print("       BUS-003 DEVICE")
print("================================")

print("Bus device started.")
print("Waiting for commands...")


while True:

    try:

        send_heartbeat()

        bus = get_bus_information()


        if bus:

            print()

            print("Bus:", bus["bus_id"])

            print("Route:", bus["route"])

            print(
                "Volume:",
                str(bus["volume"]) + "%"
            )

            print(
                "Advertisement:",
                bus["current_ad"]
            )


            pygame.mixer.music.set_volume(
                bus["volume"] / 100
            )


            if bus["current_ad"] == "STOPPED":

                if last_advertisement != "STOPPED":

                    stop_audio()


            elif bus["current_ad"] != last_advertisement:

                play_advertisement(
                    bus["current_ad"]
                )


        else:

            print(
                "Bus information not found."
            )


        print("\nChecking API again...")

        time.sleep(5)


    except requests.exceptions.ConnectionError:

        print(
            "Server unavailable. Retrying..."
        )

        time.sleep(5)