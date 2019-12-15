import face_recognition

image = face_recognition.load_image_file('./img/groups/team5.jpg')
face_locations = face_recognition.face_locations(image)

# Array of coords of each face
# print(face_locations)


print('En la foto hay ' + str(len(face_locations)) + ' personas')
