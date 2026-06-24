import subprocess
import urllib.request
import urllib.error
import json

jwt_token = None

def login():

    global jwt_token

    email = input("Email: ")
    password = input("Password: ")

    payload = json.dumps({
        "email": email,
        "password": password
    }).encode()

    request = urllib.request.Request(
        "https://api.flight-watch.xyz/api/v1/auth/login",
        data=payload,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:

        response = urllib.request.urlopen(request)

        data = json.loads(
            response.read().decode()
        )

        jwt_token = data["token"]

        print()
        print("=" * 40)
        print(" Login Successful")
        print("=" * 40)
        print()
        print(f"Welcome : {data['user']['name']}")
        print(f"Email   : {data['user']['email']}")
        print()

    except Exception as e:

        print()
        print("Login Failed")
        print(e)
        print()

    input("Press Enter to continue...")


def show_analytics():

    global jwt_token

    if not jwt_token:

        print()
        print("Please login first.")
        print()

        input("Press Enter to continue...")
        return

    request = urllib.request.Request(
        "https://api.flight-watch.xyz/api/v1/analytics",
        headers={
            "Authorization": f"Bearer {jwt_token}"
        }
    )

    try:

        response = urllib.request.urlopen(request)

        data = json.loads(
            response.read().decode()
        )

        analytics = data["analytics"]

        print()
        print("=" * 40)
        print("     FlightWatch Analytics")
        print("=" * 40)
        print()

        print(f"Total Sightings  : {analytics['totalSightings']}")
        print(f"Unique Aircraft  : {analytics['uniqueAircraft']}")
        print(f"Unique Airlines  : {analytics['uniqueAirlines']}")
        print(f"Airports Visited : {analytics['airportsVisited']}")
        print()
        print(f"Top Airline      : {analytics['mostFrequentAirline']}")
        print(f"Top Aircraft     : {analytics['mostFrequentType']}")
        print()

    except Exception as e:

        print()
        print("Analytics Request Failed")
        print(e)
        print()

    input("Press Enter to continue...")

def show_aircraft_stats():

    global jwt_token

    if not jwt_token:

        print()
        print("Please login first.")
        print()

        input("Press Enter to continue...")
        return

    request = urllib.request.Request(
        "https://api.flight-watch.xyz/api/v1/aircraft",
        headers={
            "Authorization": f"Bearer {jwt_token}"
        }
    )

    try:

        response = urllib.request.urlopen(request)

        data = json.loads(
            response.read().decode()
        )

        print()
        print("=" * 40)
        print("      Aircraft Statistics")
        print("=" * 40)
        print()

        for aircraft in data["aircraft"]:

            print(f"Aircraft  : {aircraft['name']}")
            print(f"Sightings : {aircraft['count']}")
            print(f"Last Seen : {aircraft['last_seen']}")
            print("-" * 40)

        print()

    except Exception as e:

        print()
        print("Aircraft Statistics Request Failed")
        print(e)
        print()

    input("Press Enter to continue...")


def show_airline_stats():

    global jwt_token

    if not jwt_token:

        print()
        print("Please login first.")
        print()

        input("Press Enter to continue...")
        return

    request = urllib.request.Request(
        "https://api.flight-watch.xyz/api/v1/airlines",
        headers={
            "Authorization": f"Bearer {jwt_token}"
        }
    )

    try:

        response = urllib.request.urlopen(request)

        data = json.loads(
            response.read().decode()
        )

        print()
        print("=" * 40)
        print("       Airline Statistics")
        print("=" * 40)
        print()

        for airline in data["airlines"]:

            print(f"Airline   : {airline['name']}")
            print(f"Sightings : {airline['count']}")
            print(f"Last Seen : {airline['last_seen']}")
            print("-" * 40)

        print()

    except Exception as e:

        print()
        print("Airline Statistics Request Failed")
        print(e)
        print()

    input("Press Enter to continue...")


def show_airport_stats():

    global jwt_token

    if not jwt_token:

        print()
        print("Please login first.")
        print()

        input("Press Enter to continue...")
        return

    request = urllib.request.Request(
        "https://api.flight-watch.xyz/api/v1/airports",
        headers={
            "Authorization": f"Bearer {jwt_token}"
        }
    )

    try:

        response = urllib.request.urlopen(request)

        data = json.loads(
            response.read().decode()
        )

        print()
        print("=" * 40)
        print("       Airport Statistics")
        print("=" * 40)
        print()

        for airport in data["airports"]:

            print(f"Airport   : {airport['name']}")
            print(f"Sightings : {airport['count']}")
            print(f"Last Seen : {airport['last_seen']}")
            print("-" * 40)

        print()

    except Exception as e:

        print()
        print("Airport Statistics Request Failed")
        print(e)
        print()

    input("Press Enter to continue...")

def show_flightwatch_status():
    try:
        response = urllib.request.urlopen(
            "https://api.flight-watch.xyz/api/v1/health"
        )

        data = json.loads(
            response.read().decode()
        )

        print()
        print("=" * 40)
        print("      FlightWatch Status")
        print("=" * 40)
        print()
        print(f"API Status : {data['status']}")
        print(f"Database   : {data['database']}")
        print(f"Timestamp  : {data['timestamp']}")
        print()

    except Exception as e:
        print()
        print("FlightWatch Health Check Failed")
        print(e)
        print()

    input("Press Enter to continue...")
def show_system_info():
    hostname = subprocess.check_output(
        ["hostname"]
    ).decode().strip()

    user = subprocess.check_output(
        ["whoami"]
    ).decode().strip()

    os_name = subprocess.check_output(
        ["uname", "-s"]
    ).decode().strip()

    print()
    print(f"Hostname : {hostname}")
    print(f"User     : {user}")
    print(f"OS       : {os_name}")
    print()

    input("Press Enter to continue...")


def show_disk_usage():
    disk_usage = subprocess.check_output(
        ["df", "-h"]
    ).decode()

    print()
    print(disk_usage)

    input("Press Enter to continue...")


def show_memory_usage():
    memory_usage = subprocess.check_output(
        ["free", "-h"]
    ).decode()

    print()
    print(memory_usage)

    input("Press Enter to continue...")


def show_processes():
    running_processes = subprocess.check_output(
        ["ps", "aux"]
    ).decode()

    lines = running_processes.splitlines()

    print()

    for line in lines[:10]:
        print(line)

    print()

    input("Press Enter to continue...")


def show_network_info():
    network_info = subprocess.check_output(
        ["ip", "addr"]
    ).decode()

    print()
    print(network_info)

    input("Press Enter to continue...")


print("-" * 88)
print(r"""

███████╗██╗     ██╗ ██████╗ ██╗  ██╗████████╗██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗
██╔════╝██║     ██║██╔════╝ ██║  ██║╚══██╔══╝██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║
█████╗  ██║     ██║██║  ███╗███████║   ██║   ██║ █╗ ██║███████║   ██║   ██║     ███████║
██╔══╝  ██║     ██║██║   ██║██╔══██║   ██║   ██║███╗██║██╔══██║   ██║   ██║     ██╔══██║
██║     ███████╗██║╚██████╔╝██║  ██║   ██║   ╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║
╚═╝     ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝

               ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗
              ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║
              ██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║
              ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║
              ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗
               ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝

""")
print("-" * 88)
print()
print()

while True:
    print("1. FlightWatch Health Status")
    print("2. Operator Login")
    print("3. Analytics Dashboard")
    print("4. Aircraft Statistics")
    print("5. Airline Statistics")
    print("6. Airport Statistics")
    print("7. System Information")
    print("8. Memory Usage")
    print("9. Running Processes")
    print("10. Network Information")
    print("11. Exit")
    print()

    choice = input("Select option: ")

    if choice == "1":
        show_flightwatch_status()

    elif choice == "2":
        login()

    elif choice == "3":
        show_analytics()

    elif choice == "4":
        show_aircraft_stats()

    elif choice == "5":
        show_airline_stats()

    elif choice == "6":
        show_airport_stats()

    elif choice == "7":
        show_system_info()

    elif choice == "8":
        show_memory_usage()

    elif choice == "9":
        show_processes()

    elif choice == "10":
        show_network_info()

    elif choice == "11":
        print("Exiting FlightWatch Ground Control")
        break
