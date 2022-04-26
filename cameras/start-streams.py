#!/usr/bin/python3

import os

with open('/home/pi/companion/cameras/gstreams.txt', 'r') as file:
    lines = file.readlines()

for idx, line in enumerate(lines):
    print(line)
    os.system(f'sudo -H -u pi screen -dm -S video{idx} /home/pi/companion/cameras/stream.py {line}')
