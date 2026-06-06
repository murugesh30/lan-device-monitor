from scapy.all import ARP, Ether, srp

target = "192.168.1.0/24"  # replace with your network

arp = ARP(pdst=target)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether / arp

result = srp(packet, timeout=3, verbose=False)[0]

print("Found devices:")

for sent, received in result:
    print(received.psrc, received.hwsrc)