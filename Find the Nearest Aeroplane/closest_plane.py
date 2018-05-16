import json
import sys
import urllib.request
from math import radians, cos, sin, asin, sqrt

jfk = (-73.7822, 40.6442)
et = (2.2945, 48.8580)
location_dct = {1: jfk, 2: et}


def getting_data():
    urlData = "https://opensky-network.org/api/states/all"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    json_data = json.loads(data.decode(encoding))
    return json_data


def calculate_dst(plane_position, point_position):
    plane_lon, plane_lat = [radians(x) for x in plane_position]
    point_lon, point_lat = [radians(x) for x in point_position]
    dlon = point_lon - plane_lon
    dlat = point_lat - plane_lat
    a = sin(dlat / 2) ** 2 + cos(plane_lat) * cos(point_lat) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km


def searching_minimal_distance(point_position):
    result = ""
    flight_positions = getting_data()["states"]
    for flight in flight_positions:
        if isinstance(flight[5], float) and isinstance(flight[6], float):
            flight.append((calculate_dst((flight[5], flight[6]), point_position)))
            if result == "" or flight[17] < result[17]:
                result = flight

    return result


def display_closest_plane(location):
    flight = searching_minimal_distance(location)
    print("""
    Closest plane to {} longitude and {} altitude
    Geodesic distance: {:.2f}km
    Callsign: {}
    Longitude and Lattitude: {}, {}
    Geometric Altitude: {}m
    Country of origin: {}
    ICAO24 ID: {}\n""".format(location[0], location[1], flight[17], flight[1], flight[5], flight[6], flight[7],
                              flight[2], flight[0])
          )


def main():
    while True:
        print("Choose location to search for nearest plane: ")
        print("1. JFK: " + str(location_dct[1]))
        print("2. Eiffel Tower: " + str(location_dct[2]))
        print("3. Custom location")
        print("4. Quit")
        choice = input(">")
        if choice == "1":
            display_closest_plane(location_dct[1])
        elif choice == "2":
            display_closest_plane(location_dct[2])
        elif choice == "3":
            location = [float(item) for item in input("Please enter longitude and latitude: ").split(" ")]
            display_closest_plane(location)
        elif choice == "4":
            sys.exit()


if __name__ == "__main__":
    main()
