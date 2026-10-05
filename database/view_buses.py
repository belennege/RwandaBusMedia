import sqlite3

DATABASE = "database/rwanda_bus_media.db"

connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()

cursor.execute("""
    SELECT bus_id, route, status, volume, current_ad
    FROM buses
""")

buses = cursor.fetchall()

print("================================")
print("       RWANDA BUS DATABASE")
print("================================")

for bus in buses:

    print("\nBus ID:", bus[0])
    print("Route:", bus[1])
    print("Status:", bus[2])
    print("Volume:", str(bus[3]) + "%")
    print("Current Advertisement:", bus[4])

connection.close()