FROM python:3

WORKDIR /usr/src/templog

RUN pip install RPi.GPIO adafruit-circuitpython-dht influxdb && \
  apt update && apt install -y libgpiod2

COPY log_temp.py .

CMD ["python", "-u", "log_temp.py"]
