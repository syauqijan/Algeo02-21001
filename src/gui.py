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
no_folder = Label(window, text="No folder chosen", font=("Arial Bold", 9), fg="#909fc7", bg="white", bd=0)
no_folder.place(x=190, y=230)
no_file2 = Label(window, text="No file chosen", font=("Arial Bold", 9), fg="#909fc7", bg="white", bd=0)
no_file2.place(x=190, y=320)

bp = Image.open("src/bp.jpg")
bp = bp.resize((240, 240), Image.ANTIALIAS)
bp = ImageTk.PhotoImage(bp)
bp_label = Label(window, image=bp)
bp_label.image = bp_label
bp_label.place(x=365, y=205)
bp2 = Image.open("src/bp.jpg")
bp2 = bp2.resize((240, 240), Image.ANTIALIAS)
bp2 = ImageTk.PhotoImage(bp2)
bp2_label = Label(window, image=bp2)
bp2_label.image = bp2_label
bp2_label.place(x=695, y=205)

def open_folder():
    global no_folder
    filename = filedialog.askdirectory(initialdir = "test/dataset", title = "Select A Folder")
    # my_image = Image.open(filename)
    # my_image = my_image.resize((240, 240), Image.ANTIALIAS)
    # my_image = ImageTk.PhotoImage(my_image)
    # my_image_label = Label(window, image=my_image)
    # my_image_label.image = my_image
    # my_image_label.place(x=365, y=205)
    shortfilename = filename.split('/')[len(filename.split('/'))-1]
    label_folder = Label(window, text=shortfilename, font=("Arial Bold", 9), fg="#909fc7", bg="white", bd=0)
    label_folder.place(x=190, y=230)
    no_folder.config(text=label_folder)
    
def open_file():
    global my_image
    filename = filedialog.askopenfilename(initialdir = "test/dataset", title = "Select A File", filetype = (("jpeg files", "*.jpg"), ("all files", "*.*")))
    # my_label = Label(window, text=window.filename)       
    my_image = Image.open(filename)
    my_image = my_image.resize((240, 240), Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(my_image)
    my_image_label = Label(window, image=my_image)
    my_image_label.image = my_image
    my_image_label.place(x=365, y=205)
    shortfilename = filename.split('/')[len(filename.split('/'))-1]
    label_image = Label(window, text=shortfilename, font=("Arial Bold", 9), fg="#909fc7", bg="white", bd=0)
    label_image.place(x=190, y=320)
    no_file2.config(text=label_image)


button1 = Button(window, text="Choose Folder", command=open_folder , font=("Arial Bold", 14), fg="#909fc7", bg="white", activebackground="white", activeforeground="white", bd=0)
button1.place(x=23, y=220)
button2 = Button(window, text="Choose File", command=open_file, font=("Arial Bold", 14), fg="#909fc7", bg="white", activebackground="white", activeforeground="white", bd=0)
button2.place(x=36, y=308)

window.mainloop()

