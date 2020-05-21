docker volume create influxdb-storage
docker run --rm \
	-e INFLUXDB_DB=tempstation \
	-e INFLUXDB_ADMIN_USER=administrator -e INFLUXDB_ADMIN_PASSWORD=adsu7for6b3y5eygd234fb \
	-e INFLUXDB_USER=tempuser -e INFLUXDB_USER_PASSWORD=tempusersecretuser \
	--mount type=volume,src=influxdb-storage,dst=/var/lib/influxdb \
	influxdb /init-influxdb.sh
