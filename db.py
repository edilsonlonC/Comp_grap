import mysql.connector
from Tkinter import *

class frame :
    def __init__ (self):
        self.screen=Tk()
    def get_frame (self):
        return self.screen
    def start (self):
        self.screen.mainloop()
    def size (self,value):
        self.screen.geometry(value)


def create_widgets (Frame):
    message_name = Label(Frame.get_frame(),text='name')
    message_name.pack()
    slot_name = Entry(Frame.get_frame())
    slot_name.pack()
    message_lastname1 = Label(Frame.get_frame(),text='lastname1')
    slot_last_name1 = Entry(Frame.get_frame())
    message_lastname2 = Label(Frame.get_frame(),text='lastname2')
    slot_last_name2 = Entry(Frame.get_frame())


def main ():
    Frame=frame()
    create_widgets(Frame)
    Frame.size('300x400')
    Frame.start()

main()
