from PIL import Image;
from imageTransformers import CompressImage, EnlargeImage;
import os;

def main():

    #Paste directory of the application here for proper function
    appLocation = "C:/Users/narut/OneDrive/Documents/GitHub/Picture-Pixelator/";

    #Gets user input for the program's mode while checking for incorrect inputs
    invalidInput = True;
    while invalidInput:
        try:
            print("Pixelate or shrink all pictures in the \"ToPixelate\" folder "
                  "with your desired dimensions\n\n"
                  "1 - Pixelate\n2 - Shrink\n3 - Enlarge\n");
            modeInput = int(input("Mode: "));
            invalidInput = False;
            print();
        except ValueError:
            print("\nEnter one of the designated options\n");
        except:
            print("\nAn error has occurred, try again.");
        if modeInput < 1 or modeInput > 3:
            print("Please enter an existing mode.");
            InvalidInput = True;

    picNum = 1;
    
    with os.scandir(appLocation + "ToPixelate/") as pictures:
        #Cycles through all pictures in the directory
        for picture in pictures:
            image = Image.open(appLocation + "ToPixelate/" + picture.name);

            #Pixelates image by shrinking then enlarging the image with the new pixel data
            if modeInput == 1:
                #Gets user input for the pixelation factor of the picture while checking for incorrect inputs
                invalidInput = True;
                while invalidInput:
                    try:
                        pixFactor  = int(input("Pixelation Factor: "));
                        print();
                        invalidInput = False;
                    except ValueError:
                        print("\nPixelation Factor must be an integer value.");
                    except:
                        print("\nAn error occurred, try again.");

                print("Beginning picture #" + str(picNum) + ":\n");

                print("Creating Pixels...");
                newWidth  = int(image.width / pixFactor);
                newHeight = int(image.height / pixFactor);

                #Regulates pixelation to include at least 1 pixel in order to avoid division by 0
                if newWidth == 0:
                    newWidth += 1;
                if newHeight == 0:
                    newWidth += 1;
                newData = CompressImage(newHeight, newWidth, image);

                #Uses new values rather than image.height/width in case of loss during integer division if 
                #dimensions are not evenly divisible by the pixelation factor
                print("Fitting pixels...")
                newPicture = Image.new(mode = "RGB", size = (newWidth, newHeight));
                newPicture.putdata(newData);
                newData = EnlargeImage(pixFactor, newData, newPicture);

                print("Generating Image...")
                #Uses new values rather than image.height/width in case of loss during integer division if 
                #dimensions are not evenly divisible by the pixelation factor
                newPicture = Image.new(mode = "RGB", size = (newWidth * pixFactor, newHeight * pixFactor));

            #Shrinks the image
            if modeInput == 2:
                #Gets user input for the height and width of the picture while checking for incorrect inputs
                invalidInput = True;
                while invalidInput:
                    try:
                        newWidth  = int(input("New Width: "));
                        newHeight = int(input("New Height: "));
                        print();
                        invalidInput = False;
                    except ValueError:
                        print("\nBoth fields must be an integer value.");
                    except:
                        print("\nAn error occurred, try again.");

                print("Beginning picture #" + str(picNum) + ":\n");

                print("Creating Pixels...");
                newData = CompressImage(newHeight, newWidth, image);

                print("Generating Image...")
                newPicture = Image.new(mode = "RGB", size = (newWidth, newHeight));

            #Enlarges the image
            if modeInput == 3:
                #Gets user input for the growth factor of the picture while checking for incorrect inputs
                invalidInput = True;
                while invalidInput:
                    try:
                        growthFactor  = int(input("Growth Factor: "));
                        print();
                        invalidInput = False;
                    except ValueError:
                        print("\nThe field must be an integer value.");
                    except:
                        print("\nAn error occurred, try again.");

                print("Creating Pixels...")
                newData = EnlargeImage(growthFactor, list(image.getdata()), image);

                print("Generating Image...")
                newPicture = Image.new(mode = "RGB", size = (image.width * growthFactor, image.height * growthFactor));
            
            #Finalizes image by putting in the new pixel data and saving in to the output folder
            newPicture.putdata(newData);
            newPicture.save(appLocation + "Pixelated/Picture" + str(picNum) + ".jpg");
            
            print("\nPicture #" + str(picNum) + " generated.\n");
            picNum += 1;
    print("All pictures generated");



main();
