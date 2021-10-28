import face_recognition

photo_amartya = face_recognition.load_image_file("/home/amartya/Pictures/amartya.jpg", "L")

print("The shape of this pic is", photo_amartya.shape)
