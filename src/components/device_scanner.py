'''
Modules to scan for devices in the Raspberry Pi Network Data Transfer project.
This module contains a function to count active devices using nmap.
'''

import subprocess
import sys
from typing import Dict
from datetime import datetime
from src.logging.logging import logging
from src.exception.exception import CustomException

def scan_for_devices(subnet="192.168.1.0/24") -> Dict:
  try:
    result = subprocess.run(["nmap", "-sn", subnet], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    active_device_count = 0
    for line in lines:
      if "Nmap scan report for" in line:
        active_device_count += 1

    return {
      "device_count": active_device_count,
      "interface": "nmap"
    }
  except Exception as e:
    raise CustomException(e, sys)