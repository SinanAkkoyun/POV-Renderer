import sys
import array
import OpenEXR
import Imath
import os
import numpy
from PIL import Image

def main():
    allfiles=os.listdir(os.getcwd())
    imlist=[filename for filename in allfiles if  filename[-4:] in [".exr", ".EXR"]]
    N=len(imlist)

    file = OpenEXR.InputFile(imlist[0])
    h = file.header()
    channels = h['channels'].keys()
    newchannels = dict(zip(channels, file.channels(channels)))
    #print(newchannels.r)
    #return

    pt = Imath.PixelType(Imath.PixelType.FLOAT)
    dw = file.header()['dataWindow']
    size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
    

    # for im in imlist:
    rgbf = [Image.frombytes("F", size, file.channel(c, pt)) for c in "RGB"]
    #test = [numpy.fromstring(file.channel(c, pt), dtype=numpy.float32) for c in 'RGB']
    #print("tet")
    #print(type(test))
    rgb = numpy.array([numpy.fromstring(file.channel(c, pt), dtype=numpy.float32) for c in 'RGB'])
    rgb.fill(0)
    #print(type(rgb))
    
    for im in imlist:
        f = OpenEXR.InputFile(im)
        rgb2 = numpy.array([numpy.fromstring(f.channel(c, pt), dtype=numpy.float32) for c in 'RGB'])
        rgb = rgb+rgb2/N
    
    
    for i in range(3):
        rgb[i] = numpy.where(rgb[i]<=0.0031308,
                (rgb[i]*12.92)*255.0,
                (1.055*(rgb[i]**(1.0/2.4))-0.055) * 255.0)

    rgb8 = [Image.frombytes("F", size, c.tostring()).convert("L") for c in rgb]
    #rgb8 = [Image.fromarray(c.astype(int)) for c in rgb]
    Image.merge("RGB", rgb8).save("averagetest.jpg", "JPEG", quality=95)

if __name__ == "__main__":
    main()
