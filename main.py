'''
Main file for the Raspberry Pi Network Data Transfer project.
This file initializes the FastAPI application and includes the main route.
'''
import sys
import os
from datetime import datetime
from supabase import create_client, Client

from src.components.latency_tester import latency_test
from src.components.rssi_logger import get_rssi
from src.components.speedtest_logger import run_speedtest
from src.components.system_monitor import system_monitor
from src.components.device_scanner import scan_for_devices

from src.logging.logging import logging
from src.exception.exception import CustomException
from dotenv import load_dotenv
load_dotenv()

# Create supabase client
SUPABASE_API_URL = os.getenv("SUPABASE_API_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
if not SUPABASE_API_URL or not SUPABASE_API_KEY:
  print("Supabase API URL or Key not set in environment variables.")

supabase: Client = create_client(SUPABASE_API_URL, SUPABASE_API_KEY)

# Create a function to collect all data
def collect_all_data():
  '''
  Function to collect all data from various components and return a dictionary.
  '''
  try:
    latency_data = latency_test()
    rssi_data = get_rssi()
    speedtest_data = run_speedtest()
    system_data = system_monitor()
    device_data = scan_for_devices()
    combined_data = {
      **latency_data,
      **rssi_data,
      **speedtest_data,
      **system_data,
      **device_data
    }
    return combined_data
  except Exception as e:
    raise CustomException(e, sys)

# Define function to send data to Supabase
def send_data_to_supabase():
  '''
  Function to send collected data to Supabase.
  '''
  try:
    data = collect_all_data()
    response = supabase.table("network_data").insert(data).execute()
    return response
  except Exception as e:
    raise CustomException(e, sys)

if __name__ == "__main__":
  try:
    # Collect and send data to Supabase
    send_data_to_supabase()
    print("Data sent to Supabase successfully")
  except CustomException as e:
    logging.error(f"CustomException: {e}")
