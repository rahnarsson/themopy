#!/usr/bin/python3

# Communicate with Themo.Io api

import requests
import os
import json
import logging


def __init__ (self, host):
    print('Initiliazing Themo API')
    self.host=host
    self.logger = logging.getLogger(__name__)

def get_token(self, username, password):
    URL = self.host+'/token'

    payload = 'grant_type=password&username={}&password={}'.format(username, password)
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", URL , headers=headers, data = payload)
    json_data = json.loads(response.text)
    self.logger.info('Authenticated succesfully with Themo API')
    return json_data['access_token']    

# Wrapper for all API-requests, returns response.text in JSON-format for easy parsing
def make_request(self, token, uri, payload = {}, files = {}, headers = {}, method='GET'):
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    headers.update(headers)
    url = self.host+uri
    response = requests.request(method, url, headers=headers, data = payload, files = files)
    return json.loads(response.text)

def get_client_info(self, token):
    uri = "/api/clients/me"
    client_info = (self.make_request(token, uri))
    return client_info

def get_devices (self, token):
    info = self.get_client_info(token)
    clientid = info['ID']
    uri = "/api/Devices?ClientID={}&state =false&page =0&pageSize =-1".format(clientid)
    return self.make_request(token, uri)

def get_device_data (self, token, device):
    uri = "/api/devices/{}/data".format(device)
    return self.make_request(token, uri)


def get_device_state (self, token, device):
    uri = "/api/devices/{}/state".format(device)
    return self.make_request(token, uri)

        


        