import numpy
import matplotlib.pyplot as plt
from copy import deepcopy
from PIL import Image

def getGrayColor(rgb):
    return rgb[0]

def setGrayColor(color):
    return [color, color, color]

img = Image.open('lula.png')
img = numpy.asarray(img)
# copy list not reference
ct = deepcopy(img)
r1 = 100
s1 = 50
r2 = 150
s2 = 200
for i in range(len(img)):
    for j in range(len(img[i])):
        x = getGrayColor(img[i][j])
        if(0 <= x and x <= r1):
            ct[i][j] = setGrayColor(s1/r1 * x)
        elif(r1 < x and x <= r2):
            ct[i][j] = setGrayColor(((s2 - s1)/(r2 - r1)) * (x - r1) + s1)
        elif(r2 < x and x <= 255):
            ct[i][j] = setGrayColor(((255 - s2)/(255 - r2)) * (x - r2) + s2)

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(ct)
plt.show()
