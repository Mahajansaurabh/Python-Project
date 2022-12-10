import cv2
import face_recognition_models as fr


#load images
control_picture = fr.load_image_file('PictureA.jpg')
test_picture = fr.load_image_file('PictureB.jpg')

#transform images to RGB
control_picture = cv2.cvtColor(control_picture,cv2.COLOR_BGR2RGB)
test_picture = cv2.cvtColor(test_picture,cv2.COLOR_BGR2RGB)

#locate control face
face_A_location = fr.face_locations(control_picture)[0]
coded_face_A = fr.face_encodings(control_picture)[0]

#locate control face
face_B_location = fr.face_locations(control_picture)[0]
coded_face_B = fr.face_encodings(control_picture)[0]

#show rectangle
cv2.rectangle(control_picture,
              (face_A_location[3],face_A_location[0]),
              (face_A_location[1],face_A_location[2]),
              (0,255,0),
              2)

#perform comparison
result = fr.compare_faces([coded_face_A],coded_face_B,0.3)



cv2.rectangle(test_picture,
             (face_B_location[3],face_B_location[0]),
             (face_B_location[1],face_B_location[2]),
             (0,255,0),
             2)





#measurement of distances
distance = fr.face_distance([coded_face_A],coded_face_B)

#show results
cv2.putText (test_picture,
             f'{result} {distance.round(2)}',
             (50,50),
             cv2.FONT_HERSHEY_COMPLEX,
             1,
             (0,255,0),
             2)


#show images
cv2.imshow('My Control Picture', control_picture)
cv2.imshow('My Test Picture', test_picture)


#keep the program working
cv2.waitkey(0)