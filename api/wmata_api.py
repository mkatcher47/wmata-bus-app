import requests
import json
from utils.config import WMATA_API_KEY, WMATA_BASE_URL

class WMATAAPI:
    def __init__(self):
        self.api_key = WMATA_API_KEY
        self.base_url = WMATA_BASE_URL

    def get_nearby_stops(self, lat, lon, radius=500):
        """
        Fetches nearby bus stops within a given radius of the user's location.

        Args:
            lat (float): Latitude of the user's location.
            lon (float): Longitude of the user's location.
            radius (int): Search radius in meters (default: 500).

        Returns:
            list: List of nearby bus stops with details.
        """
        url = f"{self.base_url}/Bus.svc/json/jStops"
        params = {
            "Lat": lat,
            "Lon": lon,
            "Radius": radius,
        }
        headers = {"api_key": self.api_key}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("Stops", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching nearby stops: {e}")
            return []

    def get_next_buses(self, stop_id):
        """
        Fetches the next buses arriving at a specific stop.

        Args:
            stop_id (str): The ID of the bus stop.

        Returns:
            list: List of upcoming buses with their arrival times.
        """
        url = f"{self.base_url}/NextBusService.svc/json/jPredictions"
        params = {"StopID": stop_id}
        headers = {"api_key": self.api_key}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("Predictions", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching next buses: {e}")
            return []
