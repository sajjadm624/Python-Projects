from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Image Viewer')
root.iconbitmap('c:/gui/imageviewerlogo.png')

my_img1 = ImageTk.PhotoImage(Image.open('c:/Users/SazzadHossain/Desktop/Python_GUI/ImageViewer/image1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('c:/Users/SazzadHossain/Desktop/Python_GUI/ImageViewer/image2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('c:/Users/SazzadHossain/Desktop/Python_GUI/ImageViewer/image3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('c:/Users/SazzadHossain/Desktop/Python_GUI/ImageViewer/image4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('c:/Users/SazzadHossain/Desktop/Python_GUI/ImageViewer/image5.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('c:/Users/SazzadHossain/Desktop/Python_GUI/ImageViewer/image6.jpg'))
my_img7 = ImageTk.PhotoImage(Image.open('c:/Users/SazzadHossain/Desktop/Python_GUI/ImageViewer/image7.jpg'))
my_img8 = ImageTk.PhotoImage(Image.open('c:/Users/SazzadHossain/Desktop/Python_GUI/ImageViewer/image8.jpg'))
my_img9 = ImageTk.PhotoImage(Image.open('c:/Users/SazzadHossain/Desktop/Python_GUI/ImageViewer/image9.jpg'))


image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9]

my_label = Label(image=my_img1)
my_label.grid(row=0 , column=0, columnspan=3)

def next(image_number):
	global my_label
	global button_next
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_next = Button(root, text=">>", command=lambda: next(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 9:
		button_next = Button(root, text=">>", state=DISABLED)


	my_label.grid(row=0,column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_next.grid(row=1, column=2)






def back(image_number):
	global my_label
	global button_next
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_next = Button(root, text=">>", command=lambda: next(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 0:
		button_back = Button(root, text="<<", state=DISABLED)


	my_label.grid(row=0,column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_next.grid(row=1, column=2)







button_back = Button(root, text="<<", command=back,state=DISABLED)
button_next = Button(root, text=">>", command=lambda: next(2) )
button_exit = Button(root, text="EXIT", command= root.quit)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1, column=2)


root.mainloop()