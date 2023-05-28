from PIL import Image;
from AverageRGBVals import AverageRGBVals;
import os;

#Takes the average RGB value of a section of an image and returns
#a new series of pixels based on the averages of all sections of the
#image which can be used to "draw" a new image with less pixels.

def CompressImage(newH, newW, picture):
    secWidth  = int(picture.width / newW);
    secHeight = int(picture.height / newH);
    finalPixels = [];
    for h in range(newH):
        for w in range(newW):
            pixels = [];
            for row in range(secHeight):
                for column in range(secWidth):
                    picCol = column + (secWidth * w);
                    picRow = row + (secHeight * h);
                    coord = picCol, picRow;
                    currentPixel = picture.getpixel(coord);
                    pixels.append(currentPixel);
                
            newPixel = AverageRGBVals(pixels);
            finalPixels.append(newPixel);
    return finalPixels;

#Takes one pixel's RGB values and appends it to a sectionof the image
#based on a growth factor which results in a list that can be used to
#'draw' a new image with more pixels.

def EnlargeImage(growthFactor, pixels, picture):
    finalPixels = [];
    
    for group in range(int(len(pixels)/picture.width)):
        currentPixels = [];
        for pixel in range(picture.width):
            currentPixels.append(pixels[pixel + (picture.width * group)]);

        for row in range(growthFactor):
            for col in range(picture.width):
                for px in range(growthFactor):
                    finalPixels.append(currentPixels[col]);

    return finalPixels;