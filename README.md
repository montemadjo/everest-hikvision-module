# everest-hikvision-module
A module for interconnection with HikVision cameras

## Restart device
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
