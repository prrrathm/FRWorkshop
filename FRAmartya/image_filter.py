from PIL import Image, ImageFilter

pil_sunset = Image.open('/home/amartya/Pictures/sunset.jpg')

pil_emboss = pil_sunset.filter(ImageFilter.EMBOSS())
pil_emboss.show()

pil_blur = pil_sunset.filter(ImageFilter.BLUR())
pil_blur.show()
