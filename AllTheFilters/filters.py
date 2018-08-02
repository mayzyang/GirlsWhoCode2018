# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    image = Image.open(filename)
    return image

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(imageObj):
    imageObj.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imageObj, filename):
    imageObj.save(filename, "png")
    show_img(imageObj)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(image):
    pixels = image.getdata()
    #list to hold new image pixel Data
    new_pixels = []
    #define color constants to use for recoloring
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    #process pixels in image
    for p in pixels:
        #intensity is R + G + B
        intensity = p[0] + p[1] + p[2]
        if intensity < 182:
            new_pixels.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)
        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightBlue)
        elif intensity >= 546:
            new_pixels.append(yellow)

    newImage = Image.new("RGB", image.size)
    newImage.putdata(new_pixels)
    return newImage
