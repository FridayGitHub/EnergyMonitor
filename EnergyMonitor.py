# pierwszy argument to bedzie sciezka do zapisu pliku csv!
 
 # uruchomienie skryptu komenda:
# python3 ./EnergyMonitor.py EnergyMonitorData3.csv 12
# python3 ./EnergyMonitor.py <nazwa pliku csv> <czas w godzinach działania skryptu>
 
import json
import csv
import sys
import time
import os.path

path_csv = sys.argv[1]
test_duration = sys.argv[2]
 
 # Poll a Single Devices
import tuyapower

PLUGID = 'insert your ID here'
PLUGIP = 'insert device IP'
PLUGKEY = 'insert your key here'
PLUGVERS = '3.3'

#(on, w, mA, V, err) = tuyapower.deviceInfo(PLUGID,PLUGIP,PLUGKEY,PLUGVERS)

if os.path.exists(path_csv) == False:
	# Writing headers of CSV file
    data_file = open(path_csv, 'w')
    csv_writer = csv.writer(data_file)
    header = ["datetime","switch","power","current","voltage","response"]
    csv_writer.writerow(header)
    data_file.close()

counter = 0

while (counter/60 <= float(test_duration)):
    time.sleep(60.0 - (time.time() % 60.0))
    #print(time.time())
    
    jsonStr = tuyapower.deviceJSON(PLUGID,PLUGIP,PLUGKEY,PLUGVERS)
    #'{ "datetime": "2019-10-13T03:58:57Z", "switch": "True", "power": "1.2", "current": "70.0", "voltage": "122.1", "response": "OK" }'
    jsonData = json.loads(jsonStr)
    headers = jsonData.keys()
    data_file = open(path_csv, 'a')
    print(jsonData.values())
    csv_writer = csv.writer(data_file)
    # Writing data of CSV file
    csv_writer.writerow(jsonData.values())
    
    data_file.close()
    counter += 1

print("Script finished succesfully logging data for " + str(counter/60) + " hours")

#print(type(jsonData))
#print(jsonData)
	
