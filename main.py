from tkinter import *
import backend

# ====================  windows  =======================
window = Tk()
window.title("book store")
window.geometry("620x360")
window.resizable(width=False,height=False)
color='#e0e0e0'
window.config(bg=color)
# ====================  static function  =======================
def clear_list():
    list1.delete(0,END)

def fill_list(books):
    for book in books:
        list1.insert(END,book)

# ====================  Label  =======================

l1 = Label(window, text=' Title',bd='3',anchor=CENTER,font=('B Tir',12,'bold'),width='8',height='1',bg='#b87679',padx='3',pady='3')
l1.grid(row=0, column=0,padx='10',pady='5')

l2 = Label(window, text=' Author',anchor=CENTER,font=('B Tir',12,'bold'),bd='3',width='8',height='1',bg='#b87679',padx='3',pady='3')
l2.grid(row=0, column=2,padx='10',pady='5')

l3 = Label(window, text=' Year',anchor=CENTER,font=('B Tir',12,'bold'),bd='3',width='8',height='1',bg='#b87679',padx='3',pady='3')
l3.grid(row=1, column=0,padx='10',pady='5')

l4 = Label(window, text='ISBN',anchor=CENTER,font=('B Tir',12,'bold'),bd='3',width='8',height='1',bg='#b87679',padx='3',pady='3')
l4.grid(row=1, column=2,padx='10',pady='5')

# ====================  Entry  =======================
title_text = StringVar()
e1 = Entry(window, textvariable=title_text,bd='4',font=('mitra',12,'bold'),width='15')
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text,bd='4',font=('mitra',12,'bold'),width='15')
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text,bd='4',font=('mitra',12,'bold'),width='15')
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text,bd='4',font=('mitra',12,'bold'),width='15')
e4.grid(row=1, column=3)


# =============  ListBox and Scrollbar  ================
list1 = Listbox(window, width=39, height=10,activestyle='dotbox',bd ='3',font=('mitra',10,'bold'),highlightcolor='red',relief=RAISED)
list1.grid(row=4, column=0, rowspan=5, columnspan=2,pady='10',padx='20')

sb1 = Scrollbar(window,width='20')
#sb1.grid(row=1, column=1, rowspan=5)
sb1.place(x=300,y=140)



list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

def get_selected_row(event):
    global select_book
    if len(list1.curselection()) >0:
        index=list1.curselection()[0]
        select_book=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,select_book[1])
        e2.delete(0,END)
        e2.insert(END,select_book[2])
        e3.delete(0,END)
        e3.insert(END,select_book[3])
        e4.delete(0,END)
        e4.insert(END,select_book[4])
    
list1.bind("<<ListboxSelect>>",get_selected_row)

# =======================================  Button  ======================================
#================  View All  ==============
def view_command():
    clear_list()
    books=backend.view()
    fill_list(books)

btn1 = Button(window, text="View All",font=('mitra',10,'bold'), width=20,command=lambda:view_command(),bd='5',height='1',bg='#6ac2f9',activebackground='#d8cc0f',pady='3')
#btn1.grid(row=6, column=3)
btn1.place(x=384,y=140)

#================  Search Entry  ==============
def search_command():
    clear_list()
    books=backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    fill_list(books)

btn2 = Button(window, text="Search Entry", width=20,command=lambda:search_command(),font=('mitra',10,'bold'),bd='5',height='1',bg='#6ac2f9',activebackground='#d8cc0f',pady='3')
#btn2.grid(row=13, column=3)
btn2.place(x=384,y=230)

#================  Add Entry  ==============
def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

btn3 = Button(window, text="Add", width=8,command=add_command,font=('mitra',10,'bold'),bd='5',height='1',bg='#6ac2f9',activebackground='#d8cc0f',pady='3')
#btn3.grid(row=15, column=3)
btn3.place(x=480,y=185)

#================  Update Selected  ==============
def update_command():
    backend.update(select_book[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()

btn4 = Button(window, text="Update", width=20,command=update_command,font=('mitra',10,'bold'),bd='5',height='1',bg='#6ac2f9',activebackground='#d8cc0f',pady='3')
#btn4.grid(row=19, column=3)
btn4.place(x=384,y=275)


#================  Delet Selected  ==============
def delete_command():
    backend.delet(select_book[0])
    view_command()
btn5 = Button(window, text="Delete", width=8,command=delete_command,font=('mitra',10,'bold'),bd='5',height='1',bg='#6ac2f9',activebackground='#d8cc0f',pady='3')
#btn5.grid(row=19, column=3)
btn5.place(x=384,y=185)

#================  Close  ==============
def close_command():
    window.destroy()
btn6 = Button(window, text="Close", width=10,command=close_command,font=('mitra',12,'bold'),bd='5',height='1',bg='#bd0009',activebackground='#d8cc0f',pady='3',relief=GROOVE)
#btn6.grid(row=50, column=3)
btn6.place(x=20,y=300)



window.mainloop()
