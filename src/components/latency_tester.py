'''
Latency Tester Component
This component is responsible for testing network latency by pinging a specified host.
'''

import subprocess
import sys

from typing import Dict
from datetime import datetime
from src.logging.logging import logging
from src.exception.exception import CustomException

def latency_test(host="8.8.8.8", count=5) -> Dict:
  '''
  Function to test network latency by pinging a specified host.
  '''
  try:
    output = subprocess.check_output(["ping", "-c", str(count), host], stderr=subprocess.STDOUT).decode()
    lines = output.splitlines()
    stats = lines[-1].split("=")[1].strip().split("/")
    latency = float(stats[1])
    jitter = float(stats[2]) - float(stats[0])
    packet_loss_line = [l for l in lines if "packet loss" in l][0]
    packet_loss = float(packet_loss_line.split("%")[0].split()[-1])
    
    # Return a dictionary with the results
    return {
      "latency_ms": latency,
      "jitter_ms": jitter,
      "packet_loss": packet_loss,
    }
  except Exception as e:
    print(f"Error during latency test: {e}")
    return {
      "latency": -1,
      "jitter": -1,
      "packet_loss": -1,
    }