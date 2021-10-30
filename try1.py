import face_recognition

known1 = face_recognition.load_image_file('./img/srk.jpg')
known1E = face_recognition.face_encodings(known1)[0]
unknown1 = face_recognition.load_image_file('./img/ark.jpg')
unknown1E = face_recognition.face_encodings(unknown1)[0]

result = face_recognition.compare_faces([known1E,],[unknown1E],tolerance=0.5)

if result :
    print('Faces Match')
else :
    print('Faces doesnt match')
