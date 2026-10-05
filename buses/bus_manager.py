buses = {
    "BUS-001": {
        "route": "Nyarugenge → Kanombe",
        "status": "ONLINE",
        "volume": 70,
        "current_ad": "ad_01.mp3"
    },

    "BUS-002": {
        "route": "Kicukiro → City Centre",
        "status": "ONLINE",
        "volume": 50,
        "current_ad": "ad_02.mp3"
    },

    "BUS-003": {
        "route": "Kimironko → Nyabugogo",
        "status": "OFFLINE",
        "volume": 60,
        "current_ad": "ad_03.mp3"
    }
}


print("================================")
print("       RWANDA BUS MEDIA")
print("================================")

print("\nRegistered Buses")
print("----------------")

for bus_id, bus in buses.items():

    print(f"\nBus: {bus_id}")
    print(f"Route: {bus['route']}")
    print(f"Status: {bus['status']}")
    print(f"Volume: {bus['volume']}%")
    print(f"Current Advertisement: {bus['current_ad']}")