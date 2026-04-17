from tkinter import *
from tkinter import messagebox
from os import *


class GUI:
    def __init__(self, parent):
        

        self.title_label = Label(parent, text='Collecting Person Data')
        self.title_label.grid(column=0, row=0)

        self.switch_frame_button = Button(text='Show All')
        self.switch_frame_button.grid(column=1, row=0)


        self.collect_data_frame = Frame(parent)

        self.first_name_label = Label(self.collect_data_frame, text='First Name: ')
        self.first_name_label.grid(column=0, row=0)

        self.first_name_variable = StringVar()
        self.first_name_entry = Entry(self.collect_data_frame, textvariable=self.first_name_variable)
        self.first_name_entry.grid(column=1, row=0)

        self.age_label = Label(self.collect_data_frame, text='Age: ')
        self.age_label.grid(column=0, row=1)

        self.age_variable = StringVar()
        self.age_entry = Entry(self.collect_data_frame, textvariable=self.age_variable)
        self.age_entry.grid(column=1, row=1)

        self.mobile_boolean_label = Label(self.collect_data_frame, text='Do you have a mobile phone?')
        self.mobile_boolean_label.grid(column=0, row=2)


        self.mobile_boolean_radio_button_frame = Frame(self.collect_data_frame)

        self.mobile_boolean_variable = StringVar()
        self.mobile_boolean_variable.set("Unknown") # it's not really a boolean value if it's got 3 values, is it?

        self.mobile_boolean_radio_button_true = Radiobutton(self.mobile_boolean_radio_button_frame, variable=self.mobile_boolean_variable, value=True, text='Yes')
        self.mobile_boolean_radio_button_true.grid(column=0,row=0)

        self.mobile_boolean_raidio_button_false = Radiobutton(self.mobile_boolean_radio_button_frame, variable=self.mobile_boolean_variable, value=False, text='No')
        self.mobile_boolean_raidio_button_false.grid(column=0, row=1)

        self.mobile_boolean_radio_button_frame.grid(column=1, row=2)

        



        self.collect_data_frame.grid(column=0, row=1, columnspan=2)




if __name__ == '__main__':
    root = Tk()
    window = GUI(root)
    root.mainloop()