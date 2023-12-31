import psutil
import time
import os

def get_gpu_usage():
    try:
        # Для NVIDIA GPU
        result = os.popen("nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits").read()
        return int(result.strip())
    except Exception as e:
        print(f"Ошибка при получении использования GPU: {e}")
        return None

def check_system_status():
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    memory_used = memory.used / (1024**3)
    memory_total = memory.total / (1024**3)
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    net_io = psutil.net_io_counters()
    net_sent = net_io.bytes_sent
    net_received = net_io.bytes_recv
    gpu_usage = get_gpu_usage()
    disk_partitions = psutil.disk_partitions(all=False)
    disk_usage_list = []

        
    print(f"Использование процессора: {cpu_percent}%")
    print(f"Использование ОЗУ: {memory_percent}% ({memory_used:.2f}ГБ/{memory_total:.2f}ГБ)")
    for disk_usage in disk_usage_list:
        print(f"Disk Usage ({disk_usage[0]}): {disk_usage[1]}% ({disk_usage[2]:.2f}GB/{disk_usage[3]:.2f}GB)")
    if gpu_usage is not None:
        print(f"Использование GPU: {gpu_usage}%")
    print(f"Отправлено: {net_sent} Байт")
    print(f"Получено: {net_received} Байт")
    print("----------")

while True:
    check_system_status()
    time.sleep(3)
