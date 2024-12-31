from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox,filedialog
import cv2
from PIL import Image, ImageTk, ImageDraw
import mysql.connector
import numpy as np
import pickle
import os
import numpy as np
import pickle
import csv
import mysql.connector

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("FaceStamp")

        

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_time=StringVar()
        # self.var_atten_dep=StringVar()
        self.var_atten_attendance=StringVar()
        # self.var_atten_date=StringVar()

        img1 = Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\page2.jpeg")
        img1 = img1.resize((1550, 790), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=1550, height=790)
        

        # img=Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\SD1.png")
        # img=img.resize((500,130),Image.ADAPTIVE)
        # self.photoimg = ImageTk.PhotoImage(img)
        # f_lbl1=Label(self.root,image=self.photoimg)
        # f_lbl1.place(x=0,y=0,width=500,height=130)
        text_label = Label(self.root, text="Students Attendence", font=("Helvetica", 50))
        text_label.place(x=0, y=0, width=1550, height=130)
        # img2=Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\SD2.png")
        # img2=img.resize((500,130),Image.ADAPTIVE)
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        # f_lbl2=Label(self.root,image=self.photoimg2)
        # f_lbl2.place(x=1050,y=0,width=500,height=120)
        main_frame = Frame(self.root, bd=2,  bg="black", relief=FLAT)
        main_frame.place(x=20, y=150, width=1500, height=600)

        Left_frame = LabelFrame(main_frame, bd=2,bg="black", relief=RIDGE, text="Student Details",fg="white", font=("times new roman", 20, "bold"))
        Left_frame.place(x=20, y=10, width=650, height=580)

        self.exit_button = ttk.Button(self.root, text="Exit", command=self.exit_application)
        self.exit_button.place(x=1480, y=0, width=70, height=30)

        img_left = Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\chechattttt.png")
        img_left = img_left.resize((800, 200), Image.ADAPTIVE) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        left_inside_frame = Frame(Left_frame, bd=2,bg="black", relief=RIDGE)
        left_inside_frame.place(x=20, y=150, width=600, height=350)

        #pid
        attendanceId_label=Label(left_inside_frame,text="Student pid:", width=10, bg="white", font=("comicsansns", 15, "bold"))
        attendanceId_label.grid(row=0,column=0,padx=5,pady=20,sticky=W)
        attendanceId_entry = ttk.Entry(left_inside_frame, width=15,textvariable=self.var_atten_id, font=("comicsansns", 15, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=5, pady=20, sticky=W)
        # Name 
        nameLabel = Label(left_inside_frame, text="Name:",width=10, bg="white", font=("comicsansns", 15, "bold"))
        nameLabel.grid(row=0, column=2, padx=5, pady=20,sticky=W)  # Adjusted padx
        atten_name = ttk.Entry(left_inside_frame, width=15,textvariable=self.var_atten_name ,font=("comicsansns", 15, "bold"))
        atten_name.grid(row=0, column=3,padx=5, pady=20,sticky=W)
        # rollno
        dateLabel = Label(left_inside_frame, text="RollNO:",width=10, bg="white", font=("comicsansns", 15, "bold"))
        dateLabel.grid(row=1, column=0, padx=5, pady=20,sticky=W)  # Adjusted padx
        atten_date = ttk.Entry(left_inside_frame, width=15,textvariable=self.var_atten_roll, font=("comicsansns", 15, "bold"))
        atten_date.grid(row=1, column=1,padx=5, pady=20,sticky=W)
        # Time 
        timeLabel = Label(left_inside_frame, text="Time:",width=10 ,bg="white", font=("comicsansns", 15, "bold"))
        timeLabel.grid(row=1, column=2, padx=5, pady=20,sticky=W)  # Adjusted padx
        atten_time = ttk.Entry(left_inside_frame, width=15,textvariable=self.var_atten_time, font=("comicsansns", 15, "bold"))
        atten_time.grid(row=1, column=3,padx=5, pady=20,sticky=W)
        # Attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance :", width=10,bg="white", font=("comicsansns", 12, "bold"))
        attendanceLabel.grid(row=2, column=0, padx=5, pady=20,sticky=W)  # Adjusted padx
        self.atten_status = ttk.Combobox(left_inside_frame, width=15, textvariable=self.var_atten_attendance,font=("comicsansns", 15, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=2, column=1, padx=5,pady=20,sticky=W)
        self.atten_status.current(0)  # Corrected typo from curent to current

    #     # Button fame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv:",command=self.importCsv,width=25,font=("times new roman",15,"bold"),bg="white",fg="black")
        save_btn.grid(row=0,column=0)

        # update_btn=Button(btn_frame,text="Export csv:",command=self.exportCsv,width=10,font=("times new roman",13,"bold"),bg="white",fg="black")
        # update_btn.grid(row=0,column=1)

        # delete_btn=Button(btn_frame,text="Update",width=25,font=("times new roman",15,"bold"),bg="white",fg="black")
        # delete_btn.grid(row=0,column=1)

        # reset_btn=Button(btn_frame,command=self.reset_data, text="Reset",width=15,font=("times new roman",13,"bold"),bg="white",fg="black")
        # reset_btn.grid(row=0,column=2)

        Right_frame = LabelFrame(main_frame, bd=2, bg="black", relief=RIDGE, text="Attendance Details", fg="white", font=("times new roman", 30, "bold"))
        Right_frame.place(x=700, y=10, width=780, height=580)
   
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="black")
        table_frame.place(x=5,y=5,width=760,height=520)

    # #Scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("pid","roll","name","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # # Set up headings
        # self.AttendanceReportTable.heading("pid", text="Attendance ID")
        self.AttendanceReportTable.heading("pid", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        # self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        self.AttendanceReportTable["show"] = "headings"
        # Set up columns
        self.AttendanceReportTable.column("pid", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        # self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        # # Pack the table
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease-1>",self.get_cursor)
        # self.AttendanceReportTable.bind("<ButtonRelease-1>", self.get_cursor)

    def fetchData (self,rows) :
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
        # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for row in csvread:
                # Remove single quotes and split by comma
                cleaned_row = [value.strip("'") for value in row]
                mydata.append(cleaned_row)
            self.fetchData(mydata)



    def exit_application(self):
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
            self.root.destroy()

        # export csv
    # def exportCsv(self):
    #     try:
    #         if len(mydata)<1:
    #             messagebox.showerror ("No Data", "No Data found to export", parent=self.root)
    #             return False
    #         fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*csv"), ("ALL File","*.*")), parent=self.root)
    #         with open(fln,mode="w", newline="") as myfile:
    #             exp_write=csv.writer(myfile,delimiter=",")
    #         for i in mydata:
    #             exp_write.writerow(i)
    #         messagebox. showinfo("Data Export", "Your data exported to"+os.path. basename(fln)+"successfully")
    #     except Exception as es:
    #         messagebox. showerror("Error",f"Due To : {str(es)}",parent=self.root)

    def get_cursor(self, event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content[ 'values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self. var_atten_name.set(rows [2])
        # self.var_atten_dep.set(rows [3])
        self.var_atten_time.set(rows[3])
        # self. var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows [5])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        # self.var_atten_dep.set("")
        self.var_atten_time.set("")
        # self.var_atten_date.set("")
        self.var_atten_attendance.set("")

        

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
 