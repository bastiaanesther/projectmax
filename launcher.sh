#!/bin/sh
# launcher.sh
# navigeer naar project map, haal nieuwe code op en voer python script uit en ga dan terug naar home map.

COUNTER=0
while ! ping -c 1 -W 1 github.com; do
	echo "Wachten op github.com - Mogelijk nog niet verbonden met internet"
	sleep 1

	COUNTER=$((COUNTER + 1))
	echo $COUNTER

	if $COUNTER > 30; then 
		break
	fi 
done

cd /
cd home/pi/Documents/projectmax
sudo -u pi -i git --git-dir=/home/pi/Documents/projectmax/.git --work-tree=/home/pi/Documents/projectmax fetch origin
sudo -u pi -i git --git-dir=/home/pi/Documents/projectmax/.git --work-tree=/home/pi/Documents/projectmax/ pull
sudo python max.py
cd / 
