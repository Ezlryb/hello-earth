from tkinter import *
from tkinter import messagebox
from os import *


class GUI:
    def __init__(self, parent):
        
        self.data_list = []

        

        

        #******************************************************************************************

        self.collect_data_frame = Frame(parent)

        self.collection_title_label = Label(self.collect_data_frame, text='Collecting Person Data')
        self.collection_title_label.grid(column=0, row=0)

        self.collection_show_all_button = Button(self.collect_data_frame, text='Show All', command=self.display_data)
        self.collection_show_all_button.grid(column=1, row=0)

        self.collection_first_name_label = Label(self.collect_data_frame, text='First Name: ')
        self.collection_first_name_label.grid(column=0, row=1)

        self.collection_first_name_variable = StringVar()
        self.collection_first_name_entry = Entry(self.collect_data_frame, textvariable=self.collection_first_name_variable)
        self.collection_first_name_entry.grid(column=1, row=1)

        self.collection_age_label = Label(self.collect_data_frame, text='Age: ')
        self.collection_age_label.grid(column=0, row=2)

        self.collection_age_variable = StringVar()
        self.collection_age_entry = Entry(self.collect_data_frame, textvariable=self.collection_age_variable)
        self.collection_age_entry.grid(column=1, row=2)

        self.collection_mobile_boolean_label = Label(self.collect_data_frame, text='Do you have a mobile phone?')
        self.collection_mobile_boolean_label.grid(column=0, row=3)


        self.collection_mobile_boolean_radio_button_frame = Frame(self.collect_data_frame)

        self.collection_mobile_boolean_variable = StringVar()
        self.collection_mobile_boolean_variable.set("Unknown") # it's not really a boolean value if it's got 3 values, is it?

        self.collection_mobile_boolean_radio_button_true = Radiobutton(self.collection_mobile_boolean_radio_button_frame, variable=self.collection_mobile_boolean_variable, value=True, text='Yes')
        self.collection_mobile_boolean_radio_button_true.grid(column=0,row=0)

        self.collection_mobile_boolean_raidio_button_false = Radiobutton(self.collection_mobile_boolean_radio_button_frame, variable=self.collection_mobile_boolean_variable, value=False, text='No')
        self.collection_mobile_boolean_raidio_button_false.grid(column=0, row=1)

        self.collection_mobile_boolean_radio_button_frame.grid(column=1, row=3)


        self.collection_enter_data_button = Button(self.collect_data_frame, text='Enter Data')
        self.collection_enter_data_button.grid(column=0, row=4, columnspan=2)


        self.collect_data_frame.pack()

        #******************************************************************************************

        self.display_data_frame = Frame(parent)

        self.display_title_label = Label(self.display_data_frame, text='Displaying Person Data')
        self.display_title_label.grid(column=0, row=0)

        self.display_show_all_button = Button(self.display_data_frame, text='Add New Person', command=self.collect_data)
        self.display_show_all_button.grid(column=1, row=0)

        self.display_first_name_discription_label = Label(self.display_data_frame, text='First Name: ')
        self.display_first_name_discription_label.grid(column=0, row=1)

        self.display_first_name_label = Label(self.display_data_frame, text='Unkown')
        self.display_first_name_label.grid(column=1, row=1)


        self.display_age_discription_label = Label(self.display_data_frame, text='Age: ')
        self.display_age_discription_label.grid(column=0, row=2)

        self.display_age_label = Label(self.display_data_frame, text='Unkown')
        self.display_age_label.grid(column=1, row=2)

        self.display_phone_boolean_label = Label(self.display_data_frame, text="Unknown may have a mobile phone")
        self.display_phone_boolean_label.grid(column=0, row=3, columnspan=2)

        self.display_previous_button = Button(self.display_data_frame, text='Previous')
        self.display_previous_button.grid(column=0, row=4)

        self.display_next_button = Button(self.display_data_frame, text='Next')
        self.display_next_button.grid(column=1, row=4)
        
        


    def display_data(self):
        self.collect_data_frame.pack_forget()
        self.display_data_frame.pack()

    def collect_data(self):
        self.display_data_frame.pack_forget()
        self.collect_data_frame.pack()


if __name__ == '__main__':
    root = Tk()
    window = GUI(root)
    root.mainloop()