import time

from scanner import scan_network

from database import (
    update_device,
    mark_disconnected
)



def start_monitoring():

    while True:

        print("\nScanning Network...\n")

        devices = scan_network()

        active_macs = []

        for device in devices:

            update_device(device)

            active_macs.append(
                device["mac"]
            )

            print(device)

        mark_disconnected(
            active_macs
        )

        print(
            f"Devices Found: {len(devices)}"
        )

        time.sleep(10)