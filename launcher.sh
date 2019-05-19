#!/bin/sh
# launcher.sh
# navigeer naar project map, haal nieuwe code op en voer python script uit en ga dan terug naar home map.
# Esther & Bastiaan van Dam

cd /
cd home/pi/Documents/projectmax
sudo git pull
sudo python max.py
cd / 
