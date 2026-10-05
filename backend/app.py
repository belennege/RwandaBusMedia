from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import os


app = Flask(__name__)
CORS(app)

DATABASE = "database/rwanda_bus_media.db"

DASHBOARD_FOLDER = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dashboard"
    )
)


def get_database():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


# ==============================
# PROFESSIONAL DASHBOARD
# ==============================

@app.route("/dashboard")
def dashboard():

    return send_from_directory(
        DASHBOARD_FOLDER,
        "index.html"
    )


# ==============================
# HOME
# ==============================

@app.route("/")
def home():

    return send_from_directory(
        DASHBOARD_FOLDER,
        "index.html"
    )


# ==============================
# SYSTEM STATUS
# ==============================

@app.route("/status")
def status():

    return jsonify({
        "system": "Rwanda Bus Media",
        "status": "ONLINE"
    })


# ==============================
# GET ALL BUSES
# ==============================

@app.route("/buses")
def get_buses():

    connection = get_database()

    buses = connection.execute(
        "SELECT * FROM buses"
    ).fetchall()

    connection.close()

    return jsonify([
        dict(bus)
        for bus in buses
    ])


# ==============================
# CHANGE VOLUME
# ==============================

@app.route(
    "/buses/<bus_id>/volume/<int:volume>",
    methods=["POST"]
)
def change_volume(bus_id, volume):

    if volume < 0 or volume > 100:

        return jsonify({
            "message":
                "Volume must be between 0 and 100."
        }), 400


    connection = get_database()

    connection.execute(
        """
        UPDATE buses
        SET volume = ?
        WHERE bus_id = ?
        """,
        (volume, bus_id)
    )

    connection.commit()

    connection.close()


    return jsonify({

        "message":
            "Volume updated successfully.",

        "bus_id":
            bus_id,

        "volume":
            volume

    })


# ==============================
# CHANGE ADVERTISEMENT
# ==============================

@app.route(
    "/buses/<bus_id>/advertisement/<ad_name>",
    methods=["POST"]
)
def change_advertisement(bus_id, ad_name):

    connection = get_database()

    connection.execute(
        """
        UPDATE buses
        SET current_ad = ?
        WHERE bus_id = ?
        """,
        (ad_name, bus_id)
    )

    connection.commit()

    connection.close()


    return jsonify({

        "message":
            "Advertisement updated successfully.",

        "bus_id":
            bus_id,

        "advertisement":
            ad_name

    })


# ==============================
# STOP BUS
# ==============================

@app.route(
    "/buses/<bus_id>/stop",
    methods=["POST"]
)
def stop_bus(bus_id):

    connection = get_database()

    connection.execute(
        """
        UPDATE buses
        SET current_ad = ?
        WHERE bus_id = ?
        """,
        ("STOPPED", bus_id)
    )

    connection.commit()

    connection.close()


    return jsonify({

        "message":
            "Bus stopped successfully.",

        "bus_id":
            bus_id,

        "status":
            "STOPPED"

    })


# ==============================
# BUS HEARTBEAT
# ==============================

@app.route(
    "/buses/<bus_id>/heartbeat",
    methods=["POST"]
)
def heartbeat(bus_id):

    connection = get_database()

    connection.execute(
        """
        UPDATE buses
        SET status = ?
        WHERE bus_id = ?
        """,
        ("ONLINE", bus_id)
    )

    connection.commit()

    connection.close()


    return jsonify({

        "message":
            "Heartbeat received.",

        "bus_id":
            bus_id,

        "status":
            "ONLINE"

    })


# ==============================
# RUN SERVER
# ==============================

if __name__ == "__main__":

    print("================================")
    print("     RWANDA BUS MEDIA API")
    print("================================")

    print("Server starting...")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )