# from tkinter import *

# window = Tk()
#
# photo = PhotoImage(file='person.png')
#
# label = Label(window,
#               text="bro, do you even code?",
#               font=('Arial',40,'bold'),
#               fg='#00FF00',
#               bg='black',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#               image=photo,
#               compound='bottom')
# label.pack()
# #label.place(x=0,y=0)
#
# window.mainloop()
############################### ENTRY
# def submit():
#     username = entry.get()
#     print("Hello "+username)
#
# def delete():
#     entry.delete(0,END)
#
# def backspace():
#     entry.delete(len(entry.get())-1, END)
#
# window = Tk()
#
# entry = Entry(window,
#               font=("Arial",50),
#               fg="#00FF00",
#               bg="black")
#
# #entry.insert(0,'Spongebob')
# #entry.config(show="*")
# #entry.config(state=DISABLED)
#
# entry.pack(side=LEFT)
#
# submit_button = Button(window,text="submit",command=submit)
# submit_button.pack(side=RIGHT)
#
# delete_button = Button(window,text="delete",command=delete)
# delete_button.pack(side=RIGHT)
#
# backspace_button = Button(window,text="backspace",command=backspace)
# backspace_button.pack(side=RIGHT)
############################ CHECKBUTTONS
# def display():
#     if(x.get()==1):
#         print("You agree!")
#     else:
#         print("You don't agree :(")
#
# window = Tk()
#
# x = IntVar()
#
# python_photo = PhotoImage(file='Python.png')
#
# check_button = Checkbutton(window,
#                            text="I agree to something",
#                            variable=x,
#                            onvalue=1,
#                            offvalue=0,
#                            command=display,
#                            font=('Arial',20),
#                            fg='#00FF00',
#                            bg='black',
#                            activeforeground='#00FF00',
#                            activebackground='black',
#                            padx=25,
#                            pady=10,
#                            image=python_photo,
#                            compound='left')
# check_button.pack()
################################# RADIOBUTTON
# food = ["pizza","hamburger","hotdog"]
#
# def order():
#     if(x.get()==0):
#         print("You ordered pizza!")
#     elif(x.get()==1):
#         print("You ordered a hamburger!")
#     elif(x.get()==2):
#         print("You ordered a hotdog!")
#     else:
#         print("huh?")
#
# window = Tk()
#
# pizzaImage = PhotoImage(file='pizza.png')
# hamburgerImage = PhotoImage(file='hamburger.png')
# hotdogImage = PhotoImage(file='hotdog.png')
# foodImages = [pizzaImage,hamburgerImage,hotdogImage]
#
# x = IntVar()
#
# for index in range(len(food)):
#     radiobutton = Radiobutton(window,
#                               text=food[index], #adds text to radio buttons
#                               variable=x, #groups radiobuttons together if they share the same variable
#                               value=index, #assigns each radiobutton a different value
#                               padx = 25, #adds padding on x-axis
#                               font=("Impact",50),
#                               image = foodImages[index], #adds image to radiobutton
#                               compound = 'left', #adds image & text (left-side)
#                               #indicatoron=0, #eliminate circle indicators
#                               #width = 375, #sets width of radio buttons
#                               command=order #set command of radiobutton to function
#                               )
#     radiobutton.pack(anchor=W)
##################################### LISTBOX
# listbox = A listing of selectable text items within it's own container

