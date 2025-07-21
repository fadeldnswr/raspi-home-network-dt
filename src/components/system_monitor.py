'''
System Monitor Component
This component is responsible for monitoring system resources such as CPU, memory, and disk usage.
'''

import psutil
import sys
import subprocess

from typing import Dict
from datetime import datetime
from src.logging.logging import logging
from src.exception.exception import CustomException

def get_cpu_temperature() -> float:
  '''
  Function to get CPU temperature.
  '''
  try:
    output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
    return float(output.replace("temp=", "").replace("'C\n", ""))
  except:
    return -1.0

def system_monitor() -> Dict:
  '''
  Function to monitor system resources and return a dictionary with the results.
  '''
  try:
    return {
      "cpu_usage": psutil.cpu_percent(interval=1),
      "ram_usage": psutil.virtual_memory().percent,
      "temp": get_cpu_temperature(),
    }
  except Exception as e:
    raise CustomException(e, sys)