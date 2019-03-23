# Import pytessaract and import the loading image function
import pytesseract
from PIL import ImageDraw, Image
from sys import argv

# Parameters used for in the program later on
image_param = argv[1]
output_param = argv[2]

# Variable for image
im = Image.open(image_param)
draw = ImageDraw.Draw(im)
boxes = pytesseract.image_to_boxes(im)


# PRINT DETECTED TEXTS
print(pytesseract.image_to_string(im))

# ARRAY FOR SEPERATED TEXTS THAT SPEW OUT THE COORDS: 199 2899 199 29 0
# WHICH IS X1 X2 Y1 Y2 AND THE LAST ONE, IDK
seperated = []
for l in boxes.splitlines():
    # print(l[2:].split(' '))
    seperated.append(l[2:].split(' '))

# FOR EACH COORDS IN THE SEPERATED LIST
# COORDS[0] IS X1
# COORDS[1] IS X2
# AND SO ON
for coords in seperated:
    draw.rectangle([int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])], outline='rgb(255,0,0)')

# WHEN DONE, SAVE
im.save(output_param)