# def submit():
#
#     food = []
#
#     for index in listbox.curselection():
#         food.insert(index,listbox.get(index))
#
#     print("You have ordered: ")
#     for index in food:
#         print(index)
#
# def add():
#     listbox.insert(listbox.size(),entryBox.get())
#     listbox.config(height=listbox.size())
#
# def delete():
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)
#
#     listbox.config(height=listbox.size())
#
#
# window = Tk()
#
# listbox = Listbox(window,
#                   bg="#f7ffde",
#                   font=("Constantia",35),
#                   width=12,
#                   selectmode=MULTIPLE)
# listbox.pack()
#
# listbox.insert(1,"pizza")
# listbox.insert(2,"pasta")
# listbox.insert(3,"garlic bread")
# listbox.insert(4,"soup")
# listbox.insert(5,"salad")
#
# listbox.config(height=listbox.size())
#
# entryBox = Entry(window)
# entryBox.pack()
#
# frame = Frame(window)
# frame.pack()
#
# submitButton = Button(frame,text="submit",command=submit)
# submitButton.pack(side=LEFT)
#
# addButton = Button(frame,text="add",command=add)
# addButton.pack(side=LEFT)
#
# deleteButton = Button(frame,text="delete",command=delete)
# deleteButton.pack(side=LEFT)
################################### MESSAGEBOX
# def click():
    #messagebox.showinfo(title='This is an info message box',message='You are a person')
    #messagebox.showwarning(title='WARNING!',message='You have A VIRUS!!!!')
    #messagebox.showerror(title='ERROR!',message='something went wrong :(')

    #if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
        #print('You did a thing!')
    #else:
        #print('You canceled a thing! :(')

    #if messagebox.askretrycancel(title='ask ok cancel',message='Do you want retry the thing?'):
        #print('You retried a thing!')
    #else:
        #print('You canceled a thing! :(')

    #if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
        #print('I like cake too :)')
    #else:
        #print('Why do you not like cake? :(')

    #answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
    #if(answer == 'yes'):
        #print('I like pie too :)')
    #else:
        #print('Why do you not like pie? :(')

    #answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?',icon='question')
    #if(answer==True):
        #print("You like to code :)")
    #elif(answer==False):
        #print("Then why are you watching a video on coding?")
    #else:
        #print("You have dodged the question ")

