from PIL import Image
import face_recognition

amartya_photo = face_recognition.load_image_file('/home/amartya/Pictures/amartya.jpg')
# print(amartya_photo.shape)

amartya_photo_location = face_recognition.face_locations(amartya_photo)
print(amartya_photo_location)     # top, right, bottom, left (list of tuples)

top = amartya_photo_location[0][0]
right = amartya_photo_location[0][1]
bottom = amartya_photo_location[0][2]
left = amartya_photo_location[0][3]

amartya_face = amartya_photo[top:bottom, left:right]
pil_face = Image.fromarray(amartya_face)
pil_face.show()
