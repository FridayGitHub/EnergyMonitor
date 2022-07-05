# EnergyMonitor
script that uses tuyapower to monitor the electrical parameters of tuya compatible devices e.g. plugs

tuyapower: https://github.com/jasonacox/tuyapower

See instruction in linked tuyapower repository on how to set up tuya compatible device to interact with tuyapower.

My script is add on to allow for periodic readout of data from device, e.g. plug for certain period of time in hours. I have been using GoSund SP111 plug for measurements.

To run the script use following command:
python3 ./EnergyMonitor.py <output file name> <time in hours>
