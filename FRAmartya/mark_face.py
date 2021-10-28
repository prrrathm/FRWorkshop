from PIL import Image, ImageDraw
import face_recognition

group_photo = face_recognition.load_image_file('/home/amartya/Pictures/group1.jpg')
group_photo_location = face_recognition.face_locations(group_photo)

pil_img = Image.fromarray(group_photo)


count = 0
for face_location in group_photo_location:
    count += 1
    top, right, bottom, left = face_location
    draw = ImageDraw.Draw(pil_img)
    draw.rectangle((left, top, right, bottom), outline=(0, 0, 0), width=4)

pil_img.show()
