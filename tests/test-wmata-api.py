if __name__ == "__main__":
    from utils.config import WMATA_API_KEY

    # Instantiate the WMATAAPI class
    wmata = WMATAAPI()

    # Example: Find stops near a location
    latitude = 38.8895  # Example: Washington Monument
    longitude = -77.0352
    stops = wmata.get_nearby_stops(latitude, longitude)
    print("Nearby Stops:", stops)

    # Example: Get next buses for a stop
    if stops:
        first_stop_id = stops[0]["StopID"]
        buses = wmata.get_next_buses(first_stop_id)
        print("Next Buses at Stop:", buses)
