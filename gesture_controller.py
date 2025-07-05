from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL, GUID
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import cv2

import screen_brightness_control as sbc
from utils import distance_to_value

# Fix for audio interface
IAudioEndpointVolume.iid = GUID("{5CDF2C82-841E-4546-9722-0CF74078229A}")

class GestureController:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume.iid, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))
        self.volMin, self.volMax = self.volume.GetVolumeRange()[0:2]

    def apply_controls(self, img, hands):
        left = hands['left']
        right = hands['right']

        if left:
            x1, y1 = left[4]
            x2, y2 = left[8]
            length = distance_to_value(x1, y1, x2, y2)

            brightness = int(self.map_value(length, 15, 200, 0, 100))
            brightness = max(min(brightness, 100), 0)
            sbc.set_brightness(brightness)
            print(f"🔆 Brightness set to: {brightness}%")
            cv2.putText(img, f'Brightness: {brightness}%', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        if right:
            x1, y1 = right[4]
            x2, y2 = right[8]
            length = distance_to_value(x1, y1, x2, y2)

            vol_scalar = self.map_value(length, 15, 200, 0.0, 1.0)
            vol_scalar = max(min(vol_scalar, 1.0), 0.0)
            self.volume.SetMasterVolumeLevelScalar(vol_scalar, None)
            vol_percent = int(vol_scalar * 100)
            print(f"🔊 Volume set to: {vol_percent}%")
            cv2.putText(img, f'Volume: {vol_percent}%', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        return img

    def map_value(self, value, left_min, left_max, right_min, right_max):
        # Linear mapping function
        left_span = left_max - left_min
        right_span = right_max - right_min
        value_scaled = float(value - left_min) / float(left_span)
        return right_min + (value_scaled * right_span)
