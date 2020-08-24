#!/bin/bash

if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root" 1>&2
  exit 1
fi

echo "Disabling service..";
systemctl stop opcn3-prometheus.timer;
systemctl stop opcn3-prometheus.service;

systemctl disable opcn3-prometheus.timer;
systemctl disable opcn3-prometheus.service;

rm /etc/systemd/system/opcn3-prometheus.service;
rm /etc/systemd/system/opcn3-prometheus.timer;
systemctl daemon-reload;
rm /etc/sudoers.d/opcn3-sudoers;

echo "Delete user: opcn3";
userdel -r opcn3;