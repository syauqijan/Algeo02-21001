from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from step1 import *
from eigenfaces import *
from eucidilian import *
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import time

def main():
    global folder_path, file_path, start_time, end_time
    start_time = time.time()
    data = folder_path.get()
    image_name = []
    for filename in os.listdir(data):
        image_name.append(filename)
    images = load_images_from_foldergray(data)
    colorimg = load_images_from_folder(data)
    images = resize_image(images)

    mean = meanSetImg(images)

    imgvect = imagevector(images)

    normvect = normalvect(imgvect)

    covariance = covarian(imgvect)

    tempval, eigvect = qreigen(covariance)

    eigfacearr = eigface(eigvect,imgvect)


    test = file_path.get()

    testimg = cv2.imread(test,0)

    testimg = cv2.resize(testimg,(256,256),interpolation = cv2.INTER_AREA)

    normtest = normimg(testimg,mean)
    normdata = normilazi(images)

    wtest = weighttest(eigfacearr,normtest)

    w = weightdata(eigfacearr,normdata)

    x, similarity = distance(wtest,w)

    # showimg(colorimg,x)
    print(image_name[x])
    closest_path = os.path.join(data, image_name[x])
    closest_img = Image.open(closest_path)
    closest_img = closest_img.resize((240, 240))
    closest_img = ImageTk.PhotoImage(closest_img)
    closest_img_label = Label(image=closest_img)
    closest_img_label.image = closest_img
    closest_img_label.place(x=695, y=205)
    end_time = time.time()
    ex_time1 = get_elapsed_time()
    ex_time = str(round(ex_time1, ndigits=2)) + " detik"
    ex_time_label = Label(window, text= ex_time , font=("Arial Bold", 13), fg="#909fc7", bg="white", bd=0)
    ex_time_label.place(x=532, y=515)

def get_elapsed_time():
    return end_time - start_time

def open_folder():
    global no_folder
    filename = filedialog.askdirectory(initialdir = "test/dataset", title = "Select A Folder")
    shortfilename = filename.split('/')[len(filename.split('/'))-1]
    label_folder = Label(window, text=shortfilename, font=("Arial Bold", 9), fg="#909fc7", bg="white", bd=0)
    label_folder.place(x=190, y=230)
    no_folder.config(text=label_folder)
    folder_path.set(filename)
    folder_path.get()

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
    file_path.set(filename)
    file_path.get()
    
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
folder_path = StringVar()
file_path = StringVar()

button1 = Button(window, text="Choose Folder", command=open_folder , font=("Arial Bold", 14), fg="#909fc7", bg="white", activebackground="white", activeforeground="white", bd=0)
button1.place(x=23, y=220)
button2 = Button(window, text="Choose File", command=open_file, font=("Arial Bold", 14), fg="#909fc7", bg="white", activebackground="white", activeforeground="white", bd=0)
button2.place(x=36, y=308)
button3 = Button(window, text="CHECK",command=main, font=("Arial Bold", 14), fg="white", bg="#d7ccd9", activebackground="#d7ccd9", activeforeground="white", bd=0)
button3.place(x=53, y=398)


window.mainloop()