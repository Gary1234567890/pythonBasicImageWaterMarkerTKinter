from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def openfile():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(root.filename)
    im = Image.open(root.filename)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = "Gary Pictures"

    font = ImageFont.truetype('arial.ttf', 86)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    im.show()

    #Save watermarked image
    #im.save('images/watermark.jpg')

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
