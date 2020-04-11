import tkinter as tk
import tkinter.font
from tkinter import ttk, messagebox
import requests
from add_student_popup import AddStudentPopup
from add_teacher_popup import AddTeacherPopup
from add_staff_popup import AddStaffPopup
from delete_student_popup import DeleteStudentPopup
from delete_staff_popup import DeleteStaffPopup
from delete_teacher_popup import DeleteTeacherPopup
from update_student_popup import UpdateStudentPopup
from edit_student_popup import EditStudentPopup
from edit_teacher_popup import EditTeacherPopup
from edit_staff_popup import EditStaffPopup
from json import *

class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        # Left frame, column 1
        left_frame = tk.Frame(master=self)
        left_frame.grid(row=1, column=1)

        # Right frame (info text, column 2)
        right_frame = tk.Frame(master=self)
        right_frame.grid(row=1, column=2)

        # Listbox for people
        tk.Label(left_frame, text="All People").grid(row=1, column=1, columnspan=3)
        self._people_list = tk.Listbox(left_frame, width=20)
        self._people_list.grid(row=2, column=1, columnspan=3)
        # Call on select
        self._people_list.bind("<<ListboxSelect>>", self._update_textbox)

        # Left side buttons
        ttk.Button(left_frame, text="Add Student", command=self._add_student).grid(row=3, column=1)
        ttk.Button(left_frame, text="Add Teacher", command=self._add_teacher).grid(row=4, column=1)
        ttk.Button(left_frame, text="Add Staff", command=self._add_staff).grid(row=5, column=1)

        # Right side buttons
        ttk.Button(right_frame, text="Delete Student", command=self._delete_student).grid(row=3, column=1)
        ttk.Button(right_frame, text="Delete Teacher", command=self._delete_teacher).grid(row=4, column=1)
        ttk.Button(right_frame, text="Delete Staff", command=self._delete_staff).grid(row=5, column=1)
        ttk.Button(right_frame, text="Edit Student", command=self._edit_student).grid(row=3, column=2)
        ttk.Button(right_frame, text="Edit Teacher", command=self._edit_teacher).grid(row=4, column=2)
        ttk.Button(right_frame, text="Edit Staff", command=self._edit_staff).grid(row=5, column=2)

        # Right frame widgets
        self._info_text = tk.Text(master=right_frame, height=10, width=40, font=("TkTextFont", 10))
        self._info_text.grid(row=1, column=1)
        self._info_text.tag_configure("bold", font=("TkTextFont", 10, "bold"))

        self._update_people_list()

    def _update_people_list(self):
        """ Update the List of People """
        r = requests.get("http://127.0.0.1:5000/school")
        self._people_list.delete(0, tk.END)
        for person in r.json():
            print(person[0])
            self._people_list.insert(tk.END, person[0]['id'])

    def _update_textbox(self, evt):
        """ Updates the info text box on the right, based on the current ID selected """

        # This is a list, so we take just the first item (could be multi select...)
        selected_values = self._people_list.curselection()
        selected_index = selected_values[0]
        student_id = self._people_list.get(selected_index)
        print(student_id)

        # Make a GET request
        r = requests.get("http://127.0.0.1:5000/school/student/" + str(student_id))

        # Clear the text box
        self._info_text.delete(1.0, tk.END)

        # Check the request status code
        if r.status_code != 200:
            self._info_text.insert(tk.END, "Error running the request!")

        #For every item (key, value) in the JSON response, display them:
        for key, value in r.json().items():
            self._info_text.insert(tk.END, f"{key.capitalize()}\t\t", "bold")
            self._info_text.insert(tk.END, f"{value}\n")

    def _add_student(self):
        """ Add Student Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddStudentPopup(self._popup_win, self._close_student_cb)

    def _close_student_cb(self):
        """ Close Add Student Popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _add_teacher(self):
        """ Add Student Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddTeacherPopup(self._popup_win, self._close_teacher_cb)

    def _close_teacher_cb(self):
        """ Close Add Student Popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _add_staff(self):
        """ Add Student Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddStaffPopup(self._popup_win, self._close_staff_cb)

    def _close_staff_cb(self):
        """ Close Add Student Popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _delete_student(self):
        """ Delete Person Popup """
        self._popup_win = tk.Toplevel()
        self._popup = DeleteStudentPopup(self._popup_win, self._close_delete_student)

    def _close_delete_student(self):
        """ Closes delete person popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _delete_staff(self):
        """ Delete Person Popup """
        self._popup_win = tk.Toplevel()
        self._popup = DeleteStaffPopup(self._popup_win, self._close_delete_student)

    def _close_delete_staff(self):
        """ Closes delete person popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _delete_teacher(self):
        """ Delete Person Popup """
        self._popup_win = tk.Toplevel()
        self._popup = DeleteTeacherPopup(self._popup_win, self._close_delete_teacher)

    def _close_delete_teacher(self):
        """ Closes delete person popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _update_student(self):
        """ Opens Update student popup """
        self._popup_win = tk.Toplevel()
        self._popup = UpdateStudentPopup(self._popup_win, self._close_update)

    def _close_update(self):
        """ Closes update popup """
        self._popup_win.destroy()
        self._update_people_list()

    def _edit_student(self):
        """ Opens Update student popup """
        person = self._info_text.get('4.0', 'end-0c')
        info = person.split()
        id = info[1]
        print(id)
        self._popup_win = tk.Toplevel()
        self._popup = EditStudentPopup(self._popup_win, self._close_edit, id)
        self._update_people_list()

    def _edit_staff(self):
        """ Opens Update student popup """
        person = self._info_text.get('4.0', 'end-0c')
        info = person.split()
        id = info[1]
        print(id)
        self._popup_win = tk.Toplevel()
        self._popup = EditStaffPopup(self._popup_win, self._close_edit, id)
        self._update_people_list()

    def _edit_teacher(self):
        """ Opens Update student popup """
        person = self._info_text.get('4.0', 'end-0c')
        info = person.split()
        id = info[1]
        print(info)
        print(id)
        self._popup_win = tk.Toplevel()
        self._popup = EditTeacherPopup(self._popup_win, self._close_edit, id)
        self._update_people_list()


    def _close_edit(self):
        """ Closes update popup """
        self._popup_win.destroy()
        self._update_people_list()



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    MainAppController(root).pack()
    root.mainloop()

