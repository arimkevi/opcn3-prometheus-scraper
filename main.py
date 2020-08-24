#!/usr/bin/env python3

import time
import datetime
import json
import glob
import signal
import sys

from opcn3 import Opcn3
from prometheus_client import Gauge, start_http_server

DEV_TTY='/dev/ttyACM0'
LOCATION = glob.glob('/boot/AGW*')[0][6:]
PROMETHEUS_PORT=8000
MEASURING_DELAY=10

SENSOR = None

bin_0_gauge = Gauge('bin_0', 'Bin 0', ['location'])
bin_1_gauge = Gauge('bin_1', 'Bin 1', ['location'])
bin_2_gauge = Gauge('bin_2', 'Bin 2', ['location'])
bin_3_gauge = Gauge('bin_3', 'Bin 3', ['location'])
bin_4_gauge = Gauge('bin_4', 'Bin 4', ['location'])
bin_5_gauge = Gauge('bin_5', 'Bin 5', ['location'])
bin_6_gauge = Gauge('bin_6', 'Bin 6', ['location'])
bin_7_gauge = Gauge('bin_7', 'Bin 7', ['location'])
bin_8_gauge = Gauge('bin_8', 'Bin 8', ['location'])
bin_9_gauge = Gauge('bin_9', 'Bin 9', ['location'])
bin_10_gauge = Gauge('bin_10', 'Bin 10', ['location'])
bin_11_gauge = Gauge('bin_11', 'Bin 11', ['location'])
bin_12_gauge = Gauge('bin_12', 'Bin 12', ['location'])
bin_13_gauge = Gauge('bin_13', 'Bin 13', ['location'])
bin_14_gauge = Gauge('bin_14', 'Bin 14', ['location'])
bin_15_gauge = Gauge('bin_15', 'Bin 15', ['location'])
bin_16_gauge = Gauge('bin_16', 'Bin 16', ['location'])
bin_17_gauge = Gauge('bin_17', 'Bin 17', ['location'])
bin_18_gauge = Gauge('bin_18', 'Bin 18', ['location'])
bin_19_gauge = Gauge('bin_19', 'Bin 19', ['location'])
bin_20_gauge = Gauge('bin_20', 'Bin 20', ['location'])
bin_21_gauge = Gauge('bin_21', 'Bin 21', ['location'])
bin_22_gauge = Gauge('bin_22', 'Bin 22', ['location'])
bin_23_gauge = Gauge('bin_23', 'Bin 23', ['location'])
mtof_gauge = Gauge('mtof', 'MToF', ['location'])
period_gauge = Gauge('period', 'Period', ['location'])
flow_rate_gauge = Gauge('flow_rate', 'FlowRate', ['location'])
opc_t_gauge = Gauge('opc_t', 'OPC-T', ['location'])
opc_rh_gauge = Gauge('opc_rh', 'OPC-RH', ['location'])
pm_1_gauge = Gauge('pm_1', 'PM1', ['location'])
pm_2_5_gauge = Gauge('pm_2_5', 'PM2.5', ['location'])
pm_10_gauge = Gauge('pm_10', 'PM10', ['location'])

def handle_data(data):
    bin_0_gauge.labels(LOCATION).set(data['Bin 0'])
    bin_1_gauge.labels(LOCATION).set(data['Bin 1'])
    bin_2_gauge.labels(LOCATION).set(data['Bin 2'])
    bin_3_gauge.labels(LOCATION).set(data['Bin 3'])
    bin_4_gauge.labels(LOCATION).set(data['Bin 4'])
    bin_5_gauge.labels(LOCATION).set(data['Bin 5'])
    bin_6_gauge.labels(LOCATION).set(data['Bin 6'])
    bin_7_gauge.labels(LOCATION).set(data['Bin 7'])
    bin_8_gauge.labels(LOCATION).set(data['Bin 8'])
    bin_9_gauge.labels(LOCATION).set(data['Bin 9'])
    bin_10_gauge.labels(LOCATION).set(data['Bin 10'])
    bin_11_gauge.labels(LOCATION).set(data['Bin 11'])
    bin_12_gauge.labels(LOCATION).set(data['Bin 12'])
    bin_13_gauge.labels(LOCATION).set(data['Bin 13'])
    bin_14_gauge.labels(LOCATION).set(data['Bin 14'])
    bin_15_gauge.labels(LOCATION).set(data['Bin 15'])
    bin_16_gauge.labels(LOCATION).set(data['Bin 16'])
    bin_17_gauge.labels(LOCATION).set(data['Bin 17'])
    bin_18_gauge.labels(LOCATION).set(data['Bin 18'])
    bin_19_gauge.labels(LOCATION).set(data['Bin 19'])
    bin_20_gauge.labels(LOCATION).set(data['Bin 20'])
    bin_21_gauge.labels(LOCATION).set(data['Bin 21'])
    bin_22_gauge.labels(LOCATION).set(data['Bin 22'])
    bin_23_gauge.labels(LOCATION).set(data['Bin 23'])
    mtof_gauge.labels(LOCATION).set(data['MToF'])
    period_gauge.labels(LOCATION).set(data['period'])
    flow_rate_gauge.labels(LOCATION).set(data['FlowRate'])
    opc_t_gauge.labels(LOCATION).set(data['OPC-T'])
    opc_rh_gauge.labels(LOCATION).set(data['OPC-RH'])
    pm_1_gauge.labels(LOCATION).set(data['pm1'])
    pm_2_5_gauge.labels(LOCATION).set(data['pm2.5'])
    pm_10_gauge.labels(LOCATION).set(data['pm10'])

def sigint_handler(signal, frame):
    print('Stopping.')
    SENSOR.TurnOff(DEV_TTY, 'OPC-N3')
    sys.exit(130)
  
if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint_handler)

    print('Starting HTTP server for Prometheus scraping')
    start_http_server(PROMETHEUS_PORT)

    print('Opening connection to OPC-N3')
    SENSOR = Opcn3(DEV_TTY, 'OPC-N3')

    print('Starting main loop.')
    while True:
        newData = SENSOR.getData(DEV_TTY, 'OPC-N3', handle_data)
        time.sleep(MEASURING_DELAY)


