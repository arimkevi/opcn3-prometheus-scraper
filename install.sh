#!/bin/bash

if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root" 1>&2
  exit 1
fi

echo "Installing OPC-N3 prometheus scraper";

echo "Installing packages..";
apt -y install virtualenv python3 python3-pip;

echo "Creating user..";
useradd -m opcn3 ;
usermod -a -G dialout opcn3;

echo "Downloading repo..";
curl -sL "https://github.com/arimkevi/opcn3-prometheus-scraper/archive/master.zip" > "/tmp/opcn3_prometheus.zip";
unzip -qq -o "/tmp/opcn3_prometheus.zip" -d "/home/opcn3";
mv /home/opcn3/opcn3-prometheus-scraper-master /home/opcn3/opcn3-prometheus-scraper
chown -R opcn3:opcn3 /home/opcn3/opcn3-prometheus-scraper/
rm /tmp/opcn3_prometheus.zip;

echo "Installing venv..";
runuser -l opcn3 -c 'cd /home/opcn3/opcn3-prometheus-scraper; virtualenv venv -p python3;';

echo "Istalling python requirements to venv..";
runuser -l opcn3 -c 'source /home/opcn3/opcn3-prometheus-scraper/venv/bin/activate; pip install -r /home/opcn3/opcn3-prometheus-scraper/requirements.txt;';

echo "Setting up service.."
mv "/home/opcn3/opcn3-prometheus-scraper/deploy/opcn3-prometheus.service" "/etc/systemd/system/";
mv "/home/opcn3/opcn3-prometheus-scraper/deploy/opcn3-prometheus.timer" "/etc/systemd/system/";
systemctl stop opcn3-prometheus.timer;
systemctl disable opcn3-prometheus.timer;

systemctl daemon-reload
systemctl enable opcn3-prometheus.timer;
systemctl start opcn3-prometheus.timer;