# window = Tk()
#
# button = Button(window,command=click,text='click me')
# button.pack()
################################## COLOR CHOOSER
# from tkinter import colorchooser
# def click():
#     color = colorchooser.askcolor()
#     colorHex = color[1]
#     window.config(bg=colorHex)
#
# window = Tk()
# window.geometry("420x420")
# button = Button(text='click me',command=click)
# button.pack()
################################# TEXT AREA
# def submit():
#     input = text.get("1.0",END)
#     print(input)
#
# window = Tk()
# text = Text(window,
#             bg="light yellow",
#             font=("Ink Free",25),
#             height=8,
#             width=20,
#             padx=20,
#             pady=20,
#             fg="purple")
# text.pack()
# button = Button(window,text="submit",command=submit)
# button.pack()
################################# OPEN FILE DIALOG
# from tkinter import *
# from tkinter import filedialog
#
# def openFile():
#     filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
#                                           title="Open file okay?",
#                                           filetypes= (("text files","*.txt"),
#                                           ("all files","*.*")))
#     file = open(filepath,'r')
#     print(file.read())
#     file.close()
#
# window = Tk()
# button = Button(text="Open",command=openFile)
# button.pack()
################################ SAVE FILE DIALOG
# from tkinter import filedialog
#
# def saveFile():
#     file = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
#                                     defaultextension='.txt',
#                                     filetypes=[
#                                         ("Text file",".txt"),
#                                         ("HTML file", ".html"),
#                                         ("All files", ".*"),
#                                     ])
#     if file is None:
#         return
#     filetext = str(text.get(1.0,END))
#     #filetext = input("Enter some text I guess: ") //use this if you want to use console window
#     file.write(filetext)
#     file.close()
#
# window = Tk()
# button = Button(text='save',command=saveFile)
# button.pack()
# text = Text(window)
# text.pack()
############################### MENUBAR
# def openFile():
#     print("File has been opened!")
# def saveFile():
#     print("File has been saved!")
# def cut():
#     print("You cut some text!")
# def copy():
#     print("You copied some text!")
# def paste():
#     print("You pasted some text!")
#
# window = Tk()
#
# openImage = PhotoImage(file="file.png")
# saveImage = PhotoImage(file="save.png")
# exitImage = PhotoImage(file="exit.png")
#
# menubar = Menu(window)
# window.config(menu=menubar)
#
# fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="File",menu=fileMenu)
# fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
# fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
# fileMenu.add_separator()
# fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')
#
# editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="Edit",menu=editMenu)
# editMenu.add_command(label="Cut",command=cut)
# editMenu.add_command(label="Copy",command=copy)
# editMenu.add_command(label="Paste",command=paste)
############################### FRAME
# window = Tk()
#
# frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
# frame.pack()
#
# Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
# Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)
############################### OPEN NEW WINDOWS
# def create_window():
#     new_window = Tk()       #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
#                             #Tk() = new independent window
#     #old_window.destroy()   #close out of old window
#
# old_window = Tk()
#
# Button(old_window,text="create new window",command=create_window).pack()
############################### WINDOWS TABS
# from tkinter import ttk
#
# window = Tk()
#
# notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays
#
# tab1 = Frame(notebook) #new frame for tab 1
# tab2 = Frame(notebook) #new frame for tab 2
#
# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2,text="Tab 2")
# notebook.pack(expand=True,fill="both")  #expand = expand to fill any space not otherwise used
#                                        #fill = fill space on x and y axis
# Label(tab1,text="Hello, this is tab#1",width=50,height=25).pack()
# Label(tab2,text="Goodbye, this is tab#2",width=50,height=25).pack()
################################ GUI GRID
# from tkinter import *
#
# #grid() = geometry manager that organizes widgets in a table-like structure in a parent widget
#
# window = Tk()
#
# titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)
#
# firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
# firstNameEntry = Entry(window).grid(row=1,column=1)
#
# lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
# lastNameEntry = Entry(window).grid(row=2,column=1)
#
# emailLabel = Label(window,text="email: ",bg="blue").grid(row=3,column=0)
# emailEntry = Entry(window).grid(row=3,column=1)
#
# submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)
################################# PROGRESS BAR
# from tkinter.ttk import *
# import time
#
# def start():
#     GB = 100
#     download = 0
#     speed = 1
#     while(download<GB):
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download+=speed
#         percent.set(str(int((download/GB)*100))+"%")
#         text.set(str(download)+"/"+str(GB)+" GB completed")
#         window.update_idletasks()
#
# window = Tk()
#
# percent = StringVar()
# text = StringVar()
#
# bar = Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)
#
# percentLabel = Label(window,textvariable=percent).pack()
# taskLabel = Label(window,textvariable=text).pack()
#
# button = Button(window,text="download",command=start).pack()
############################### CANVAS
# window = Tk()
#
# canvas = Canvas(window,height=500,width=500)
# #canvas.create_line(0,0,500,500,fill="blue",width=5)
# #canvas.create_line(0,500,500,0,fill="red",width=5)
# #canvas.create_rectangle(50,50,250,250,fill="purple")
# #points = [250,0,500,500,0,500]
# #canvas.create_polygon(points,fill="yellow",outline="black",width=5)
# #canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)
# canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
# canvas.create_oval(190,190,310,310,fill="white",width=10)
# canvas.pack()
############################## KEYBOARD EVENTS
# def doSomething(event):
#     #print("You pressed: " + event.keysym)
#     label.config(text=event.keysym)
#
# window = Tk()
#
# window.bind("<Key>",doSomething)
#
# label = Label(window,font=("Helvetica",100))
# label.pack()
############################### MOUSE EVENTS
# def doSomething(event):
#     print("Mouse coordinates: " + str(event.x)+","+str(event.y))
#
# window = Tk()
#
# window.bind("<Button-1>",doSomething) #left mouse click
#window.bind("<Button-2>",doSomething) #scroll wheel
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething)#mousebutton release
#window.bind("<Enter>",doSomething) #enter the window
#window.bind("<Leave>",doSomething) #leave the window
#window.bind("<Motion>",doSomething) #Where the mouse moved
############################### DRAG AND DROP
# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y
#
# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)
#
# window = Tk()
#
# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)
#
# label2 = Label(window,bg="blue",width=10,height=5)
# label2.place(x=100,y=100)
#
# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)
#
# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)
################################ CLOCK
# from time import *
#
# def update():
#     time_string = strftime("%I:%M:%S %p")
#     time_label.config(text=time_string)
#
#     day_string = strftime("%A")
#     day_label.config(text=day_string)
#
#     date_string = strftime("%B %d, %Y")
#     date_label.config(text=date_string)
#
#     window.after(1000,update)
#
#
# window = Tk()
#
# time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
# time_label.pack()
#
# day_label = Label(window,font=("Ink Free",25,"bold"))
# day_label.pack()
#
# date_label = Label(window,font=("Ink Free",30))
# date_label.pack()
#
# update()


# window.mainloop()