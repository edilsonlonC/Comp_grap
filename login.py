from Tkinter import *

class frame:
    def __init__ (self):
        self.window=Tk()
        self.window.geometry('1000x1000')
        self.entrypass=Entry(self.window,show='*')
        self.entryuser=Entry(self.window)

    def show (self):
        self.window.mainloop()
    def get_user ():
        return self.entryuser.get()
    def insert_widget(self,widget):
        self.widget=widget
        self.widget.pack()
    def get_window (self):
        return self.window
    def get_user (self):
        #print self.entryuser.get()
        return self.entryuser.get()
    def show_user (self):
        self.entryuser.pack()
    def show_pass (self):
        self.entrypass.pack()
win=frame()


label1=Label(win.get_window(),text="user")
label2=Label(win.get_window(),text='password')
button=Button(win.get_window(),text='LOGIN',command=win.get_user)
win.insert_widget(label1)
win.show_user()
#win.insert_widget(entryuser)
win.insert_widget(label2)
win.show_pass()
#win.insert_widget(entrypass)
win.insert_widget(button)
win.show()
user=win.get_user()
print user
