#!/bin/sh
# launcher.sh
# navigeer naar project map, haal nieuwe code op en voer python script uit en ga dan terug naar home map.

cd /
cd home/pi/Documents/projectmax
sudo -u pi -i git --git-dir=/home/pi/Documents/projectmax/.git --work-tree=/home/pi/Documents/project max fetch origin
sudo -u pi -i git --git-dir=/home/pi/Documents/projectmax/.git --work-tree=/home/pi/Documents/projectmax/ pull
sudo python max.py
cd / 
