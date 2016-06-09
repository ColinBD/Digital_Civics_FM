#/!bin/bash

if ! ps -e | grep epiphany > /dev/null
then
    export XAUTHORITY="/home/pi/.Xauthority"
    export DISPLAY=:0.0
    echo "DISPLAY is $DISPLAY"
    epiphany-browser -a --profile /home/pi/.config http://127.0.0.1/index.html & sleep 5 && xdotool mousemove_relative --sync 512 600 & sleep 3600 && xdotool key F5
fi

