import tkinter
from PIL import ImageTk,Image

root = tkinter.Tk()
root.title('show image')
read_image = Image.open('./test.png')
image_canvas = tkinter.Canvas(width=100,height=100)
image_canvas.pack()
im = ImageTk.PhotoImage(image=read_image)
image_canvas.create_image(0,0,anchor='nw',image=im)


root.mainloop()
