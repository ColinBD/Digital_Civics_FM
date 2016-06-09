#/!bin/bash

#Check to see if the browser is open 
if ! ps -e | grep epiphany > /dev/null

#If the browser is open...
then

	# export xauthority
    export XAUTHORITY="/home/pi/.Xauthority"
	#export display
    export DISPLAY=:0.0
    #echo "DISPLAY is $DISPLAY"
	
	#run epiphany web browser to localhost file, sleep 5, simulate mouse movement off-screen and then sleep for one hour. Simulate F5 keypress to re-load index.html 
    epiphany-browser -a --profile /home/pi/.config http://127.0.0.1/index.html & sleep 5 && xdotool mousemove_relative --sync 512 600 & sleep 3600 && xdotool key F5
fi

