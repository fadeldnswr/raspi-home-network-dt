'''
Speedtest Logger Component
This component is responsible for logging the results of a speed test.
'''

from speedtest import Speedtest
from typing import Dict

def run_speedtest() -> Dict:
  '''
  Function to run a speed test and return the results.
  '''
  try:
    st = Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    return {
      "download_mbps": round(download_speed, 2),
      "upload_mbps": round(upload_speed, 2),
    }
  except Exception as e:
    print(f"Error running speed test: {e}")
    return {
      "download_speed": -1,
      "upload_speed": -1,
    }