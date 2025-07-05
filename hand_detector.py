import cv2
import mediapipe as mp
from google.protobuf.json_format import MessageToDict

class HandDetector:
    def __init__(self):

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(min_detection_confidence=0.75)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        left = None
        right = None

        if results.multi_hand_landmarks and results.multi_handedness:
            for idx, hand_handedness in enumerate(results.multi_handedness):
                label = MessageToDict(hand_handedness)['classification'][0]['label']
                lmList = []
                for lm in results.multi_hand_landmarks[idx].landmark:
                    h, w, _ = img.shape
                    lmList.append([int(lm.x * w), int(lm.y * h)])

                if label == 'Left':
                    left = lmList
                elif label == 'Right':
                    right = lmList

                self.mpDraw.draw_landmarks(img, results.multi_hand_landmarks[idx], self.mpHands.HAND_CONNECTIONS)

        return {'left': left, 'right': right, 'img': img}