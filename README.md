# everest-hikvision-module
A module for interconnection with HikVision cameras

## Restart device
```
#!/bin/bash
SERVICE=$1
while [ true ]; do
if ps aux | grep $1 | grep -v grep | grep -v bash > /dev/null
then
        : #echo "$(date): $SERVICE is running"
else
        echo "$(date): $SERVICE is stopped"
        python3 /home/pi/Documents/prod/$SERVICE/run.py $2 &
        echo "$(date): restart app!"
fi
sleep 3
done
```

## Autostart
run
```
cd /home/pi/.config/autostart/
```
U njemu su:
backender.desktop
```
[Desktop Entry]
Type=Application
Name=Clock
Exec=/usr/bin/lxterminal -e 'bash /home/pi/Documents/prod/restart0.sh everest-plc-ac-backender/everest-plc-ac-backender /home/pi/Documents/prod/config-backender.ini'

```
cam0.desktop
```
[Desktop Entry]
Type=Application
Name=cam0
Exec=/usr/bin/lxterminal -e 'bash /home/pi/Documents/prod/restart0.sh cam0/everest-hikvision-module /home/pi/Documents/prod/config-cam0.ini'
```
cam1.desktop
```
[Desktop Entry]
Type=Application
Name=cam1
Exec=/usr/bin/lxterminal -e 'bash /home/pi/Documents/prod/restart0.sh cam1/everest-hikvision-module /home/pi/Documents/prod/config-cam1.ini'

```
uhf0.desktop
```
[Desktop Entry]
Type=Application
Name=uhfi0
Exec=/usr/bin/lxterminal -e 'bash /home/pi/Documents/prod/restart0.sh i0/everest-uhf-module /home/pi/Documents/prod/config-uhf-i0.ini'

```
uhf1.desktop
```
[Desktop Entry]
Type=Application
Name=uhfi1
Exec=/usr/bin/lxterminal -e 'bash /home/pi/Documents/prod/restart0.sh i1/everest-uhf-module /home/pi/Documents/prod/config-uhf-i1.ini'
```

