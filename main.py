import cv2
from hand_detector import HandDetector
from gesture_controller import GestureController

cap = cv2.VideoCapture(0)
detector = HandDetector()
controller = GestureController()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands = detector.find_hands(img)
    img = controller.apply_controls(img, hands)

    cv2.imshow('Gesture Controller', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
