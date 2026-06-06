import sqlite3

DB_NAME = "devices.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS devices(
        mac_address TEXT PRIMARY KEY,
        device_name TEXT,
        ip_address TEXT,
        status TEXT,
        last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def update_device(device):
    conn = connect()

    conn.execute("""
    INSERT INTO devices
    (mac_address, device_name, ip_address, status)
    VALUES(?,?,?,?)
    ON CONFLICT(mac_address)
    DO UPDATE SET
        device_name=excluded.device_name,
        ip_address=excluded.ip_address,
        status='Connected',
        last_seen=CURRENT_TIMESTAMP
    """,
    (
        device["mac"],
        device["name"],
        device["ip"],
        "Connected"
    ))

    conn.commit()
    conn.close()

def mark_disconnected(active_macs):
    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT mac_address FROM devices"
    )

    stored = [row[0] for row in cursor.fetchall()]

    for mac in stored:
        if mac not in active_macs:
            conn.execute("""
            UPDATE devices
            SET status='Disconnected'
            WHERE mac_address=?
            """, (mac,))

    conn.commit()
    conn.close()