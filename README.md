# Project: JPG to PNG Converter

The scope is to convert all JPG images of a given folder, convert them into PNG images and saving them in another folder

## Start with the code below

```
import sys
import os   # or pathlib
from PIL import Image
```

## Steps:
- Use the SIS module to grab the first and second argument/directory
- Check if the 2n argument exist, if not create it
- Loop through the first directory selecting all the images and convert them to PNG
- Save them inside the second directory
