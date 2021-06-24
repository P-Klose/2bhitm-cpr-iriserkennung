import io
import picamera
import cv2
import numpy
#for post request
import requests


#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


while True:
        #Create a memory stream so photos doesn't need to be saved in a file
        stream = io.BytesIO()

        #Get the picture (low resolution, so it should be quite fast)
        #Here you can also specify other parameters (e.g.:rotate the image)
        with picamera.PiCamera() as camera:
                camera.resolution = (640, 480)
                camera.capture(stream, format='jpeg')
        #Convert the picture into a numpy array
        buff = numpy.frombuffer(stream.getvalue(), dtype=numpy.uint8)

        #Now creates an OpenCV image
        image = cv2.imdecode(buff, 1)

        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #Look for faces in the image using the loaded cascade file
        faces = face_cascade.detectMultiScale(image, 1.1, 5)
        eyes = eye_cascade.detectMultiScale(image, 1.1, 5)


        #Draw a rectangle around every found face
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
        
        for (x,y,w,h) in eyes:
            cv2.circle(image,(x+int(w/2),y+int(w/2)),20,(255,255,255),2)
            
        url = 'http://localhost:3000/ChartData'
        myObj = {'faces':len(faces),'eyes':len(eyes)}

        x = requests.post(url, data = myObj)

        #cv2.destroyAllWindows() 
            
        cv2.imshow("show", image)
        if cv2.waitKey(100) & 0xFF == ord ('x'):
                break
        





#Save the result image
#cv2.imwrite('result.jpg',image)
