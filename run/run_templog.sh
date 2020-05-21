docker run -d --name=templog \
	--device /dev/gpiomem \
	--device /dev/gpiochip0 \
	--network tempstation-net \
	templog
