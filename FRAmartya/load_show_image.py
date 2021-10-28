from PIL import Image
import face_recognition

photo_amartya = face_recognition.load_image_file("/home/amartya/Pictures/amartya.jpg", "RGB")
print("The shape of this pic is", photo_amartya.shape)

pil_photo_amartya = Image.fromarray(photo_amartya)
pil_photo_amartya.show()
