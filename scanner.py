from scapy.all import ARP, Ether, srp
import socket
import psutil
import ipaddress


import psutil
import ipaddress

def get_network():

    for interface, addresses in psutil.net_if_addrs().items():

        for addr in addresses:

            if addr.family == 2:

                ip = addr.address
                mask = addr.netmask

                if (
                    ip != "127.0.0.1"
                    and not ip.startswith("169.254.")
                ):

                    network = ipaddress.IPv4Network(
                        f"{ip}/{mask}",
                        strict=False
                    )

                    return str(network)

    return None


def scan_network():
    """
    Scan the detected LAN network using ARP.
    """

    network = get_network()

    if not network:
        print("Unable to detect network.")
        return []

    print(f"Scanning Network: {network}")

    arp = ARP(pdst=network)

    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether / arp

    result = srp(
        packet,
        timeout=3,
        verbose=0
    )[0]

    devices = []

    for sent, received in result:

        try:
            hostname = socket.gethostbyaddr(
                received.psrc
            )[0]
        except:
            hostname = "Unknown"

        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "name": hostname
        })

    return devices