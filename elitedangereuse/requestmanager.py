import certifi
import requests
import json
import time
import random

from elitedangereuse.debug import Debug

SERVER_URL = "https://ship.elitedangereuse.fr:5000/endpoint"

class RequestManager:
    def __init__(self, elitedangereuse):
        print("Sending dummy spaceship status to server...")
        print(certifi.where())
        # self.send_dummy_data()
        self.send_init_data()

    # Function to generate a random payload
    def generate_random_payload(self):
        return {
            "cmdr": "Jameson",
            "ship_name": "Python",  # Keep ship name constant, or you can randomize this too
            "hull_health": random.randint(
                50, 100
            ),  # Random hull health between 50 and 100
            "shield_health": random.randint(
                50, 100
            ),  # Random shield health between 50 and 100
            "fuel_level": random.randint(
                0, 100
            ),  # Random fuel level between 0 and 100
            "location": random.choice(
                ["Lave System", "Sol System", "Mars Orbit", "Alpha Centauri"]
            ),  # Random location choice
        }


    def send_dummy_data(self):
        headers = {"Content-Type": "application/json"}
        try:
            # Generate a new random payload
            dummy_payload = self.generate_random_payload()

            # Send a POST request with the random payload
            response = requests.post(
                SERVER_URL, json=dummy_payload, headers=headers, verify=True
            )
            response.raise_for_status()  # Raise an error on bad status
            print("Data sent successfully:", response.json())
        except requests.RequestException as e:
            print(f"Failed to send data: {e}")


    def send_init_data(self):
        headers = {"Content-Type": "application/json"}
        try:
            # Generate a new random payload
            payload = {
                "cmdr": "Jameson",
                "info": "has joined",
            }

            # Send a POST request with the random payload
            response = requests.post(
                SERVER_URL, json=payload, headers=headers, verify=True
            )
            response.raise_for_status()  # Raise an error on bad status
            print("Data sent successfully:", response.json())
        except requests.RequestException as e:
            print(f"Failed to send data: {e}")

    def send_data(self, cmdr, info):
        headers = {"Content-Type": "application/json"}
        try:
            # Generate a new random payload
            payload = {
                "cmdr": cmdr,
                "info": info,
            }

            # Send a POST request with the random payload
            response = requests.post(
                SERVER_URL, json=payload, headers=headers, verify=True
            )
            response.raise_for_status()  # Raise an error on bad status
            print("Data sent successfully:", response.json())
        except requests.RequestException as e:
            print(f"Failed to send data: {e}")
