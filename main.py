# Import pytessaract and import the loading image function
import pytesseract
from PIL import ImageDraw, Image
from sys import argv

image_param = argv[1]
output_param = argv[2]

# Variable for image
im = Image.open('test3.jpeg')
draw = ImageDraw.Draw(im)
boxes = pytesseract.image_to_boxes(im)

splitl = boxes.splitlines()
seperated = []

print(pytesseract.image_to_string(im))

for l in splitl:
    # print(l[2:].split(' '))
    seperated.append(l[2:].split(' '))

for coords in seperated:
    draw.rectangle([int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])], outline='rgb(255,0,0)')

im.save('./outputnew.jpg')
