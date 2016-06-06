# Digital Civics FM

This repository contains the codebase for Colin, Stuart and Helen's Technologies for Digital Civics project.

# Overview

A focus group of older people expressed a desire for Newcastle University's digital communications to be made accessible to people with low levels of I.T. literacy. We developed Digital Civics FM as a response. This centres on a modified traditional radio which reads out the University's digital communications to the user, along with communications relating to a research area of personal interest to the user. Additionally, the radio features a screen which can display images and text. 

## Features

The radio has a dial to allow the user to select one of four streams:
1. Newcastle University's twitter communications
2. Twitter activity relating to the user's research area of interest.
3. Newcastle University's Facebook activity
4. Newcastle University's Instagram activity

The radio has three buttons - play, stop, and eject.
a) The play button reads out tweets if one of the two twitter streams is selectd
b) The stop button ends audio playback
c) The eject button toggles the screen in and out of the radio. 

## Using the software

The repository contains two folder 'forRadioPi' and 'forServerPi'. As such two raspberry PI computers are required.

1. The code within the forRadioPi folder should be loaded onto a raspberry pi and placed within the modified radio. The job of this code is to look for user interactions with the radio and then play the appropriate audio files, display the appropriate images on the screen, or eject/withdraw the screen.
2. The code within the forServerPi folder should be loaded onto a pi which does not need to be placed within the radio. The job of this code is to run scripts at regular intervals which:
a) for the twitter streams: scrape twitter and returns tweets including the @uniofnewcastle address, and tweets with a hash tag relating to the users research interests (which in this case was #breastfeeding). These tweets are parsed to make them more legible and fed into a text to speech convertor. The audio files which are returned are then pushed onto the PI within the radio waiting for the user to play them.
b) for the instagram stream: Stuart to complete

## Installing dependancies
Twython is used to scrape twitter. It must be installed on the serverPI. 
  sudo pip install twython
  
CereProc is used for the text to speech conversion. To apply for an academic license and to download the code visit: https://www.cereproc.com/en/products/academic 
1) On the server PI you must include a voice file (heather.voice in our case), a licence file, and the cerevoice_eng python library. These are not included within the repository for copyright reasons. 
2) Within the txt2wavTool.py file (line 41) you must point to the cerevoice_eng/pylib folder that is on your system. 
3) Within scrapeTwitter.py (line 12) you must point to licence file and the voice file on your system.



## License
The txt2wavTool.py file contains code written by CereProc and contains a license within the file. All other files were written by Colin, Stuart or Helen for the purpose of this project and are licensed under the MIT license (see below)

Copyright (c) <2016> <Colin Dodds, Stuart Nicholson, Helen Rice>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
