""" Image to ASCII Art
   - Specify the file types allowed
   - Determine how to indetify pixel with corresponding character
"""

from PIL import Image

# Open the image
im = Image.open("kawhi_shot.jpg")

# Convert image to RGB
to_rgb = im.convert('RGB')

# Map out range of pixels to ascii
ascii_mapping = {
   (0, 16): '!',
   (17, 33): '@',
   (34, 50): '#',
   (51, 67): '$',
   (68, 84): '%',
   (85, 101): '^',
   (102, 118): '&',
   (119, 135): '*',
   (136, 152): '(',
   (153, 169): ')',
   (170, 186): '+',
   (187, 203): '~',
   (204, 220): '?',
   (221, 238): '<',
   (239, 255): '.'
}

# Helper function for converting brightness to ascii equivalent
def converter(brightness):
   for brightness_range, char in ascii_mapping.items():
      if brightness_range[0] <= brightness <= brightness_range[1]:
         return char
   

# Print out the ascii equivalent
for i in range(im.size[1]):
   for j in range(im.size[0]):
      pixelRGB = to_rgb.getpixel((j, i)) 
      R, G, B = pixelRGB
      brightness = sum(pixelRGB) // 3

      # Get the corresponding ASCII character for the brightness
      char = converter(brightness)
      print(char, end='')

   print()  # Move to the next line after printing all characters in the row