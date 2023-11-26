@echo off




color 09
echo installing required components...
pip install -r requirements.txt


color 0A
echo  components installed.

color 09
echo  running up machine learning algorimths( might take a minute or two )...

python main.py


