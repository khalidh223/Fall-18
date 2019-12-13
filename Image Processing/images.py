'''
    images.py

    Jeff Ondich, 1 November 2009
    Updated 27 October 2018
    Modified by Khalid Hussain, 3 November 2018

    This program illustrates pixel-based manipulation of images using the
    Python Imaging Library (PIL). To run this program on your own computer,
    you will need to install install the python3 version of PIL:
        
        pip3 install Pillow

    See more about installing PIL at
    https://pillow.readthedocs.io/en/5.3.x/installation.html
    PIL is already installed in the CS labs in the CMC (304, 306, 102) and
    in Weitz 138.

    Your job for the image processing assignment is to write the functions
    below whose definitions currently contain only the stub code
    "return original_image".  Simple testing code for all the functions,
    including the stubs, is included at the bottom of this program.
'''

import sys
from PIL import Image, ImageOps, ImageColor

def get_green_image(original_image):
    ''' Returns a copy of the specified image with all the red and blue removed. '''
    green_image = original_image.copy()
    green_pixels = green_image.load()
    image_width = green_image.size[0]
    image_height = green_image.size[1]
    for row in range(image_height):
        for column in range(image_width):
            green_value = green_pixels[column, row][1]
            green_pixels[column, row] = (0, green_value, 0)
    return green_image

def get_small_image(original_image):
    ''' Returns a copy of the specified image, scaled to half size both
       horizontally and vertically. '''
    small_image_width = original_image.size[0] // 2
    small_image_height = original_image.size[1] // 2
    originalPixels = original_image.load()
    small_image = Image.new("RGB", (small_image_width, small_image_height))
    small_image_pixels = small_image.load()
    for y in range(small_image_height):
        for x in range(small_image_width):
            red = (originalPixels[2*x, 2*y][0] + originalPixels[2*x + 1, 2*y][0]\
                    + originalPixels[2*x, 2*y + 1][0] + originalPixels[2*x + 1, 2*y + 1][0]) // 4
            green = (originalPixels[2*x, 2*y][1] + originalPixels[2*x + 1, 2*y][1]\
                    + originalPixels[2*x, 2*y + 1][1] + originalPixels[2*x + 1, 2*y + 1][1]) // 4
            blue = (originalPixels[2*x, 2*y][2] + originalPixels[2*x + 1, 2*y][2]\
                    + originalPixels[2*x, 2*y + 1][2] + originalPixels[2*x + 1, 2*y + 1][2]) // 4
            small_image_pixels[x, y] = (red, green, blue)
    return small_image

def get_gray_image(original_image):
    ''' Returns a copy of the specified image in black-and-white (also known as
       "gray-scale"). Replaces each pixel's red, green, and blue components with
       the average of its original red, green, and blue values. '''
    gray_image = original_image.copy()
    gray_pixels = gray_image.load()
    image_width = gray_image.size[0]
    image_height = gray_image.size[1]
    for y in range(image_height):
        for x in range(image_width):
            gray_value_red = gray_pixels[x, y][0]
            gray_value_green = gray_pixels[x, y][1]
            gray_value_blue = gray_pixels[x, y][2]
            average_rgb = (gray_value_red + gray_value_green + gray_value_blue) // 3
            gray_pixels[x, y] = (average_rgb, average_rgb, average_rgb)
    return gray_image

def get_mirror_image(original_image):
    ''' Returns a copy of the specified image, reflected horizontally
       (so, for example, if there were a ">" in the original image, it would appear
       as a "<" in the mirror image). '''
    mirror_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    return mirror_image

def get_rotated_image(original_image):
    ''' Returns a copy of the specified image, rotated clockwise by
        90 degrees.  (Note that you will need to create a new image whose dimensions
        are different than the original image's dimensions. See get_small_image for
        an example of how to do this.) '''
    rotated_image = original_image.rotate(-90, expand=True)
    return rotated_image

def get_bordered_image(original_image, border_color, border_thickness):
    ''' Returns a copy of the specified image, surrounded by a solid
        border of the specified color, with the thickness of the border specified
        by the integer border_thickness. Note that your new image will need to be
        bigger than the original_image by 2*border_thickness in both directions
        so you don't lose any of the original image. '''
    bordered_image = ImageOps.expand(original_image,border=border_thickness,fill=border_color)
    return bordered_image

