from hikvision_camera import Camera

from queue import Queue
from threading import Thread
import zmq
import logging
import time
import xmltodict, json
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
IS_EASY_ACCESS = bool(strtobool(config['Basic']['EasyAccess']))
OPPOSITE_SIDE_MASK_TIME = int(config['Basic']['OppositeSideMaskTime'])

REQUEST_TIMEOUT = int(config['Zmq']['Timeout'])
REQUEST_RETRIES = int(config['Zmq']['Retries'])
SERVER_ENDPOINT = config['Zmq']['Endpoint']
UHF_READER_ADDRESS = config['UhfReader']['Address']
UHF_READER_PORT = int(config['UhfReader']['Port'])
CAMERA_ADDRESS = config['Camera']['Address']
CAMERA_USERNAME = config['Camera']['Username']
CAMERA_PASSWORD = config['Camera']['Password']
CAMERA_URL = "http://" + CAMERA_ADDRESS + "/ISAPI/System/IO/outputs/1/trigger"
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
        CAMERA_URL, CAMERA_USERNAME, CAMERA_PASSWORD)
    uhfsender = Sender(
        SENDER_URL)
    # zmq context
    context = zmq.Context()
    logging.info("connecting to server...")
    client = context.socket(zmq.REQ)
    client.connect(SERVER_ENDPOINT)

    data = reader.get_firmware_version()

    print("podaci: " + str(data))

    # reader.disconnect()

    # start scanning for tags
    try:
        q = Queue()
        r_q = Queue()
        q_opener = Queue()
        q_sender = Queue()
        t1 = Thread(target=producer, args=(q, r_q, q_opener, q_sender, reader))
        t2 = Thread(target=consumer, args=(q, r_q))
        t3 = Thread(target=opener, args=(q_opener, ))
        t4 = Thread(target=sender, args=(q_sender, ))

        t1.start()
        t2.start()
        t3.start()
        t4.start()

    except:
        print("EXCEPTION OCCURS!!!")
        sys.exit(1)

    # while True:
    #     clr = reader.clear_reader_buffer()
    #     tgs = reader.scan_for_tags()
    #     # wheather the result is 00 or 01
    #     if tgs is not b'\x00':
    #         #     print(binascii.hexlify(bytearray(tgs)))
    #         # else:
    #         tag = reader.get_tag_data()
    #         print(binascii.hexlify(bytearray(tag)))
    #     time.sleep(0.1)

    # reader.disconnect()

    print("started!")