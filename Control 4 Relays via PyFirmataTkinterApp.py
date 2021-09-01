#Control 4 Relays by Pyfirmata App in Python Programming
from tkinter import *
from pyfirmata import Arduino, util#importing Arduino and utility from pyfirmata mpdule
board = Arduino('Com11')# Create a variable name board and assign the Arduino board and COM Port
root=Tk()
root.geometry('500x600')
root.title("PyFirmata App")
root.iconbitmap("python_logo_icon.ico")
Appname=Label(root,text='WELCOME TO ANOKHAUTOMATION',fg='purple',bg='white',font="Georgea 20 bold")
Appname.pack(pady=10)
root.configure(background="yellow")
on_image =PhotoImage(file='Toggle-off-96.png')
off_image =PhotoImage(file='Toggle-on-96.png')
global relay1
global relay2
global relay3
global relay4
relay1 =True
relay2 =True
relay3 =True
relay4 =True
#Define Button1 function
def Button_1():
    global relay1
    if relay1:
        board.digital[12].write(1)#Arduino pin 12 High
        button_1.config(image=off_image)
        load1_label.config(text="LOAD 1 is Off",fg="blue")
        relay1=False
    else:
        board.digital[12].write(0)#Arduino pin 12 Low
        button_1.config(image=on_image)
        load1_label.config(text="LOAD 1 is ON",fg="red")
        relay1=True
#Define button2 function
def Button_2():
        global relay2
        if relay2:
            board.digital[11].write(1)#Arduino pin 11 High
            button_2.config(image=off_image)
            load2_label.config(text="LOAD 2 is Off", fg="blue")
            relay2 = False
        else:
            board.digital[11].write(0)#Arduino pin 11 Low
            button_2.config(image=on_image)
            load2_label.config(text="LOAD 2 is ON", fg="red")
            relay2 = True
#Function for Button-3
def Button_3():
    global relay3
    if relay3:
        board.digital[10].write(1)#Arduino pin 10 High
        button_3.config(image=off_image)
        load3_label.config(text="LOAD 3 is Off",fg="blue")
        relay3=False
    else:
        board.digital[10].write(0)#Arduino pin 10 Low
        button_3.config(image=on_image)
        load3_label.config(text="LOAD 3 is ON",fg="red")
        relay3=True
#Function for Button -4
def Button_4():
        global relay4
        if relay4:
            board.digital[9].write(1)#Arduino pin 9 High
            button_4.config(image=off_image)
            load4_label.config(text="LOAD 4 is Off", fg="blue")
            relay4 = False
        else:
            board.digital[9].write(0)#Arduino pin 9 Low
            button_4.config(image=on_image)
            load4_label.config(text="LOAD 4 is ON", fg="red")
            relay4 = True
#label for Load-1
load1_label=Label(root,text="Click Btn-1 ",bg="yellow",fg="green",font=("Verdana",15,"bold"))
load1_label.pack(pady=1,)
#button for Load-1
button_1=Button(root,image=off_image,bg='yellow',borderwidth=0,command=Button_1)
button_1.pack(pady=1)
#label for Load-2
load2_label=Label(root,text="Click Btn-2",bg="yellow",fg="green",font=("Verdana",15,"bold"))
load2_label.pack(pady=1)
#button for Load-2
button_2=Button(root,image=off_image,bg='yellow',borderwidth=0,command=Button_2)
button_2.pack(pady=1)
#label for Load-3
load3_label=Label(root,text="Click Btn-3",bg="yellow",fg="green",font=("Verdana",15,"bold"))
load3_label.pack(pady=1)
#button for Load-3
button_3=Button(root,image=off_image,bg='yellow',borderwidth=0,command=Button_3)
button_3.pack(pady=1)
#label for Load-4
load4_label=Label(root,text="Click Btn-4",bg="yellow",fg="green",font=("Verdana",15,"bold"))
load4_label.pack(pady=1)
#button for Load-4
button_4=Button(root,image=off_image,bg='yellow',borderwidth=0,command=Button_4)
button_4.pack(pady=1)
root.mainloop()