def get_image_with_fake_scratches(original_image):
    ''' Returns a copy of the specified image with white pixels added stand
        in for "scratches" on the surface of a photograph.  My version of this method
        creates diagonal white lines 50 pixels apart, but you can do anything that adds
        a reasonable number of unexpected white pixels to the image. (Vertical or horizontal
        lines are probably easier to draw, and would be perfectly acceptable.) '''
    scratched_image = original_image.copy()
    scratched_pixels = scratched_image.load()
    image_width = scratched_image.size[0]
    image_height = scratched_image.size[1]
    for y in range(image_height):
        for x in range(10, image_width, 40):
            scratched_pixels[x, y] = (255, 255, 255)
    return scratched_image

def get_green_screened_image(original_image, background_image, green_screen_color, color_radius):
    ''' Returns a copy of the original image with all pixels within the
        specified color range replaced by the background image's corresponding pixel.
        Suppose green_screen_color is (R, G, B). Then a color (r, g, b) should be
        considered to be "within the color range" of (R, G, B) if the Euclidean distance
        between (r, g, b) and (R, G, B) is less than or equal to color_radius. That is,
        (r - R)**2 + (g - G)**2 + (b - B)**2 <= color_radius**2. '''
    green_screen_image = original_image.copy()
    green_screen_pixels = green_screen_image.load()
    background = background_image
    background_image_pixels = background.load()
    R, G, B = green_screen_color[0], green_screen_color[1], green_screen_color[2]
    green_screen_image_width = green_screen_image.size[0]
    green_screen_image_height = green_screen_image.size[1]
    for y in range(green_screen_image_height):
        for x in range(green_screen_image_width):
            r = green_screen_pixels[x, y][0]
            g = green_screen_pixels[x, y][1]
            b = green_screen_pixels[x, y][2]
            if (r - R)**2 + (g - G)**2 + (b - B)**2 <= color_radius**2:
                green_screen_pixels[x, y] = background_image_pixels[x, y]
            else:
                green_screen_pixels[x,y] = (r, g, b)
    return green_screen_image

def main():
    """
    Calls appropriate functions, and uses show method to output what is returned
    from each function. Saves output image to same folder as program.
    """
    if len(sys.argv) != 3:
        print('Usage: %s imagefile' % sys.argv[0])
        exit()

    image_file_name = sys.argv[1]
    if '.' in image_file_name:
        index_of_last_dot = image_file_name.rfind('.')
        image_file_base_name = image_file_name[:index_of_last_dot]
    else:
        image_file_base_name = image_file_name

    image = Image.open(image_file_name)
    image.show()
    
    background_image_file_name = sys.argv[2]
    background_image = Image.open(background_image_file_name)
    background_image.show()

    green_image = get_green_image(image)
    green_image.show()
    green_image.save('{0}.green.jpg'.format(image_file_base_name), 'JPEG')

    small_image = get_small_image(image)
    small_image.show()
    small_image.save('{0}.small.jpg'.format(image_file_base_name), 'JPEG')

    gray_image = get_gray_image(image)
    gray_image.show()
    gray_image.save('{0}.gray.jpg'.format(image_file_base_name), 'JPEG')

    rotated_image = get_rotated_image(image)
    rotated_image.show()
    rotated_image.save('{0}.rotated.jpg'.format(image_file_base_name), 'JPEG')

    mirror_image = get_mirror_image(image)
    mirror_image.show()
    mirror_image.save('{0}.mirrored.jpg'.format(image_file_base_name), 'JPEG')

    scratched_image = getImageWithFakeScratches(image)
    scratched_image.show()
    scratched_image.save('{0}.scratched.jpg'.format(image_file_base_name), 'JPEG')

    bordered_image = get_bordered_image(image, (0, 255, 0), 20)
    bordered_image.show()
    rotated_image.save('{0}.rotated.jpg'.format(image_file_base_name), 'JPEG')

    green_screened_image = get_green_screened_image(image, background_image, (111, 232, 117), 50)
    green_screened_image.show()
    green_screened_image.save('{0}.putonbackground.jpg'.format(image_file_base_name), 'JPEG')
main()
