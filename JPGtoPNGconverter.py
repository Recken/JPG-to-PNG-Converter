import sys
import os # or pathlib
from PIL import Image

# Grabs first and second directory
# Careful: needs to be add / at the end of each of the arguments provided!
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(f"First directory is {image_folder} and second directory is {output_folder}")


# Checks if second directory exists, if not is created
if os.access(output_folder, os.F_OK):
    print(f"The {output_folder} directory already exists!")
else:
    os.mkdir(output_folder)
    #os.chdir(f"{output_folder}")   moves to the new directory created
    #print(os.getcwd())     tell us in which directory we are in
    print(f"The {output_folder} directory has been created!")

'''
Alternative:
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
'''

# Loop over all items from first directory and turn them to PNG inside the second directory
items_directory = os.listdir(image_folder)
for items in items_directory:
    img = Image.open(f"{image_folder}{items}")
    img.save(f"{output_folder}{items[:-4]}.png", "png")    # we remove the 4 last letters of items (.jpg) and write instead .png

'''
Alternative:
for items in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{items}")
    clean_name = os.path.splittext(filename)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")

    Splitext will return a tupple with the file name and the extension, so we grab 0 to only pick up the filename and then we add the .png extension
'''