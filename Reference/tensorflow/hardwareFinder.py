'''
https://www.tensorflow.org/tutorials/
'''


from tensorflow.python.client import device_lib

local_device_protos = device_lib.list_local_devices()
print local_device_protos
#return [x.name for x in local_device_protos if x.device_type == 'GPU']

