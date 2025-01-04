import psutil
import time
import logging
from datetime import datetime
CHECK_INTERVAL = 5  
CPU_THRESHOLD = 80   
MEMORY_THRESHOLD = 60  
DISK_THRESHOLD = 90  
LOG_FILE = 'server_health.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
def check_health():
    cpu_usage = psutil.cpu_percent() 
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = (f"[{current_time}] CPU Usage: {cpu_usage}% | "
                   f"Memory Usage: {memory_info.percent}% | "
                   f"Disk Usage: {disk_info.percent}%")
    print(log_message) 
    logging.info(log_message)
    if cpu_usage > CPU_THRESHOLD:
        alert_message = f"[{current_time}] High CPU Usage: {cpu_usage}%"
        print(alert_message)
        logging.warning(alert_message)
    if memory_info.percent > MEMORY_THRESHOLD:
        alert_message = f"[{current_time}] High Memory Usage: {memory_info.percent}%"
        print(alert_message)
        logging.warning(alert_message)
    if disk_info.percent > DISK_THRESHOLD:
        alert_message = f"[{current_time}] High Disk Usage: {disk_info.percent}%"
        print(alert_message)
        logging.warning(alert_message)
def main():
    print("Starting server health checks...")
    try:
        while True: 
            check_health()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("Stopping server health checks...")
if __name__ == '__main__':
    main()
