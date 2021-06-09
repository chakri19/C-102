import os
import sys
from PIL import Image

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        img = Image.open(sys.argv[1])
        target = sys.argv[1] + ".jpg"
        rgb_img = img.convert('RGB')
        rgb_img.save(target)
        print("Saved as " + target)
    else:
        print(sys.argv[1] + " is not found")
else:
    print("Write like this: convert2jpg.py <file>")