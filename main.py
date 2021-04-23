from tkinter import *
from PIL import ImageTk, Image
txt = ""
res = False
ans = 0

def press(num):
    global txt, ans, res
    if (res == True):
        txt = ans
        res = False
    txt = txt + str(num)
    equation.set(txt)

def clear():
   global txt, ans, res
   txt = ""
   equation.set("")
   res = False


def equal():
    try:
        global txt, ans, res
        ans = str(eval(txt))
        equation.set(ans)
        res = True
    except:
        equation.set("ERROR : Invalid Equation")
        txt = ""
if __name__ == "__main__":
    root = Tk()
    root.iconbitmap=('ig.ico')
    root.title("Ruby's Calculator")
    equation = StringVar()
    txt_field = Entry(relief=RIDGE, textvariable=equation, bd=10, font=("Aerial", 20), bg="powder blue")
    txt_field.grid(columnspan=4, ipady=10, ipadx=10, sticky="nsew")
    width = 80
    height = 80
    img1 = Image.open("1.png")
    img1 = img1.resize((width, height))
    oneImage = ImageTk.PhotoImage(img1)
    button_1 = Button(root,padx=40,pady=20,image=oneImage,bd=8,command=lambda :press(1))
    img2 = Image.open("2.png")
    img2 = img2.resize((width, height))
    twoImage = ImageTk.PhotoImage(img2)
    button_2 = Button(root,padx=40,pady=20,image=twoImage,bd=8,command=lambda :press(2))
    img3 = Image.open("3.png")
    img3 = img3.resize((width, height))
    threeImage = ImageTk.PhotoImage(img3)
    button_3 = Button(root,image=threeImage,padx=40,pady=20,bd=8,command=lambda : press(3))
    img4 = Image.open("4.png")
    img4 = img4.resize((width, height))
    fourImage = ImageTk.PhotoImage(img4)
    button_4 = Button(root,image=fourImage,padx=40,pady=20,bd=8,command=lambda : press(4))
    img5 = Image.open("5.png")
    img5 = img5.resize((width, height))
    fiveImage = ImageTk.PhotoImage(img5)
    button_5 = Button(root,image=fiveImage,padx=40,pady=20,bd=8,command=lambda : press(5))
    img6 = Image.open("6.png")
    img6 = img6.resize((width, height))
    sixImage = ImageTk.PhotoImage(img6)
    button_6 = Button(root,image=sixImage,padx=40,pady=20,bd=8,command=lambda : press(6))
    img7 = Image.open("7.png")
    img7 = img7.resize((width, height))
    sevenImage = ImageTk.PhotoImage(img7)
    button_7 = Button(root,image=sevenImage,padx=40,pady=20,bd=8,command=lambda : press(7))
    img8 = Image.open("8.png")
    img8 = img8.resize((width, height))
    eightImage = ImageTk.PhotoImage(img8)
    button_8 = Button(root,image=eightImage,padx=40,pady=20,bd=8,command=lambda : press(8))
    img9 = Image.open("9.png")
    img9 = img9.resize((width, height))
    nineImage = ImageTk.PhotoImage(img9)
    button_9 = Button(root,image=nineImage,padx=40,pady=20,bd=8,command=lambda : press(9))
    img0 = Image.open("0.png")
    img0 = img0.resize((width, height))
    zeroImage = ImageTk.PhotoImage(img0)
    button_0 = Button(root,image=zeroImage,padx=40,pady=20, bd=8,command=lambda :press(0))
    imgadd = Image.open("plus.png")
    imgadd = imgadd.resize((width, height))
    addImage = ImageTk.PhotoImage(imgadd)
    button_add = Button(root,image=addImage,padx=40,pady=20, bd=8,command=lambda :press("+"))
    imgsub = Image.open("sub.png")
    imgsub = imgsub.resize((width, height))
    subImage = ImageTk.PhotoImage(imgsub)
    button_sub = Button(root,image=subImage,padx=40,pady=20,bd=8,command=lambda : press("-"))
    imgx = Image.open("mul.png")
    imgx = imgx.resize((width, height))
    multiplyImage = ImageTk.PhotoImage(imgx)
    button_mul = Button(root,image=multiplyImage,padx=40,pady=20,bd=8,command=lambda : press("*"))
    imgdiv = Image.open("div.png")
    imgdiv = imgdiv.resize((width, height))
    divImage = ImageTk.PhotoImage(imgdiv)
    button_div = Button(root,image=divImage,padx=40,pady=20,bd=8,command=lambda : press("/"))
    imgeq = Image.open("eq.png")
    imgeq = imgeq.resize((width, height))
    eqImage = ImageTk.PhotoImage(imgeq)
    button_equal = Button(root,image=eqImage,padx=40,pady=20,bd=8,command=equal)
    imgclear = Image.open("c.png")
    imgclear = imgclear.resize((width, height))
    clearImage = ImageTk.PhotoImage(imgclear)
    button_clear = Button(root,image=clearImage,padx=40,pady=20,bd=8,command=clear)

    #putting buttons in the screen
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_clear.grid(row=4,column=2)
    button_add.grid(row=1, column=3)
    button_sub.grid(row=2, column=3)
    button_mul.grid(row=3, column=3)
    button_div.grid(row=4, column=3)
    button_equal.grid(row=4, column=1)

root.mainloop()
