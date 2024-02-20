from tkinter import *

root = Tk()
root.geometry("=400x200")  # Use "x" instead of "*"

def getvals():
    print("Accepted")

Label(root ,text = "Python Registration Form" ,  font  = "ar 15 bold").grid(row=0 , column =3)

name =Label (root ,  text = "Name")
phone =Label (root ,  text = "Phone")
gender = Label (root ,  text = "Gender")
emg =Label (root ,  text = "Emergency")
payment = Label (root,  text ="Payment Mood")

name.grid(row =1 , column =2)
phone.grid(row =2 , column =2)
gender.grid(row =3 , column =2)
emg.grid(row =4 , column =2)
payment.grid(row =5 , column =2)

namevalue =  StringVar
phonevalue =  StringVar
genderval =  StringVar
emgvalue =  StringVar
paymentvalue=  StringVar
checkvalue =  StringVar

nameentry =  Entry(root, textvariable=namevalue)
phonevalue =  Entry(root, textvariable=phonevalue)
genderentry =  Entry(root, textvariable=genderval)
emgentry =  Entry(root, textvariable=emgvalue)
paymententry =  Entry(root, textvariable=paymentvalue)

nameentry.grid(row=1 , column=3)
phonevalue.grid(row=2 , column=3)
genderentry.grid(row=3 , column=3)
emgentry.grid(row=4 , column=3)
paymententry.grid(row=5 , column=3)


checkbtn = Checkbutton(text = "Remember me  ? ", variable = checkvalue)
checkbtn.grid(row=6 , column=3)

Button(text ="Submit", command=getvals).grid(row=7 , column=3)

root.mainloop()