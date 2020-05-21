# TempStation
A small and easy to understand temperature monitoring station for Raspberry Pi and the DHT22 temparature and humidity sensor.

## Usage
1. Start with a Raspberry Pi running Raspbian
2. Install Docker
3. Clone this repository
4. From the `docker` directory run `docker build --tag templog:latest .`
5. From the project root run `sh init.sh`
6. To start the temperature monitoring station run `sh run.sh`
7. Now you can log into the Grafana UI and configure how the data should be displayed by visiting `raspberrypi.local:3000` on your local network (replace `raspberrypi` with the hostname of your Raspberry Pi)

## Edits
There are a number of ways in which you can customize your experience. The script [log_temp.py](docker/log_temp.py) assumes that the data pin `D4` is used to connect the DHT22. If this is not the case, this must be changed.

While the InfluxDB server should not be accessible from outside of the custom Docker network, you may want to change the passwords contained in [linit_influxdb.sh](init/init_influxdb.sh) and [log_temp.py](docker/log_temp.py).
