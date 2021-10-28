from PIL import Image, ImageDraw, ImageFont

pil_sunset = Image.open('/home/amartya/Pictures/sunset.jpg')

draw = ImageDraw.Draw(pil_sunset)

fnt = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', 60)
draw.text((500, 350), "Sunset Picture", font=fnt, fill=(0, 0, 255))
pil_sunset.show()
