import cv2 as cv #jag har inget skämt om denna
import mediapipe as mp #mp som i manapool från skyblock
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os #CachyOS omg vilken ref (reference)

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'detector.tflite')
base_options = python.BaseOptions(model_asset_path=model_path)
cap = cv.VideoCapture(0) #säger att video capture är cap för slang osv samma som calc = calculator
options = vision.FaceDetectorOptions(base_options=base_options) #säger vilka inställningar typ å då säger den att den vill ha från detector.tflite
face_detek = vision.FaceDetector.create_from_options(options) #självaste detektorn

w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(f"Camera feed: {w}x{h}")
middle_x = w/2
middle_y = h/2

def camera_loop():
    global face_x, face_y, deadzone
    
    while True:
        ret, frame = cap.read()

        if not ret: #om inte finns = no funk
            break    

        conv = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=conv)
        convframe = face_detek.detect(mp_image)
        if convframe.detections:

            detection = convframe.detections[0]
            bbox = detection.bounding_box
            face_x = bbox.origin_x + bbox.width // 2
            face_y = bbox.origin_y + bbox.height // 2
        
            #print(f"Ansikte hittat!,  {face_x},{face_y}")
        
            Hpoint_x = bbox.origin_x + bbox.width
            Hpoint_y = bbox.origin_y + bbox.height
            deadzone = int(int(bbox.width) / 5) # 5 är arbiträrt

            cv.rectangle(frame, (bbox.origin_x, bbox.origin_y), (Hpoint_x, Hpoint_y), (255, 25, 103), 2 )
            cv.circle(frame, (face_x,face_y), (deadzone), (0, 25, 103), 2)
        #else:
            #print("Inget ansikte")


        cv.imshow("frame", frame) #dehär är vad som visar skiten type shiii

        if cv.waitKey(1) & 0xFF == ord('q'): #måste va fokuserad på video grejen, uuhm aa den funkar fint
            break

    cap.release() #när den stängs av så släpps den och kan användas vidare
    cv.destroyAllWindows() #dödar allt osv, osv, etc