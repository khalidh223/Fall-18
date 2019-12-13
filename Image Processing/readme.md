This program utilizes an image-manipulation library within Python known as the [Python Imaging Library](https://pillow.readthedocs.io/en/5.3.x/handbook/index.html) to implement a few image transformations. Specifically, it will take the chosen image and make it green, scale it to half the original size, black-and-white, flipped, rotated, bordered by a color, attain fake vertical scratches, and can have a third image with a green-screen placed over it.

# Files #

## `images.py` ##
Main program used to run the different image transformations. Must be run with the command `python images.py [chosen green screen image] [chosen regular image]`, with images chosen being JPEG images.

## `space.jpg` ##
An example regular image.

## `testgreenscreen.jpg` ##
An example green-screened image.

**Note: Every file listed must be in the same folder in order to run `images.py`**.

# Acknowledgements #
To [Professor Jeff Ondich](http://cs.carleton.edu/faculty/jondich/) for providing the original starter code and idea.
