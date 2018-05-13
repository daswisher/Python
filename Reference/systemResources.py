import multiprocessing
import psutil

import Tkinter as tk

from tensorflow.python.client import device_lib

print "CPU core count:", multiprocessing.cpu_count()
print "RAM info:", psutil.virtual_memory()

local_device_protos = device_lib.list_local_devices()

for x in local_device_protos:
	print "Name:", x.name
	print "Info:", x

# Get screen size

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print "Width:", screen_width
print "Height:", screen_height
