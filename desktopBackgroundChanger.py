"""
windows desktop changer(get image from a source, random change it)
"""

import ctypes
import time
from pathlib import Path

import schedule
from PIL import Image
import random
import datetime


def check_image(p):
    try:
        Image.open(p)
        return True
    except IOError:
        return False


def change_background(item):
    print(datetime.datetime.now(), str(item))
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 1
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(item), SPIF_UPDATEINIFILE)


def job(files_grabbed):
    item = random.choice(files_grabbed)
    change_background(item)


def initList():
    files_grabbed = []
    for path in Path('E:\\Nikon').rglob('*.*'):
        if check_image(path):
            files_grabbed.append(path)
    return files_grabbed


images = initList()
schedule.every(10).to(30).seconds.do(job, images)
while True:
    schedule.run_pending()
    time.sleep(1)
