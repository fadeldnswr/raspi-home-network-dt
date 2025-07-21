'''
Rssi Logger Component
This component is responsible for logging the Received Signal Strength Indicator (RSSI) of the network.
'''

import subprocess
import sys

from typing import Dict
from datetime import datetime
from src.logging.logging import logging
from src.exception.exception import CustomException

def get_rssi(interface="wlan0") -> Dict:
  '''
  Function to get the RSSI value of the specified network interface.
  '''
  try:
    output = subprocess.check_output(["iwconfig", interface]).decode()
    for line in output.splitlines():
      if "Signal level" in line:
        level = line.split("Signal level=")[1].split(" ")[0]
        return {
          "interface": interface,
          "rssi_dbm": int(level)
        }
  except Exception as e:
    print(f"Error getting RSSI: {e}")
    return {
      "interface": interface,
      "rssi_dbm": -100
  }