import psutil

for interface, addresses in psutil.net_if_addrs().items():
    print("\nInterface:", interface)

    for addr in addresses:
        print("  Family:", addr.family)
        print("  Address:", addr.address)
        print("  Netmask:", addr.netmask)