import cv2 as cv


class Camera:

    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Unable to open the camera")

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            return_value, frame = self.camera.read()

            if return_value:
                return return_value, cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            else:
                return return_value, None
        else:
            return None
