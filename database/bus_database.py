import sqlite3

DATABASE = "database/rwanda_bus_media.db"


def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS buses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bus_id TEXT UNIQUE NOT NULL,
            route TEXT NOT NULL,
            status TEXT NOT NULL,
            volume INTEGER NOT NULL,
            current_ad TEXT
        )
    """)

    connection.commit()
    connection.close()

    print("Database created successfully!")


def add_buses():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    buses = [
        (
            "BUS-001",
            "Nyarugenge → Kanombe",
            "ONLINE",
            70,
            "ad_01.mp3"
        ),

        (
            "BUS-002",
            "Kicukiro → City Centre",
            "ONLINE",
            50,
            "ad_02.mp3"
        ),

        (
            "BUS-003",
            "Kimironko → Nyabugogo",
            "OFFLINE",
            60,
            "ad_03.mp3"
        )
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO buses
        (bus_id, route, status, volume, current_ad)
        VALUES (?, ?, ?, ?, ?)
    """, buses)

    connection.commit()
    connection.close()

    print("Buses added successfully!")


if __name__ == "__main__":

    create_database()
    add_buses()