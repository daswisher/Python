import os

absolutePath = os.path.abspath(__file__)
directoryName = os.path.dirname(absolutePath)
print "Changing working directory to", directoryName
os.chdir(directoryName)
