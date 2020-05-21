docker run -d --name=influxdb \
	--network tempstation-net \
	--mount type=volume,src=influxdb-storage,dst=/var/lib/influxdb \
	influxdb
