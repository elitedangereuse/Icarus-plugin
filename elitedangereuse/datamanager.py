import requests
import json

from elitedangereuse.constants import RequestMethod
from elitedangereuse.httprequestmanager import EliteDangereuseRequest
from elitedangereuse.debug import Debug

SERVER_URL = "https://ship.elitedangereuse.fr:5000/endpoint"

class DataManager:
    def __init__(self, elitedangereuse):
        self.elitedangereuse = elitedangereuse

        self.send_init_data()

    def send_init_data(self):
        headers = {"Content-Type": "application/json"}
        payload = {
            "info": "Icarus plugin has started",
        }
        self.elitedangereuse.request_manager.queue_request(
            SERVER_URL,
            RequestMethod.POST,
            callback=None,
            params={},
            headers={"Content-Type": "application/json"},
            stream=False,
            payload=payload
        )


    def send_data(self, cmdr, info):
        headers = {"Content-Type": "application/json"}
        payload = {
            "cmdr": cmdr,
            "info": info,
        }

        self.elitedangereuse.request_manager.queue_request(
            SERVER_URL,
            RequestMethod.POST,
            callback=None,
            params={},
            headers={"Content-Type": "application/json"},
            stream=False,
            payload=payload
        )
