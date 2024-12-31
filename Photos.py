# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk, ImageDraw
# from student import Student




# class Photos:
#     def __init__(self, root):
#         self.root=root
#         self.root.geometry("1550x790+0+0")
#         self.root.title("FaceStamp")

#         img6 = Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\page2.jpeg")
#         img6 = img6.resize((1550, 790), Image.ADAPTIVE)
#         self.photoimg6 = ImageTk.PhotoImage(img6)
#         f_lbl6 = Label(self.root, image=self.photoimg6)
#         f_lbl6.place(x=0, y=0, width=1550, height=790)
        

# if __name__ == "__main__":
#     root = Tk()
#     obj = Photos(root)
#     root.mainloop()


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import os

class Photos:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x790+0+0")
        self.root.title("FaceStamp")

        img6 = Image.open(r"C:\Users\Valeska\Desktop\Sem4MiniProject\ImagesForGUI\page2.jpeg")
        img6 = img6.resize((1550, 790), Image.ADAPTIVE)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        f_lbl6 = Label(self.root, image=self.photoimg6)
        f_lbl6.place(x=0, y=0, width=1550, height=790)



        # Get the path to the directory containing the images
        images_dir = 'data/images'

        # Get the list of image files in the directory
        image_files = os.listdir(images_dir)

        # Create a new Toplevel window to display the images
        image_window = Toplevel(self.root)
        image_window.title("Photos")

        # Display the images in the window
        row, col = 0, 0
        for image_file in image_files:
            # Load the image
            img_path = os.path.join(images_dir, image_file)
            img = Image.open(img_path)
            img.thumbnail((200, 200))  # Resize the image if necessary

            # Convert the image to Tkinter PhotoImage
            photoimg = ImageTk.PhotoImage(img)

            # Create a Label to display the image
            label = Label(image_window, image=photoimg)
            label.grid(row=row, column=col, padx=10, pady=10)

            # Keep a reference to the PhotoImage object to prevent it from being garbage collected
            label.image = photoimg

            # Increment row and column for next image
            col += 1
            if col == 3:
                col = 0
                row += 1

if __name__ == "__main__":
    root = Tk()
    obj = Photos(root)
    root.mainloop()