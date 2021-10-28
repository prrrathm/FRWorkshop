from PIL import Image
import face_recognition

group_photo = face_recognition.load_image_file('/home/amartya/Pictures/group.jpg')
group_photo_location = face_recognition.face_locations(group_photo)

for face_location in group_photo_location:
    top, right, bottom, left = face_location
    face_in_group_photo = group_photo[top:bottom, left:right]
    pil_face = Image.fromarray(face_in_group_photo)
    pil_face.show()
