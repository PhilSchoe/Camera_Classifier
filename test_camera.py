from unittest import TestCase
from camera import Camera


class TestCamera(TestCase):

    def setUp(self):
        self.camera = Camera()

    def test_get_frame(self):
        return_value, frame = self.camera.get_frame()

        self.assertTrue(return_value)
        self.assertTrue(len(frame.shape) == 3)
        self.assertTrue(frame.shape[0] > 0)
        self.assertTrue(frame.shape[1] > 0)
        self.assertTrue(frame.shape[2] > 0)
