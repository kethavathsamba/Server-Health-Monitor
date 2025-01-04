# Server Health Monitoring Script

## Overview
The Server Health Monitoring Script is a Python-based utility that monitors a server's resource usage, including CPU, memory, and disk utilization. It logs the system's health metrics to a log file and provides alerts when resource usage exceeds specified thresholds.

## Features
- **Real-Time Monitoring**: Periodically checks the server's CPU, memory, and disk usage.
- **Logging**: Logs health metrics with timestamps into a log file (`server_health.log`).
- **Alerts**: Displays and logs warning messages when resource usage exceeds predefined thresholds:
  - CPU usage > 80%
  - Memory usage > 60%
  - Disk usage > 90%
- **Graceful Termination**: Allows interruption using `Ctrl+C`.

## Configuration
The script includes configurable thresholds and intervals:
- **CHECK_INTERVAL**: Time (in seconds) between health checks. Default: 5 seconds.
- **CPU_THRESHOLD**: CPU usage percentage threshold. Default: 80%.
- **MEMORY_THRESHOLD**: Memory usage percentage threshold. Default: 60%.
- **DISK_THRESHOLD**: Disk usage percentage threshold. Default: 90%.

## Prerequisites
- Python 3.x installed on your system.
- Required library: `psutil`. Install it using:
  ```bash
  pip install psutil
  ```

## Usage
1. **Clone or Download the Script**: Save the script as `server_health_monitor.py` on your system.
2. **Run the Script**:
   ```bash
   python server_health_monitor.py
   ```
3. **Monitor Health**: The script will start monitoring the server and display the health metrics in the terminal. Alerts will be printed and logged if thresholds are exceeded.
4. **Stop the Script**: Use `Ctrl+C` to stop the monitoring process.

## Output

### Terminal Output
Example output:
```yaml
[2025-01-04 11:00:00] CPU Usage: 45% | Memory Usage: 58% | Disk Usage: 72%
[2025-01-04 11:00:05] CPU Usage: 85% | Memory Usage: 62% | Disk Usage: 91%
[2025-01-04 11:00:05] High CPU Usage: 85%
[2025-01-04 11:00:05] High Memory Usage: 62%
[2025-01-04 11:00:05] High Disk Usage: 91%
```

### Log File
The log file `server_health.log` contains detailed records of each check and alert:
```yaml
[2025-01-04 11:00:00] CPU Usage: 45% | Memory Usage: 58% | Disk Usage: 72%
[2025-01-04 11:00:05] CPU Usage: 85% | Memory Usage: 62% | Disk Usage: 91%
[2025-01-04 11:00:05] High CPU Usage: 85%
[2025-01-04 11:00:05] High Memory Usage: 62%
[2025-01-04 11:00:05] High Disk Usage: 91%
```

## Future Enhancements
- Add email or SMS notifications for critical alerts.
- Extend the script to monitor additional resources (e.g., network usage, process details).
- Add a feature to visualize the resource usage trends in real-time.
- Support for multiple disk partitions.

## License
This project is open-source and licensed under the MIT License. Feel free to modify and distribute it as needed.
```

You can save this content in a `README.md` file in your project directory. Let me know if you'd like any modifications!
