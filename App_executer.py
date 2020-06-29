import tkinter as tk
from tkinter import filedialog,Text
import os
#The working screen
root = tk.Tk()
apps = []

#to detect current selected file
if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps=tempApps.split(",")
        #To insert into main array
        apps=[x for x in tempApps if x.strip()]
        print(tempApps)
#to Add the files in your lists  
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename= filedialog.askopenfilename(initialdir = "/" ,title = "Select File",
                                        filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    #To Display the selected executable file on the screen 
    for app in apps:
        label = tk.Label(frame,text=app,bg="gray")
        label.pack()
#To run the selected executable file at once
def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root,height=600,width = 600,bg = "#263042")
canvas.pack()
#The Diunguish between the display screen .
frame = tk.Frame(root,bg="white")
frame.place(relwidth = 0.5, relheight = 0.8,relx = 0.1 ,rely=0.1)
#Button to ececute the opening of file method
openFile = tk.Button(root,text="Open File",padx = 10 ,pady=5,fg="white",bg="#263D42",command = addApp)
openFile.pack()
#button to dunthe the selected files
runApps = tk.Button(root,text="Run Apps",padx = 10 ,pady=5,fg="white",bg="#263D42",command = runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame,text=app)
    label.place(relx = 0.1,rely = 0.1)
    label.pack()

root.mainloop()

with open("save.txt",'w')as f:
    for app in apps:
        f.write(app + ",")
