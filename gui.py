from doctest import master
import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button

window = Tk()

class HealthMonitor:

    def __init__(self):
        
        # ROW 0
        

        #Name frame
        self.name_frame = Frame(master=window, width=200, height=50)
        self.name_frame.grid(row=0, column=0, padx=5, pady=5)
        self.name_label = Label(master=self.name_frame, text="Name", width=25, height=5, fg="black", bg="blue")
        self.name_label.pack()
        self.name_entry = Entry(master=self.name_frame, width=20)
        self.name_entry.pack()
        

        #Age frame
        self.age_frame = Frame(master=window, width=100, height=50)
        self.age_frame.grid(row=1, column=0, padx=5, pady=5)
        self.age_label = Label(master=self.age_frame, text="Age", width=25, height=5, fg="black", bg="blue")
        self.age_label.pack()
        self.age_entry = Entry(master=self.age_frame, width=10)
        self.age_entry.pack()

        #Gender frame
        self.gender_frame = Frame(master=window, width=100, height=50)
        self.gender_frame.grid(row=1, column=1, padx=5, pady=5)
        self.gender_label = Label(master=self.gender_frame, text="Gender", width=25, height=5, fg="black", bg="blue")
        self.gender_label.pack()
        self.gender_entry = Entry(master=self.gender_frame, width=10)
        self.gender_entry.pack()


        #Display frame
        self.display_frame = Frame(master=window, width=100, height=200)
        self.display_frame.grid(row=3, column=0, padx=5, pady=5)
        self.display_label = Label(master=self.display_frame, text='', width=25, height=5, fg="black", bg="blue")
        self.display_label.pack()
        

        # ROW 1

        #Heart Rate frame
        self.hr_frame = Frame(master=window, width=100, height=50)
        self.hr_frame.grid(row=0, column=2, padx=5, pady=5)
        self.hr_label = Label(master=self.hr_frame, text="hr", width=25, height=5, fg="black", bg="blue")
        self.hr_label.pack()
        self.hr_entry = Entry(master=self.hr_frame, width=10)
        self.hr_entry.pack()

        #Blood Pressure frame
        self.bp_frame = Frame(master=window, width=100, height=50)
        self.bp_frame.grid(row=1, column=2, padx=5, pady=5)
        self.bp_label = Label(master=self.bp_frame, text="bp", width=25, height=5, fg="black", bg="blue")
        self.bp_label.pack()
        self.bp_entry = Entry(master=self.bp_frame, width=10)
        self.bp_entry.pack()

        #Temperature frame
        self.temp_frame = Frame(master=window, width=100, height=50)
        self.temp_frame.grid(row=2, column=2, padx=5, pady=5)
        self.temp_label = Label(master=self.temp_frame, text="temp", width=25, height=5, fg="black", bg="blue")
        self.temp_label.pack()
        self.temp_entry = Entry(master=self.temp_frame, width=10)
        self.temp_entry.pack()


        #Button frame
        self.button_frame = Frame(master=window, width=100, height=50)
        self.button_frame.grid(row=3, column=2, padx=5, pady=5)
        self.button_button = Button(master=self.button_frame, text="Check", width=25, height=5, command=self.check_health)
        self.button_button.pack()

    #Check user vitals
    def check_health(self):
        display_text = ''

        if (self.hr_entry.get() == '' or self.bp_entry.get() == '' or self.temp_entry.get() == ''):
            self.display_label["text"] = 'Please enter HR, BP\n and Temp details'
            return
        if (int(self.hr_entry.get()) >= 100 or int(self.hr_entry.get()) <= 40):
            display_text += 'Warning HR unsafe! \nHealthy range 40 < HR < 100 \n'
        
        if (int(self.bp_entry.get()) >= 120 or int(self.bp_entry.get()) <= 60):
            display_text += 'Warning BP unsafe! \nHealthy range 60 < BP < 120 \n'
        
        if (float(self.temp_entry.get()) >= 37 or float(self.temp_entry.get()) <= 36):
            display_text += 'Warning T unsafe! \nHealthy range 36 < T < 37 \n'

        if display_text == '':
            display_text = 'Vitals in safe range'
        
        self.display_label["text"] = display_text

def main():
    #Construct GUI
    HealthMonitor()

    #Run event loop
    window.mainloop()

if __name__ == '__main__':
    main()