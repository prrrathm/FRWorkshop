from PIL import Image, ImageDraw

pil_sunset = Image.open('/home/amartya/Pictures/sunset.jpg')

draw = ImageDraw.Draw(pil_sunset)

draw.rectangle((100, 200, 550, 650), outline=(0, 0, 0), width=10)
draw.line((100, 200, 550, 650), fill=(255, 0, 0), width=5)
pil_sunset.show()
