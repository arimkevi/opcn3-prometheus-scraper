# OPC-N3 Prometheus scraper

Prometheus scraper for [Alphasense OPC-N3][opcn3].

OPC-N3 integration modified from [JarvisSan22's repo][jarvis]

## Setup

1. Disable login shell for serial on rpi via raspi-config. (Interfacing options -> Serial -> No to login shell -> Yes to serial hardware)
2. Connect OPC-N3 to RPI using SPI-USB adapter
3. Check that `ls /dev/ | grep ttyACM0` is found

## Install

Run:

```curl -fsSL "https://raw.githubusercontent.com/arimkevi/opcn3-prometheus-scraper/master/install.sh" | sudo bash```

then run:

```sudo systemctl restart opcn3-prometheus```

[opcn3]: alphasense.com/index.php/products/optical-particle-counter/
[jarvis]: https://github.com/JarvisSan22/OPC-N3_python
