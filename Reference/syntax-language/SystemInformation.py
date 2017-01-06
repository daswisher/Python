from psutil import virtual_memory
import psutil

print psutil.cpu_count()
print virtual_memory().total
