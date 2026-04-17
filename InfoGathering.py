from tkinter import *
from tkinter import messagebox
from os import *



class Person:
    def __init__(self, first_name, age, phone_status):
        self.first_name = first_name
        self.age = age
        
        if phone_status == 1:
            self.phone_status = "does have a mobile phone"
        elif phone_status == 2:
            self.phone_status = "does not have a mobile phone"
        else:
            self.phone_status = "might have a mobile phone"

    def print_data(self):
        print(self.first_name)
        print(self.age)
        print(self.phone_status)


class GUI:
    def __init__(self, parent):
        
        self.people = []
        self.displayed_person_index = 0


        #******************************************************************************************

        self.collect_data_frame = Frame(parent)

        self.collection_title_label = Label(self.collect_data_frame, text='Collecting Person Data')
        self.collection_title_label.grid(column=0, row=0)

        self.collection_show_all_button = Button(self.collect_data_frame, text='Show All', command=self.display_data_frame_func)
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

        self.collection_mobile_status_label = Label(self.collect_data_frame, text='Do you have a mobile phone?')
        self.collection_mobile_status_label.grid(column=0, row=3)


        self.collection_mobile_status_radio_button_frame = Frame(self.collect_data_frame)

        self.collection_mobile_status_variable = IntVar()

        self.collection_mobile_status_radio_button_true = Radiobutton(self.collection_mobile_status_radio_button_frame, variable=self.collection_mobile_status_variable, value=1, text='Yes')
        self.collection_mobile_status_radio_button_true.grid(column=0,row=0)

        self.collection_mobile_status_raidio_button_false = Radiobutton(self.collection_mobile_status_radio_button_frame, variable=self.collection_mobile_status_variable, value=2, text='No')
        self.collection_mobile_status_raidio_button_false.grid(column=0, row=1)

        self.collection_mobile_status_radio_button_frame.grid(column=1, row=3)


        self.collection_enter_data_button = Button(self.collect_data_frame, text='Enter Data', command=self.enter_data_func)
        self.collection_enter_data_button.grid(column=0, row=4, columnspan=2)


        self.collect_data_frame.pack()

        #******************************************************************************************

        self.display_data_frame = Frame(parent)

        self.display_title_label = Label(self.display_data_frame, text='Displaying Person Data')
        self.display_title_label.grid(column=0, row=0)

        self.display_show_all_button = Button(self.display_data_frame, text='Add New Person', command=self.collect_data_frame_func)
        self.display_show_all_button.grid(column=1, row=0)

        self.display_first_name_discription_label = Label(self.display_data_frame, text='First Name: ')
        self.display_first_name_discription_label.grid(column=0, row=1)

        self.display_first_name_label = Label(self.display_data_frame, text='Unkown')
        self.display_first_name_label.grid(column=1, row=1)


        self.display_age_discription_label = Label(self.display_data_frame, text='Age: ')
        self.display_age_discription_label.grid(column=0, row=2)

        self.display_age_label = Label(self.display_data_frame, text='Unkown')
        self.display_age_label.grid(column=1, row=2)

        self.display_phone_status_label = Label(self.display_data_frame, text="Unknown may have a mobile phone")
        self.display_phone_status_label.grid(column=0, row=3, columnspan=2)

        self.display_previous_button = Button(self.display_data_frame, text='Previous', command=self.previous_func)
        self.display_previous_button.grid(column=0, row=4)

        self.display_next_button = Button(self.display_data_frame, text='Next', command=self.next_func)
        self.display_next_button.grid(column=1, row=4)
        
        


    def display_data_frame_func(self):
        if len(self.people) >= 1:
            self.display_person_func(self.displayed_person_index)
        self.collect_data_frame.pack_forget()
        self.display_data_frame.pack()


    def collect_data_frame_func(self):
        self.display_data_frame.pack_forget()
        self.collect_data_frame.pack()


    def enter_data_func(self):
        person = Person(self.collection_first_name_variable.get(),
                        self.collection_age_variable.get(),
                        self.collection_mobile_status_variable.get(),
                        )
        self.people.append(person)
        self.collection_first_name_entry.delete(0,END)
        self.collection_age_entry.delete(0,END)
        self.collection_mobile_status_variable.set(0)
        self.people[-1].print_data()


    def display_person_func(self, person_index):
        print("Something")
        self.display_first_name_label.configure(text=self.people[person_index].first_name)
        self.display_age_label.configure(text=self.people[person_index].age)
        self.display_phone_status_label.configure(text=f'{self.people[person_index].first_name} {self.people[person_index].phone_status}')


    def next_func(self):
        self.displayed_person_index+=1
        if self.displayed_person_index > len(self.people) - 1:
            self.displayed_person_index -= len(self.people)
        self.display_person_func(self.displayed_person_index)
    

    def previous_func(self):
        self.displayed_person_index -=1
        if -self.displayed_person_index > len(self.people):
            self.displayed_person_index += len(self.people)
        self.display_person_func(self.displayed_person_index)

if __name__ == '__main__':
    root = Tk()
    window = GUI(root)
    root.mainloop()