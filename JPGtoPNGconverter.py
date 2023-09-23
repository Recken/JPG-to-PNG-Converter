import sys
import os # or pathlib
from PIL import Image

# use SIS module and grab 1st, 2nd argument
# check if 2n argument exist, if not create it
# loop through the entire folder and convert images to PNG
# for this we use the os module, we grab the path so we want the files of argument 1 and we want to write in argument2
# save them to a new folder

original_path = sys.argv[1]
final_path = sys.argv[2]

print(f"1st path {original_path} and 2nd path {final_path}")
#os.chdir(f"{original_path}")
#print(os.getcwd())     checks if it has changed the directory


if os.access(final_path, os.F_OK):
    print("The directory exists!")
else:
    os.mkdir(final_path)
    #os.chdir(f"{original_path}")
    #print(os.getcwd())
    print("Directory created!")

#os.chdir(f"{original_path}")
print(os.listdir(original_path))
items_directory = os.listdir(original_path)
for items in items_directory:
    print(items)
    img = Image.open(f"{original_path}/{items}")
    print(img)
    img.save(f"{final_path}/{items[:-4]}.png", "png")
