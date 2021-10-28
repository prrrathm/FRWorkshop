from PIL import Image
import face_recognition

group_photo = face_recognition.load_image_file('/home/amartya/Pictures/group.jpg')

group_photo_location = face_recognition.face_locations(group_photo)
print("Total Faces in the Picture are ", len(group_photo_location))
