from PIL import Image, ImageDraw
import face_recognition

group_photo = face_recognition.load_image_file('/home/amartya/Pictures/group1.jpg')
group_photo_location = face_recognition.face_locations(group_photo)

pil_img = Image.fromarray(group_photo)

first_top, first_right, first_bottom, first_left = group_photo_location[0]

for face_location in group_photo_location:
    top, right, bottom, left = face_location
    if top <= first_top:
        first_top = top
    if right >= first_right:
        first_right = right
    if bottom >= first_bottom:
        first_bottom = bottom
    if left <= first_left:
        first_left = left
draw = ImageDraw.Draw(pil_img)
draw.rectangle((first_left-20, first_top-20, first_right+20, first_bottom+20), outline=(0, 0, 0), width=10)

pil_img.show()
