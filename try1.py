import face_recognition
from PIL import Image, ImageDraw, ImageFont
pil_sunset = Image.open('img/images(3)')
draw = ImageDraw.Draw(pil_sunset)
draw.text((500, 350), "Sunset Picture", fill=(0, 0, 255))
pil_sunset.show()
Image.open('img/images4').show()
