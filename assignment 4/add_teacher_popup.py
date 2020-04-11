import requests
import tkinter as tk
from tkinter import ttk, messagebox
import json


class AddTeacherPopup(tk.Frame):
    """ Popup Frame to Add a Student """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        ttk.Label(self, text="ID:").grid(row=1, column=1)
        self._id = ttk.Entry(self)
        self._id.grid(row=1, column=2)

        ttk.Label(self, text="First Name:").grid(row=2, column=1)
        self._fname = ttk.Entry(self)
        self._fname.grid(row=2, column=2)

        ttk.Label(self, text="Last Name:").grid(row=3, column=1)
        self._lname = ttk.Entry(self)
        self._lname.grid(row=3, column=2)

        ttk.Label(self, text="Age:").grid(row=4, column=1)
        self._age = ttk.Entry(self)
        self._age.grid(row=4, column=2)

        ttk.Label(self, text="Salary:").grid(row=5, column=1)
        self._salary = ttk.Entry(self)
        self._salary.grid(row=5, column=2)

        ttk.Label(self, text="Courses:").grid(row=6, column=1)
        self._courses = ttk.Entry(self)
        self._courses.grid(row=6, column=2)



        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=7, column=1)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=7, column=2)

    def _submit_cb(self):
        """ Submit the Add Student """

        data = {}
        data['id'] = int(self._id.get())
        data['fname'] = self._fname.get()
        data['lname'] = self._lname.get()
        data['age'] = int(self._age.get())
        data['salary'] = int(self._salary.get())
        data['courses'] = self._courses.get()

        self.add_teacher(data)

    def add_teacher(self, data):
        """Makes post request"""
        r = requests.post("http://127.0.0.1:5000/school/teacher", json=data)
        print(r.text)
        self._close_cb()
