# Requires python-imaging
# Additional requirements: libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

'''
EXIFTAGS = TAGS.items()
EXIFTAGS.sort()
print EXIFTAGS

print

gps = GPSTAGS.items()
gps.sort()
print gps
'''

image = Image.open("/home/slm/GitHub/Python/Reference/flower.jpg")
EXIFData = image._getexif()
catEXIF = EXIFData.items()
catEXIF.sort()
print catEXIF
