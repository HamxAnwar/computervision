import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('http://192.168.10.3:4747/video')

#Using mediapipe for hand tracking with default parameters
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands()

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    track = hands.process(imageRGB)
    # print(track.multi_hand_landmarks)

    if track.multi_hand_landmarks:
        for landmarks in track.multi_hand_landmarks:
            mpDraw.draw_landmarks(image, landmarks, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Hand tracked image", image)
    cv2.waitKey(1)