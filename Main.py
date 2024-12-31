
from tkinter import *
from tkinter import ttk
from datetime import datetime
from time import strftime
from PIL import Image, ImageTk, ImageDraw
from student import Student
from Photos import Photos
import os
from takeAtt import face_recognition
from checkAtt import Attendance

class Page2:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("FaceStamp")

        img6 = Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\page2.jpeg")
        img6 = img6.resize((1550, 790), Image.ADAPTIVE)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        f_lbl6 = Label(self.root, image=self.photoimg6)
        f_lbl6.place(x=0, y=0, width=1550, height=790)
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        fr = LabelFrame(root, bd=2, bg="black", relief=RIDGE, fg="white", font=("times new roman", 15, "bold"))
        fr.place(x=20, y=600, width=150, height=75)

# Create Label inside the LabelFrame
        lbl = Label(fr, font=("times new roman", 15, "bold"), bg="black", fg="white")
        lbl.place(x=20, y=20, width=110, height=30)  # Adjust the coordinates to position the label properly

# Call the time function
        time()

        # Student Details
        img7 = Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\SD.png")
        img7.thumbnail((210, 210), Image.ADAPTIVE)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b7 = Button(f_lbl6, image=self.photoimg7,command=self.student_details,cursor="hand2")
        b7.place(x=200, y=200,width=220,height=220)  
        b7_7 = Button(f_lbl6, text="Student Details",command=self.student_details,cursor="hand2",font=("Helvetica", 14), fg="black", bg="white", relief=FLAT)
        b7_7.place(x=200, y=400,width=220,height=40)  
        #TakeAttendance
        img10 = Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\TA.png")
        img10.thumbnail((210, 210), Image.ADAPTIVE)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b10 = Button(f_lbl6,command=self.takatt ,image=self.photoimg10,cursor="hand2")
        b10.place(x=450, y=200,width=220,height=220)  
        b10_10 = Button(f_lbl6,command=self.takatt ,text="Take Attendance",cursor="hand2",font=("Helvetica", 14), fg="black", bg="white", relief=FLAT)
        b10_10.place(x=450, y=400,width=220,height=40)
        #CheckAttendance
        img8 = Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\CA.png")
        img8.thumbnail((210, 210), Image.ADAPTIVE)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b8 = Button(f_lbl6,command=self.attendance_details, image=self.photoimg8,cursor="hand2")
        b8.place(x=700, y=200,width=220,height=220)  
        b8_8 = Button(f_lbl6,command=self.attendance_details ,text="CheckAttendance",cursor="hand2",font=("Helvetica", 14), fg="black", bg="white", relief=FLAT)
        b8_8.place(x=700, y=400,width=220,height=40)  
        # Photos
        img9 = Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\p.png")
        img9.thumbnail((210, 210), Image.ADAPTIVE)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b9 = Button(f_lbl6,command=self.open_img ,image=self.photoimg9,cursor="hand2")
        b9.place(x=950, y=200,width=220,height=220)  
        b9_9 = Button(f_lbl6,command=self.open_img, text="Photos",cursor="hand2",font=("Helvetica", 14), fg="black", bg="white", relief=FLAT)
        b9_9.place(x=950, y=400,width=220,height=40)  
        
        #exit
        img11 = Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\exit.jpeg")
        img11.thumbnail((210, 210), Image.ADAPTIVE)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b11 = Button(f_lbl6, image=self.photoimg11,cursor="hand2",command=self.iExit)
        b11.place(x=1200, y=200,width=220,height=220)  
        b11_11 = Button(f_lbl6, text="Exit",cursor="hand2",command=self.iExit,font=("Helvetica", 14), fg="black", bg="white", relief=FLAT)
        b11_11.place(x=1200, y=400,width=220,height=40)  

    def iExit(self):
        # self.iExit = tkinter.askyesno("EXIT", "Are you sure you want to exit?")
        if self.iExit:
            self.root.destroy()
        else:
            return




    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def attendance_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def takatt(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)

    # def checkatt(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Attendance(self.new_window)

  

    def open_img(self):
        os.startfile("data")


if __name__ == "__main__":
    root = Tk()
    obj = Page2(root)
    root.mainloop()
 