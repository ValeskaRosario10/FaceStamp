
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox
import mysql.connector
import numpy as np
import cv2
import pickle
import os
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier
import csv

class Student:

    def __init__(self, root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("FaceStamp")

        #var
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_pid=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_img=StringVar()
        img6 = Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\page2.jpeg")
        img6 = img6.resize((1550, 790), Image.ADAPTIVE)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        f_lbl6 = Label(self.root, image=self.photoimg6)
        f_lbl6.place(x=0, y=0, width=1550, height=790)

        #centeral images and text
        img=Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\SD1.png")
        img=img.resize((500,130),Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl1=Label(self.root,image=self.photoimg)
        f_lbl1.place(x=0,y=0,width=500,height=130)
        text_label = Label(self.root, text="Student Details", font=("Helvetica", 50))
        text_label.place(x=500, y=0, width=550, height=130)
        img2=Image.open(r"C:\Users\Valeska\OneDrive\Desktop\Sem4MiniProject\ImagesForGUI\SD2.png")
        img2=img.resize((500,130),Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=1050,y=0,width=500,height=130)
        main_frame = Frame(self.root, bd=2,  bg="black", relief=FLAT)
        main_frame.place(x=20, y=150, width=1500, height=650)

        #leftLabelFrame
        Left_frame = LabelFrame(main_frame, bd=2,bg="black", relief=RIDGE, text="Student Details",fg="white", font=("times new roman", 30, "bold"))
        Left_frame.place(x=20, y=10, width=710, height=580)

        cc_frame = LabelFrame(Left_frame, bd=2,bg="black", relief=RIDGE, text="Current Course",fg="white", font=("times new roman", 15, "bold"))
        cc_frame.place(x=10, y=10, width=690, height=150)
        #dep
        dep_label=Label(cc_frame,text="Department",font=("times new roman", 15, "bold"),bg="black",fg="white")
        dep_label.grid(row=0,column=0,padx=10)
        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_dep,font=("times new roman", 15, "bold"),state="read only")
        dep_combo["values"]=("Select Department ",'CMPN','INFT','EXTC','ELEC','MECH')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2,pady=10)
        #Course
        co_label=Label(cc_frame,text="Course",font=("times new roman", 15, "bold"),bg="black",fg="white")
        co_label.grid(row=0,column=2,padx=10,sticky=W)
        co_combo=ttk.Combobox(cc_frame,textvariable=self.var_course,font=("times new roman", 15, "bold"),state="read only")
        co_combo["values"]=("Select Course ", "FE","SE","TE","BE")
        co_combo.current(0)
        co_combo.grid(row=0,column=3, padx=2,pady=10,sticky=W)
        #year
        y_label=Label(cc_frame,text="Year",font=("times new roman", 15, "bold"),bg="black",fg="white")
        y_label.grid(row=1,column=0,padx=10,sticky=W)
        y_combo=ttk.Combobox(cc_frame,textvariable=self.var_year,font=("times new roman", 15, "bold"),state="read only")
        y_combo["values"]=("Select Year ", "2020-21","2021-22","2022-23","2023-24")
        y_combo.current(0)
        y_combo.grid(row=1,column=1, padx=2,pady=10,sticky=W)
        #Semester
        y_label=Label(cc_frame,text="Semester",font=("times new roman", 15, "bold"),bg="black",fg="white")
        y_label.grid(row=1,column=2,padx=10,sticky=W)
        y_combo=ttk.Combobox(cc_frame,textvariable=self.var_sem,font=("times new roman", 15, "bold"),state="read only")
        y_combo["values"]=("Select Year ", "1","2","3","4","5","6","4","8")
        y_combo.current(0)
        y_combo.grid(row=1,column=3, padx=2,pady=20,sticky=W)

        #ClassSInfo
        ci_frame = LabelFrame(Left_frame, bd=2,bg="black", relief=RIDGE, text="Class Student Info",fg="white", font=("times new roman", 15, "bold"))
        ci_frame.place(x=10, y=200, width=690, height=300)

        sid_label=Label(ci_frame,text="Student PID",font=("times new roman", 15, "bold"),bg="black",fg="white")
        sid_label.grid(row=0,column=0,padx=10,sticky=W)
        studentID_entry=ttk.Entry(ci_frame,textvariable=self.var_pid,width=17,font=("times new roman", 15, "bold"))
        studentID_entry.grid(row=0,column=1,padx=20,pady=10,sticky=W)

        sn_label=Label(ci_frame,text="Student Name",font=("times new roman", 15, "bold"),bg="black",fg="white")
        sn_label.grid(row=0,column=2,padx=10,sticky=W)
        sn_entry=ttk.Entry(ci_frame,width=17,textvariable=self.var_name,font=("times new roman", 15, "bold"))
        sn_entry.grid(row=0,column=3,padx=20,pady=10,sticky=W)

        sid_label=Label(ci_frame,text="Division",font=("times new roman", 15, "bold"),bg="black",fg="white")
        sid_label.grid(row=1,column=0,padx=10,sticky=W)
        studentID_entry=ttk.Entry(ci_frame,textvariable=self.var_div,width=17,font=("times new roman", 15, "bold"))
        studentID_entry.grid(row=1,column=1,padx=20,pady=10,sticky=W)

        se_label=Label(ci_frame,text="Roll no",font=("times new roman", 15, "bold"),bg="black",fg="white")
        se_label.grid(row=1,column=2,padx=10,sticky=W)
        se_entry=ttk.Entry(ci_frame,textvariable=self.var_rollno,width=17,font=("times new roman", 15, "bold"))
        se_entry.grid(row=1,column=3,padx=20,pady=10,sticky=W)

        # sr_label=Label(ci_frame,text="Roll No",font=("times new roman", 15, "bold"),bg="black",fg="white")
        # sr_label.grid(row=2,column=0,padx=10,sticky=W)
        # sr_entry=ttk.Entry(ci_frame,width=20,font=("times new roman", 15, "bold"))
        # sr_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # sp=Label(ci_frame,text="Phone No",font=("times new roman", 15, "bold"),bg="black",fg="white")
        # sp.grid(row=2,column=2,padx=10,sticky=W)
        # sp_entry=ttk.Entry(ci_frame,width=20,font=("times new roman", 15, "bold"))
        # sp_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # #Radiob
        # radiobutton1=ttk.Radiobutton(ci_frame,text="Take Photo Sample", value="Yes")
        # radiobutton1.grid(row=6,column=0)
        # radiobutton2=ttk.Radiobutton(ci_frame,text="No Photo Sample", value="No")
        # radiobutton2.grid(row=6,column=1)
        
        # self.exit_button = ttk.Button(self.root, text="Exit", command=self.exit_application)
        # self.exit_button.place(x=1400, y=750, width=70, height=30)

        btn_frame=Frame(ci_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=175,width=680,height=50)

        sbtn=Button(btn_frame,text="Save",command=self.add_data,width=9,font=("times new roman", 15, "bold"),bg="black",fg="white")
        sbtn.grid(row=0,column=0)
        # sbtn=Button(btn_frame,text="Update",width=13,font=("times new roman", 15, "bold"),bg="black",fg="white")
        # sbtn.grid(row=0,column=1)
        sbtn=Button(btn_frame,text="Delete",command=self.del_date,width=9,font=("times new roman", 15, "bold"),bg="black",fg="white")
        sbtn.grid(row=0,column=2)
        sbtn=Button(btn_frame,text="Reset",command=self.reset,width=8,font=("times new roman", 15, "bold"),bg="black",fg="white")
        sbtn.grid(row=0,column=3)
        sbtn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=15,font=("times new roman", 15, "bold"),bg="black",fg="white")
        sbtn.grid(row=0,column=4)
        sbtn=Button(btn_frame,text="Train Images ",command=self.train_data,width=12,font=("times new roman", 15, "bold"),bg="black",fg="white")
        sbtn.grid(row=0,column=5)

        # btn1_frame=Frame(ci_frame,bd=2,relief=RIDGE)
        # btn1_frame.place(x=50,y=230,width=200,height=50)
        # takP=Button(btn1_frame,text="Take Photo Sample",width=14,font=("times new roman", 15, "bold"),bg="black",fg="white")
        # takP.grid(row=0,column=0)
        

        Right_frame = LabelFrame(main_frame, bd=2, bg="black", relief=RIDGE, text="Student Details", fg="white", font=("times new roman", 40, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=900)

        Search_frame = LabelFrame(Right_frame, bd=2, bg="black", relief=RIDGE, fg="white", font=("times new roman", 30, "bold"))
        Search_frame.place(x=10, y=20, width=690, height=500)

        # search_label = Label(Search_frame, text="Search BY", font=("times new roman", 15, "bold"), bg="black", fg="white")
        # search_label.grid(row=0, column=0, padx=10, sticky=W)

        # se_colbo9 = ttk.Combobox(Search_frame, font=("times new roman", 15, "bold"), state="readonly", width=15)
        # se_colbo9["values"] = ("Select ", "roll_no", "Phone_number")
        # se_colbo9.current(0)
        # se_colbo9.grid(row=0, column=1, padx=10, sticky=W)

        # se_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 10, "bold"))
        # se_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # se_btn = Button(Search_frame, text="Search", width=12, font=("times new roman", 10, "bold"))  # Add text or image for the button
        # se_btn.grid(row=0, column=3)

        # showall_btn = Button(Search_frame, text="Show All", width=13, font=("times new roman", 10, "bold"))
        # showall_btn.grid(row=0, column=4)
        #right frame
        table_frame = Frame(Right_frame, bd=2, bg="black", relief=RIDGE)
        table_frame.place(x=18, y=80, width=650, height=410)
        style = ttk.Style()

        # style.configure("Horizontal.TScrollbar", background="black")
        # style.configure("Vertical.TScrollbar", background="black")

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "rollno", "gender", "dob", "email"), 
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("rollno", text="Roll No")
    

       
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rollno",width=100)
        
        
        self.student_table["show"]="headings"
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetchdata()
        

    # data add
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_pid.get() == "":
            messagebox.showerror("Error", "All fields should be filled", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="$Leaval10", database="sem4facestamp")
                my_cursor = conn.cursor()
                query = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                data = (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(), self.var_pid.get(), self.var_name.get(), self.var_div.get(), self.var_rollno.get())
                my_cursor.execute(query, data)
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("Successful", "Student data has been added", parent=self.root)
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Failed to add student data: {e}", parent=self.root)
    def fetchdata(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="$Leaval10", database="sem4facestamp")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cur_foc=self.student_table.focus()
        content=self.student_table.item(cur_foc)
        data=content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_pid.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_rollno.set(data[7])


    # def update(self):
    #     if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_pid.get() == "":
    #         messagebox.showerror("Error", "All fields should be filled", parent=self.root)
    #     else:
    #         try:
    #             Update=messagebox.askyesno("Update","Do you want to update this student details",p)
    def del_date(self):
        if self.var_dep.get() == "" :
            messagebox.showerror("Error", "Student must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page ","Do you want to delete tehis deteils", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="$Leaval10", database="sem4facestamp")
                    my_cursor = conn.cursor()
                    sql="delete from student where spid=%s"
                    val=(self.var_pid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("Delete","successfullly deleted student details", parent=self.root)
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Failed to delete student data: {e}", parent=self.root)


            #storing images
                
    def reset(self):
        self.var_dep.set("Select Dep")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_pid.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_rollno.set("")

  
    # def generate_dataset(self):

    #     if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_pid.get() == "":
    #         messagebox.showerror("Error", "All fields should be filled", parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(host="localhost", username="root", password="$Leaval10", database="sem4facestamp")
    #             my_cursor = conn.cursor()
    #             my_cursor.execute("select * from student")
    #             myresult=my_cursor.fetchall()
    #             id=0
    #             for x in myresult:
    #                 id+=1
    #             my_cursor.execute("update student set Dep=%s, course=%s, year=%s, sem=%s, spid=%s, sname=%s, division=%s, rollno=%s where spid=%s", (
    #                                                                                 self.var_dep.get(),
    #                                                                                 self.var_course.get(),
    #                                                                                 self.var_year.get(),
    #                                                                                 self.var_sem.get(),  
    #                                                                                 self.var_pid.get(),
    #                                                                                 self.var_name.get(),
    #                                                                                 self.var_div.get(),
    #                                                                                 self.var_rollno.get(),
    #                                                                                 self.var_pid.get()==id+1  ))

    #             conn.commit()
    #             self.fetchdata()
    #             self.reset()
    #             conn.close()

    #             face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')              
    #             def face_cropped(img):
    #                 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #                 faces=face_classifier.detectMultiScale(gray,1.3,5)  #sf=1.3,mn=5
    #                 for (x,y,w,h) in faces:
    #                     face_cropped=img[y:y+h,x:x+w]
    #                     return face_cropped            
    #             cap=cv2.VideoCapture(0)
    #             img_id=0
    #             print(cap)
    #             while True:
    #                 ret,my_frame=cap.read() 
    #                 if face_cropped(my_frame) is not None: 
    #                     img_id+=1
    #                 face=cv2.resize(face_cropped(my_frame),(450,450)) 
    #                 face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
    #                 file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg" 
    #                 cv2.imwrite(file_name_path,face)
    #                 cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
    #                 cv2.imshow("Cropped Face", face)

    #                 if cv2.waitKey(1)==13 or int(img_id)==100: #Enter button ASCI code
    #                     break
    #             cap.release()
    #             cv2.destroyAllWindows()
    #             messagebox.showinfo("Result","Generating data sets completed!!!")

    #         except Exception as es:
    #             print(es)
    #             messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    def train_data(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') 
            imageNp=np.array(img,'uint8')     #uint8...data type in array
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        recognizer = cv2.face.LBPHFaceRecognizer_create() #train the classifier
        recognizer.train(faces,ids)
        recognizer.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_pid.get() == "":
            messagebox.showerror("Error", "All fields should be filled", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="$Leaval10", database="sem4facestamp")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s, course=%s, year=%s, sem=%s, spid=%s, sname=%s, division=%s, rollno=%s where spid=%s", (
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_sem.get(),  
                                                                                    self.var_pid.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_rollno.get(),
                                                                                    self.var_pid.get()==id+1  ))

                conn.commit()
                self.fetchdata()
                self.reset()
                conn.close()

                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')              
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)  #sf=1.3,mn=5
                    if len(faces) == 0:
                        return None
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return cv2.resize(face_cropped, (450, 450))  # Resize the cropped face
                cap=cv2.VideoCapture(0)
                img_id=0
                
                while True:
                    ret,my_frame=cap.read() 
                    if face_cropped(my_frame) is not None: 
                        img_id+=1
                        face=cv2.cvtColor(face_cropped(my_frame),cv2.COLOR_BGR2GRAY) 
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg" 
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100: #Enter button ASCI code
                        break
                cap.release()
                # cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")

            except Exception as es:
                print(es)
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


