import cv2

#im = cv2.imread('iu.jpeg', cv2.IMREAD_COLOR)
#print(im.shape)

cap = cv2.VideoCapture(0) #0=>default camera 1=>secondary camera

#Instantiate the Cascade Classifier with file_name
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
	ret, frame = cap.read() # Status, Frame

	if not ret:
		continue

	cv2.imshow("Feed", frame)

	#Find all the faces in the frame
	faces = face_cascade.detectMultiScale(frame, 1.3, 5) #Frame , Scaling Factor, Neighbours

        print(faces) #4 parameters x,y,w,h
        
        for face in faces:
                x,y,w,h = face #Tuple unpacking
                
                #Drawing boundary
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2) #fr, start coor, end coor, color rgb, thickness
        
        cv2.imshow("Feed", frame)
        
	key = cv2.waitKey(1)
	if key & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
