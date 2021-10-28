from PIL import Image, ImageDraw, ImageFont
import face_recognition

group_photo = face_recognition.load_image_file('/home/amartya/Pictures/group.jpg')
group_photo_location = face_recognition.face_locations(group_photo)

pil_img = Image.fromarray(group_photo)

fnt = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', 30)

count = 0
for face_location in group_photo_location:
    count += 1
    top, right, bottom, left = face_location
    draw = ImageDraw.Draw(pil_img)
    draw.rectangle((left, top, right, bottom), outline=(0, 0, 0), width=4)
    face_in_group_photo = group_photo[top:bottom, left:right]
    pil_face = Image.fromarray(face_in_group_photo)
    pil_face.show()
    name = input("Enter the name of face shown: ")
    draw.text((left+15, top-50), str(name), font=fnt, fill=(0, 0, 255))

pil_img.show()
