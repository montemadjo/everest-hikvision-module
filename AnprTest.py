from hikvision_camera import Camera
from hikvision_camera import Sender

from datetime import datetime
from queue import Queue
from threading import Thread
import zmq
import logging
import time
import xmltodict
import json
import configparser
import argparse

import sys
import os
from distutils.util import strtobool

parser = argparse.ArgumentParser()
parser.add_argument("config", help="path to configuration file")
args = parser.parse_args()

config_path = args.config

print("config path")
print(config_path)

# load the configuration file
config = configparser.ConfigParser()
config.read(config_path)

MY_ID = int(config['Basic']['Id'])
INTERVAL = int(config['Basic']['Interval'])

CAMERA_ADDRESS = config['Camera']['Address']
CAMERA_USERNAME = config['Camera']['Username']
CAMERA_PASSWORD = config['Camera']['Password']

SENDER_URL = config['Remote']['SenderUrl']

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


if __name__ == '__main__':
    # camera = Camera('192.168.1.152', 'admin', 'Tfs123456')

    # r = camera.getAnprPlates()

    # xml = r.content.decode("utf-8")

    # # print(xml)

    #

    # o = xmltodict.parse(xml)
    # f = json.dumps(o) # '{"e": {"a": ["text", "text"]}}'
    # print(f)

    camera = Camera(
        CAMERA_ADDRESS, CAMERA_USERNAME, CAMERA_PASSWORD)
    uhfsender = Sender(
        SENDER_URL)

    r = camera.getAnprPlates()
    xml = r.content.decode("utf-8")
    o = xmltodict.parse(xml)
    j = json.dumps(o)

    print(j)

    # svakih x sekundi treba da se iščitaju podaci sa kamere,
    # i da se aploaduju na cloud
