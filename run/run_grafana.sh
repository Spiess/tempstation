docker run -d --name=grafana \
	--network tempstation-net \
	-p 3000:3000 \
	--mount type=volume,src=grafana-storage,dst=/var/lib/grafana \
	grafana/grafana
