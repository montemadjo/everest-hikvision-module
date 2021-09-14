from queue import Queue
from threading import Thread
from hikvision_camera import Camera
import configparser
import time

# load configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# read the configuration
URL = config['Remote']['URL']
username = config['Basic']['Username']
password = config['Basic']['Password']

if __name__ == '__main__':
    camera = Camera(URL, username, password)
    camera.postOutputRequest(1)
    time.sleep(1)
    camera.postOutputRequest(0)