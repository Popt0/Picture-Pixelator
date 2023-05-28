# Takes a 3D array of defined RGB values and returns a new pixel
# with the average R,G, and B values from the pixels passed in

def AverageRGBVals(pixels):
    rTotal     = 0;
    gTotal     = 0;
    bTotal     = 0;
    pixelCount = 0;
    newPixel = (0, 0, 0);

    for pixel in pixels:
        rTotal += pixel[0];
        gTotal += pixel[1];
        bTotal += pixel[2];
        pixelCount += 1;

    if pixelCount > 0:
        rAverage = int(rTotal/pixelCount);
        gAverage = int(gTotal/pixelCount);
        bAverage = int(bTotal/pixelCount);
        newPixel = (rAverage, gAverage, bAverage);

    return newPixel;

# Takes a 3D array of defined RGBA values and returns a new pixel
# with the average R,G,B, and A values from the pixels passed in
def AverageRGBAVals(pixels):
    rTotal     = 0;
    gTotal     = 0;
    bTotal     = 0;
    aTotal     = 0;
    pixelCount = 0;
    newPixel = (0, 0, 0, 0);

    return newPixel;