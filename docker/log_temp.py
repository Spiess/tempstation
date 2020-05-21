import time
import datetime
import signal
import sys
from statistics import mean

import board
import adafruit_dht
from influxdb import InfluxDBClient

# Define global variables
shutdown_requested = False
batch_size = 30
verbose = True
temperatures = []
humidities = []

# Set up shutdown handler
def shutdown_handler(sig, frame):
    global shutdown_requested
    shutdown_requested = True
    print('Shutdown requested.')

signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)

# Initialize the dht device, with data pin connected to pin D4
dhtDevice = adafruit_dht.DHT22(board.D4)
if verbose:
    print('Successfully connected to DHT22 sensor on data pin D4.')

# Initialize InfluxDB client
client = InfluxDBClient(host='influxdb', port=8086, username='tempuser', password='tempusersecretuser')
client.switch_database('tempstation')
if verbose:
    print('Successfully connected to local InfluxDB.')

while not shutdown_requested:
    try:
        # Print the values to the serial port
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        temperatures.append(temperature)
        humidities.append(humidity)

        if len(temperatures) >= batch_size:
            mean_temp = mean(temperatures)
            mean_hum = mean(humidities)
            json_body = [
                {
                    "measurement": "tempInfo",
                    "tags": {
                        "room": "Florian's Bedroom"
                    },
                    "fields": {
                        "temperature": mean_temp,
                        "humidity": mean_hum
                    }
                }
            ]
            ret = client.write_points(json_body)
            if ret:
                temperatures = []
                humidities = []
                if verbose:
                    print(f'{datetime.datetime.now()} - Temp: {mean_temp:.1f} C - Humidity: {mean_hum:.1f}%')
            elif verbose:
                print('Error: Could not commit data to database.', file=sys.stderr)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])

    time.sleep(2.0)

print('Shutting down...')
client.close()

