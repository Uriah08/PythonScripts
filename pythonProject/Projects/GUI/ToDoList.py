from tkinter import *
from tkinter import ttk

class ToDoList:
    def __init__(self,window):
        self.window = window
        self.window.title("To Do List")
        self.todos = []
        self.draw()

    def draw(self):
        self.title_frame = Frame(window,bg="gray")
        self.title_frame.grid(row=0)
        self.title_label = Label(self.title_frame,text="To Do List",font=("Arial",50),fg="black",bg="gray")
        self.title_label.grid(row=0)
        self.add_label = Label(self.title_frame,text="Add List: ",bg="gray",font=("Arial",15),fg="black")
        self.add_label.grid(row=1,sticky="w",column=0,padx=5)
        self.text_list_area = Entry(self.title_frame,width=35)
        self.text_list_area.grid(row=1,pady=10,padx=10,column=0,sticky="e")
        self.list_frame = Frame(window)
        self.list_frame.grid(row=1)
        self.btn_frame = Frame(window)
        self.btn_frame.grid(row=2)
        self.add_btn = Button(self.btn_frame,text="Add",font=("Arial",10),bg="gray",fg="black",
                              activebackground="gray").grid(column=0,pady=5,padx=8)
        self.remove_btn = Button(self.btn_frame, text="Complete", font=("Arial", 10), bg="gray", fg="black",
                              activebackground="gray").grid(column=1,row=0, pady=5,padx=8)

    def add(self):
        pass
    def complete(self):
        pass


window = Tk()
start = ToDoList(window)
window.mainloop()