import multiprocessing
import psutil

from tensorflow.python.client import device_lib

print "CPU core count:", multiprocessing.cpu_count()
print "RAM info:", psutil.virtual_memory()

local_device_protos = device_lib.list_local_devices()

for x in local_device_protos:
	print "Name:", x.name
	print "Info:", x

