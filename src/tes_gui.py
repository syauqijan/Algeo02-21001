from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

window = Tk() 
window.title("Face Recognition")    
window.geometry("992x558")
window.resizable(0, 0)
bg = PhotoImage(file = "src/bg.png")
label_bg = Label(window, image = bg)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

def open_img1():
    global my_image
    window.filename = filedialog.askopenfilename(initialdir = "test/dataset/pins_Zendaya", title = "Select A File", filetype = (("jpeg files", "*.jpg"), ("all files", "*.*")))
    # my_label = Label(window, text=window.filename)
    my_image = ImageTk.PhotoImage(Image.open(window.filename))
    # my_image.resize((200, 200), Image.ANTIALIAS)
    my_image_label = Label(image=my_image).place(x=300, y=300)

def open_img2():
    global my_image
    window.filename = filedialog.askopenfilename(initialdir = "test/dataset/pins_Zendaya", title = "Select A File", filetype = (("jpeg files", "*.jpg"), ("all files", "*.*")))
    # my_label = Label(window, text=window.filename)
    my_image = ImageTk.PhotoImage(Image.open(window.filename))
    my_image_label = Label(image=my_image).pack()

button1 = Button(window, text="Choose File", command=open_img1, font=("Arial Bold", 14), fg="#909fc7", bg="white", activebackground="white", activeforeground="white", bd=0).place(x=36, y=220)
button2 = Button(window, text="Choose File", command=open_img1, font=("Arial Bold", 14), fg="#909fc7", bg="white", activebackground="white", activeforeground="white", bd=0).place(x=36, y=308)

window.mainloop()

