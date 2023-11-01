import tkinter
from tkinter import messagebox
import random

# creating root window
root = tkinter.Tk()

root.configure(bg = "pink")

root.title("To-Do-List")

root.geometry("325x275")

tasks = []

def update_listbox():

    clear_listbox()

    for task in tasks:
        lbl_tsk.insert("end", task)

def clear_listbox():
    lbl_tsk.delete(0,"end")

###################################################
def on_enter(event):
    event.widget.config(bg='blue', fg='white')

def on_leave(event):
    event.widget.config(bg='white', fg='black')
###################################################

def add_task():

    task = txt_input.get()
   
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("You need to enter a task.")

    txt_input.delete(0,"end")

def asc_sort():
    
    tasks.sort()
    update_listbox()

def dsc_sort():

    tasks.sort()
    tasks.reverse()
    update_listbox()

def del_all():
    confirmed = messagebox.askyesno("Please confirm", "Do you really want to delete all?")
    if confirmed == True:
        global tasks
        tasks = []
        update_listbox()

def delete():
    task = lbl_tsk.get("active")

    if task in tasks:
        tasks.remove(task)

    update_listbox()

def choose_random():

    task = random.choice(tasks)
    lbl_display["text"] = task
    
    update_listbox()
    

def total_tsk():
    number_of_tsk = len(tasks)
    msg = "Nummber of tasks: %s" %number_of_tsk
    lbl_display["text"] = msg

def exit_program():
    root.quit()


lbl_title = tkinter.Label(root, text = "To-Do-List", bg = "pink")
lbl_title.grid(row=0, column=0, columnspan=3)

lbl_display = tkinter.Label(root, text = "", bg = "pink")
lbl_display.grid(row=0,column=1)


txt_input = tkinter.Entry(root, width = 32,fg = "black",bg = "white")
txt_input.grid(row=1,column=1)

button_add_tsk = tkinter.Button(root, text="Add Task",width=15, fg="black", bg = "white", command = add_task)
button_add_tsk.grid(row=1,column=0)

button_asc = tkinter.Button(root, text="Sort(ASC)",width=15, fg="black", bg = "white", command =  asc_sort)
button_asc.grid(row=4,column=0)

button_dsc = tkinter.Button(root, text="Sort(DSC)",width=15, fg="black", bg = "white", command = dsc_sort)
button_dsc.grid(row=5,column=0)

button_del = tkinter.Button(root, text="Delete",width=15, fg="black", bg = "white", command = delete)
button_del.grid(row=3,column=0)

button_del_all = tkinter.Button(root, text="Delete All",width=15, fg="black", bg = "white", command = del_all)
button_del_all.grid(row=2,column=0)

button_choose_random = tkinter.Button(root, text="Choose Random",width=15, fg="black", bg = "white", command = choose_random)
button_choose_random.grid(row=6,column=0)

button_number_tak = tkinter.Button(root, text="Total Task",width=15, fg="black", bg = "white", command = total_tsk)
button_number_tak.grid(row=7,column=0)

button_exit = tkinter.Button(root, text="Exit", fg="black", bg = "white",width=43, command=exit_program)
button_exit.grid(row=8,column=0,columnspan=2)

lbl_tsk = tkinter.Listbox(root,fg = "white",bg = "black",width=32)
lbl_tsk.grid(row=2,column=1,rowspan=6)


buttons = [button_add_tsk,button_asc,button_dsc,button_del,button_del_all,button_choose_random,   button_number_tak,button_exit]

for button in buttons:
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    
root.mainloop()
