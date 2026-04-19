"""This file creates a tkinter window for the collection of various people
data: their name, age and whether or not they have a mobile phone"""
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from os import *



class Person:
    """person object stores the variables first name, age and phone_status."""
    def __init__(self, first_name, age, phone_status):
        self.first_name = first_name
        self.age = age
        if phone_status == 1:
            self.phone_status = "does have a mobile phone"
        elif phone_status == 2:
            self.phone_status = "does not have a mobile phone"
        else:
            self.phone_status = "might have a mobile phone"


class GUI:
    """This class creates a graphical user interface window and handles all its 
    functionality."""
    def __init__(self, parent):
        """This function initialises the style used by the class, global 
        variables/lists used by the class, widgets displayed in the window."""
        s=ttk.Style()
        s.theme_use('default')
        s.configure('Custom.TFrame', background='#da70d6')
        s.configure('Custom.TLabel', background='#da70d6')
        self.people = []
        self.displayed_person_index = 0
        self.collect_data_frame = ttk.Frame(parent)
        self.collect_data_frame.columnconfigure(0, weight=1)
        self.collection_top_frame = ttk.Frame(self.collect_data_frame,
            style='Custom.TFrame')
        self.collection_title_label = ttk.Label(self.collection_top_frame,
            text='Collecting Person Data',
            style='Custom.TLabel')
        self.collection_title_label.grid(column=0, row=0, padx=10, pady=10)
        self.collection_show_all_button = ttk.Button(self.collection_top_frame,
                                                    text='Show All', command=self.display_data_frame_func)
        self.collection_show_all_button.grid(column=1, row=0, padx=10, pady=10)
        self.collection_top_frame.grid(column=0, row=0, columnspan=2, sticky='nsew')
        self.collection_first_name_label = ttk.Label(self.collect_data_frame, text='First Name:')
        self.collection_first_name_label.grid(column=0, row=1, padx=10, pady=10)
        self.collection_first_name_variable = StringVar()
        self.collection_first_name_entry = ttk.Entry(self.collect_data_frame, textvariable=self.collection_first_name_variable)
        self.collection_first_name_entry.grid(column=1, row=1, padx=10, pady=5)
        self.collection_age_label = ttk.Label(self.collect_data_frame, text='Age: ')
        self.collection_age_label.grid(column=0, row=2, padx=10, pady=10)
        self.collection_age_variable = StringVar()
        self.collection_age_entry = ttk.Entry(self.collect_data_frame, textvariable=self.collection_age_variable)
        self.collection_age_entry.grid(column=1, row=2, padx=10, pady=5)
        self.collection_mobile_status_label = ttk.Label(self.collect_data_frame, text='Do you have a mobile phone?')
        self.collection_mobile_status_label.grid(column=0, row=3, padx=10, pady=10)
        self.collection_mobile_status_radio_button_frame = ttk.Frame(self.collect_data_frame)
        self.collection_mobile_status_variable = IntVar()
        self.collection_mobile_status_radio_button_true = ttk.Radiobutton(self.collection_mobile_status_radio_button_frame, variable=self.collection_mobile_status_variable, value=1, text='Yes')
        self.collection_mobile_status_radio_button_true.grid(column=0,row=0, padx=10, pady=10)
        self.collection_mobile_status_raidio_button_false = ttk.Radiobutton(self.collection_mobile_status_radio_button_frame, variable=self.collection_mobile_status_variable, value=2, text='No')
        self.collection_mobile_status_raidio_button_false.grid(column=0, row=1, padx=10) 
        self.collection_mobile_status_radio_button_frame.grid(column=1, row=3, padx=10)
        self.collection_enter_data_button = ttk.Button(self.collect_data_frame, text='Enter Data', command=self.enter_data_func)
        self.collection_enter_data_button.grid(column=0, row=4, columnspan=2)
        self.collect_data_frame.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)
        self.display_data_frame = ttk.Frame(parent)
        self.display_data_frame.columnconfigure(0, weight=1)
        self.display_data_frame.columnconfigure(1, weight=1)
        self.display_top_frame = ttk.Frame(self.display_data_frame, style='Custom.TFrame')
        self.display_title_label = ttk.Label(self.display_top_frame, text='Displaying Person Data', style='Custom.TLabel')
        self.display_title_label.grid(column=0, row=0, padx=10, pady=10)
        self.display_show_all_button = ttk.Button(self.display_top_frame, text='Add New Person', command=self.collect_data_frame_func)
        self.display_show_all_button.grid(column=1, row=0, padx=10, pady=10)
        self.display_top_frame.grid(column=0, row=0, columnspan=2, sticky='nsew')
        self.display_first_name_discription_label = ttk.Label(self.display_data_frame, text='First Name: ')
        self.display_first_name_discription_label.grid(column=0, row=1, padx=10, pady=10)
        self.display_first_name_label = ttk.Label(self.display_data_frame, text='Unkown')
        self.display_first_name_label.grid(column=1, row=1, padx=10, pady=10)
        self.display_age_discription_label = ttk.Label(self.display_data_frame, text='Age: ')
        self.display_age_discription_label.grid(column=0, row=2, padx=10, pady=10)
        self.display_age_label = ttk.Label(self.display_data_frame, text='Unkown')
        self.display_age_label.grid(column=1, row=2, padx=10, pady=10)
        self.display_phone_status_label = ttk.Label(self.display_data_frame, text="Unknown may have a mobile phone")
        self.display_phone_status_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        self.display_previous_button = ttk.Button(self.display_data_frame, text='Previous', command=self.previous_func)
        self.display_previous_button.grid(column=0, row=4, padx=10, pady=10)
        self.display_next_button = ttk.Button(self.display_data_frame, text='Next', command=self.next_func)
        self.display_next_button.grid(column=1, row=4, padx=10, pady=10)

    def is_num(self, value):
        """This function inputs a value and returns true if it is an integer and false if not"""
        try:
            value = int(value)
            return True
        except ValueError:
            return False

    def display_data_frame_func(self):
        """This function hides the collection frame and shows the display frame"""
        if len(self.people) >= 1:
            self.display_person_func(self.displayed_person_index)
        self.collect_data_frame.grid_forget()
        self.display_data_frame.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

    def collect_data_frame_func(self):
        """This function shows the collection frame and hides the display frame"""
        self.display_data_frame.grid_forget()
        self.collect_data_frame.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

    def enter_data_func(self):
        """This function checks if the information the user has put into the entry widgets is 
        valid and if so creates a 'person' object which is added to the 'people' list"""
        if self.is_num(self.collection_age_variable.get()):
            if int(self.collection_age_variable.get()) <= 0:
                messagebox.showerror("Invalid Entry", "Please enter a positive number")
                self.collection_age_entry.delete(0,END)
            else:
                person = Person(self.collection_first_name_variable.get(),
                        self.collection_age_variable.get(),
                        self.collection_mobile_status_variable.get(),
                        )
                self.people.append(person)
                self.collection_first_name_entry.delete(0,END)
                self.collection_age_entry.delete(0,END)
                self.collection_mobile_status_variable.set(0)
                self.people[-1].print_data()
        else:
            messagebox.showerror("Invalid Entry", "Please enter a number")
            self.collection_age_entry.delete(0,END)

    def display_person_func(self, person_index):
        """This function inputs an integer and updates child widgets of the display frame to display 
        the information of a 'person' object in the 'people' list at the index of the 'poerson_index'"""
        if len(self.people) != 0:
            self.display_first_name_label.configure(text=self.people[person_index].first_name)
            self.display_age_label.configure(text=self.people[person_index].age)
            self.display_phone_status_label.configure(text=f'{self.people[person_index].first_name} {self.people[person_index].phone_status}')

    def next_func(self):
        """This function runs the 'display_person_func' function with the index of 
        the next 'person' object in the 'people' list"""
        self.displayed_person_index += 1
        if self.displayed_person_index >= len(self.people):
            self.displayed_person_index = 0
        self.display_person_func(self.displayed_person_index)
    
    def previous_func(self):
        """This function runs the 'display_person_func' function with the index of 
        the previous 'person' object in the 'people' list"""
        self.displayed_person_index -= 1
        if -self.displayed_person_index >= len(self.people) + 1:
            self.displayed_person_index = len(self.people) - 1
        self.display_person_func(self.displayed_person_index)


if __name__ == '__main__':
    root = Tk()
    window = GUI(root)
    root.geometry("480x240")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()