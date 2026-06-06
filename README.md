# LAN Device Discovery and Monitoring System

## Overview

This project is a Python-based LAN Device Discovery and Monitoring System.

The application discovers devices connected to the same Local Area Network (LAN), collects their:

* Device Name
* IP Address
* MAC Address

and stores the information in a SQLite database.

The system continuously monitors the network and automatically updates the database when:

* A new device joins the network
* A device disconnects from the network
* A device's IP address changes

---

## Features

* Automatic LAN Device Discovery
* IP Address Detection
* MAC Address Detection
* Hostname Resolution
* SQLite Database Storage
* Continuous Network Monitoring
* Device Connection Tracking
* Device Disconnection Tracking
* IP Change Detection

---

## Technologies Used

* Python 3
* Scapy
* SQLite
* Socket Programming
* Psutil
* IPAddress Module

---

## Project Structure

```text
LAN-Device-Monitor
│
├── main.py
├── scanner.py
├── database.py
├── monitor.py
├── requirements.txt
├── README.md
└── devices.db
```

---

## Installation

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install scapy
pip install psutil
```

---

## Running the Application

```bash
python main.py
```

Example Output:

```text
Scanning Network: 10.36.88.0/24

{'ip': '10.36.88.63',
 'mac': '50:c2:e8:1b:37:f3',
 'name': 'Murugesh'}

Devices Found: 2
```

---

## Database Design

Database File:

```text
devices.db
```

Table:

```sql
devices
```

Columns:

| Column      | Description              |
| ----------- | ------------------------ |
| mac_address | Unique device identifier |
| device_name | Hostname of device       |
| ip_address  | Current IP Address       |
| status      | Connected / Disconnected |
| last_seen   | Last detected timestamp  |

### Why MAC Address is Primary Key?

IP addresses may change due to DHCP.

MAC addresses remain unique for each network device.

Therefore the MAC address is used as the primary key to avoid duplicate device records and correctly track IP changes.

---

## Initial Implementation (Hardcoded Network)

Initially, the application used a hardcoded subnet:

```python
NETWORK = "192.168.1.0/24"
```

or

```python
NETWORK = "10.86.66.0/24"
```

### Limitations

* Works only on a specific network.
* Requires source code changes when switching networks.
* Reduces portability and maintainability.

This approach was useful during early testing but was not suitable for a general-purpose solution.

---

## Improved Implementation (Loose Coupling)

To improve flexibility, the subnet detection was decoupled from the scanning logic.

Instead of hardcoding the network range, the application:

1. Detects the active network interface.
2. Retrieves the IPv4 address.
3. Retrieves the subnet mask.
4. Calculates the network automatically.

Example:

```text
IP Address : 10.36.88.63
Subnet Mask: 255.255.255.0
```

Automatically generates:

```text
10.36.88.0/24
```

### Benefits

* No manual configuration required.
* Works across different LAN environments.
* More reusable and maintainable.
* Demonstrates loose coupling and modular design.

---

## Software Design Principles

### Separation of Concerns

The project is divided into multiple modules:

#### scanner.py

Responsible only for network scanning.

#### database.py

Responsible only for database operations.

#### monitor.py

Responsible only for monitoring and change detection.

#### main.py

Application entry point.

This design makes the code easier to maintain and extend.

---

### Loose Coupling

Each module performs a specific task and depends minimally on other modules.

Benefits:

* Easier testing
* Better maintainability
* Simplified debugging
* Improved scalability

Example:

scanner.py discovers devices.

database.py stores devices.

monitor.py coordinates the workflow.

Each component can be modified independently without affecting the entire system.

---

## How the Application Works

### Step 1

Detect active network interface.

### Step 2

Calculate subnet range automatically.

### Step 3

Send ARP broadcast packets.

### Step 4

Receive responses from active devices.

### Step 5

Extract:

* IP Address
* MAC Address
* Hostname

### Step 6

Store information in SQLite database.

### Step 7

Rescan periodically.

### Step 8

Update database when changes are detected.

---

## Device Monitoring Logic

### New Device Detection

If a device appears that is not present in the database:

Action:

* Insert new record.

### Device Disconnection

If a previously known device no longer appears:

Action:

* Update status to Disconnected.

### IP Address Change

If the same MAC address appears with a different IP:

Action:

* Update the existing database record.

---

## Networking Concepts Used

This project applies several networking concepts:

* ARP (Address Resolution Protocol)
* IPv4 Addressing
* MAC Addressing
* Subnetting
* LAN Communication
* DHCP-based IP Allocation

---

## Academic Concepts Used

### Python Programming

* Functions
* Loops
* Dictionaries
* Exception Handling
* Modules

### Computer Networks

* ARP
* IP Addressing
* MAC Addressing
* Subnet Masks
* Gateways

### Database Management Systems

* SQLite
* SQL Queries
* Primary Keys
* Insert and Update Operations

### Software Engineering

* Modular Design
* Loose Coupling
* Separation of Concerns
* Maintainability

---

## Future Enhancements

* Automatic Event Logging
* Flask Web Dashboard
* CSV Export
* Email Notifications
* REST API
* Docker Deployment

---

## Conclusion

This project successfully discovers LAN devices, stores device information in SQLite, and continuously monitors network changes.

The application evolved from a hardcoded subnet implementation to a loosely coupled automatic subnet detection mechanism, resulting in a more flexible, maintainable, and production-oriented solution.
