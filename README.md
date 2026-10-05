# Rwanda Bus Media

## Overview

Rwanda Bus Media is a bus-based digital advertising and media management system designed to remotely control advertisements and audio playback across multiple buses.

The system connects a central Flask API, database, bus device simulators, audio advertisements, and a web-based control dashboard.

## Main Features

- Centralised bus management
- Multiple bus device support
- Remote advertisement selection
- Remote advertisement playback
- Stop advertisement control
- Remote volume control
- Bus online/offline heartbeat monitoring
- SQLite database
- REST API
- Web-based control dashboard
- Local MP3 advertisement playback
- Three simulated buses
- Three advertisement files

## System Components

### Backend API

The Flask backend provides REST API endpoints for:

- Retrieving buses
- Updating advertisement assignments
- Updating volume
- Sending bus heartbeats
- Controlling bus media states

### Bus Devices

The project currently simulates three buses:

| Bus | Route | Advertisement |
|---|---|---|
| BUS-001 | Nyarugenge → Kanombe | ad_01.mp3 |
| BUS-002 | Kicukiro → City Centre | ad_02.mp3 |
| BUS-003 | Kimironko → Nyabugogo | ad_03.mp3 |

Each bus device communicates with the Flask API and periodically sends a heartbeat to report that it is online.

### Dashboard

The web dashboard provides a central interface for controlling the buses.

The dashboard allows the user to:

- View bus status
- View bus routes
- Select advertisements
- Play advertisements
- Stop advertisements
- Change volume levels
- Monitor the current media state

## Technologies Used

- Python
- Flask
- SQLite
- Pygame
- HTML
- CSS
- JavaScript
- REST API
- PowerShell
- Git
- GitHub

## Project Structure

```text
RwandaBusMedia/
│
├── audio/
│   └── advertisements/
│       ├── ad_01.mp3
│       ├── ad_02.mp3
│       └── ad_03.mp3
│
├── backend/
│   └── app.py
│
├── bus_player/
│   ├── audio_player.py
│   ├── controller.py
│   └── playlist_player.py
│
├── buses/
│   └── bus_manager.py
│
├── dashboard/
│   └── index.html
│
├── database/
│   ├── bus_database.py
│   ├── rwanda_bus_media.db
│   └── view_buses.py
│
├── device/
│   ├── bus_device.py
│   ├── bus_002.py
│   └── bus_003.py
│
├── frontend/
│   └── index.html
│
├── playlists/
│   └── default_playlist.txt
│
├── tests/
│   └── test_python.py
│
├── docs/
├── .gitignore
└── README.md