
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from student import student
from FaceRecognitionSystem import pg1

class Exit:
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app =Main (self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()