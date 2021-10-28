from PIL import Image
import face_recognition

amartya_pic = face_recognition.load_image_file('/home/amartya/Pictures/amartya.jpg')

amartya_pic_location = face_recognition.face_locations(amartya_pic, model='cnn')

print(amartya_pic_location)

top = amartya_pic_location[0][0]
right = amartya_pic_location[0][1]
bottom = amartya_pic_location[0][2]
left = amartya_pic_location[0][3]

amartya_face = amartya_pic[top:bottom, left:right]
pil_face = Image.fromarray(amartya_face)
pil_face.show()
