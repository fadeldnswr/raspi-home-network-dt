# 🏠 Raspberry Pi Network Digital Twin

📡 *A real-time monitoring system that logs home network performance using a Raspberry Pi, and sends structured data to Supabase every 5 minutes.*

---

## 📌 Project Overview

This project is a **lightweight digital twin** for home network environments built on **Raspberry Pi**. It monitors key network and system health metrics, then logs them to a **Supabase database** for storage, analysis, and future visualization or modeling.

---

## 🧱 Components

The system consists of 5 modular Python components:

| Module | Description |
|--------|-------------|
| `latency_tester.py` | Measures network latency, jitter, and packet loss via ping |
| `rssi_logger.py` | Captures RSSI (signal strength) from the local WiFi interface |
| `speedtest_logger.py` | Measures download and upload speeds via Speedtest CLI |
| `system_monitor.py` | Logs CPU usage, RAM usage, and Raspberry Pi temperature |
| `device_scanner.py` | Counts connected devices on the network using `nmap` |

Each component returns a single summarized record for logging every 5 minutes.

---

## 🗃️ Supabase Schema

Data is logged to a single table named `network_logs`, with the following schema:

```sql
create table network_logs (
  id uuid primary key default gen_random_uuid(),
  timestamp timestamptz,
  latency_ms float,
  jitter_ms float,
  packet_loss float,
  rssi_dbm int,
  interface text,
  download_mbps float,
  upload_mbps float,
  cpu_usage float,
  ram_usage float,
  temp float,
  device_count int
);