#!/bin/sh
# launcher.sh
# navigeer naar project map, voer python script uit en ga dan terug naar home map.

cd /
cd home/pi/Documents/projectmax
git pull
sudo python max.py
cd / 
