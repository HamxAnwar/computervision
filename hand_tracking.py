import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectionConf=0.5, trackConf=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConf = detectionConf
        self.trackConf = trackConf

        #Initialize mediapipe for hand tracking with default parameters
        self.mpHands = mp.solutions.hands
        self.mpDraw = mp.solutions.drawing_utils
        self.hands = self.mpHands.Hands()
    
    def imageCapture():
        cap = cv2.VideoCapture('http://192.168.10.3:4747/video')
        success, image = self.cap.read()
        if self.success:
            return self.image



    def findHands(self, image, draw=True):
        self.imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)



def main():
    
    #for FPS calculation
    previous_time = 0
    current_time = 0
    
    current_time = time.time()
    fps = 1/(current_time - previous_time)
    previous_time = current_time
    cv2.putText(image, str(int(fps)), (5, 80), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
    cv2.imshow("Hand tracked image", image)
    cv2.waitKey(1)









while True:
    
    track = hands.process(imageRGB)
    # print(track.multi_hand_landmarks)

    if track.multi_hand_landmarks:
        for landmarks in track.multi_hand_landmarks:
            mpDraw.draw_landmarks(image, landmarks, mpHands.HAND_CONNECTIONS)

    