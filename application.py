import tkinter as tk
from tkinter import simpledialog
import cv2 as cv
import os
import PIL.Image, PIL.ImageTk
import camera


class Application:

    def __init__(self, window=tk.Tk(), window_title="Camera Classifier"):
        self.window = window
        self.window.attributes('-topmost', True)
        self.window.mainloop()

        self.window_title = window_title

        self.counters = [1, 1]

        #self.model = ...

        self.auto_predict = False

        self.camera = camera.Camera()

        #self.init_gui()

        self.delay = 15
        #self.update()

    def init_gui(self):
        self.canvas = tk.Canvas(self.window, width=self.camera.width, height=self.camera.height)

    def auto_predict_toggle(self):
        self.auto_predict = not self.auto_predict

    @staticmethod
    def run_app():
        print("Hello from App")
