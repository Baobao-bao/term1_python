import requests
import tkinter as tk
from tkinter import ttk, messagebox
import json

class EditStudentPopup(tk.Frame):
    """ Popup Frame to Add a Student """

    def __init__(self, parent, close_callback, id):
        """ Constructor """

        self.id = id

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        ttk.Label(self, text="First Name:").grid(row=2, column=1)
        self._fname = ttk.Entry(self)
        self._fname.grid(row=2, column=2)

        ttk.Label(self, text="Last Name:").grid(row=3, column=1)
        self._lname = ttk.Entry(self)
        self._lname.grid(row=3, column=2)

        ttk.Label(self, text="Age:").grid(row=4, column=1)
        self._age = ttk.Entry(self)
        self._age.grid(row=4, column=2)

        ttk.Label(self, text="Courses:").grid(row=5, column=1)
        self._courses = ttk.Entry(self)
        self._courses.grid(row=5, column=2)

        ttk.Label(self, text="Tuition:").grid(row=6, column=1)
        self._tuition = ttk.Entry(self)
        self._tuition.grid(row=6, column=2)



        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=7, column=1)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=7, column=2)

    def _submit_cb(self):
        """ Submit the Add Student """

        data = {}
        data['id'] = int(self.id)
        data['fname'] = self._fname.get()
        data['lname'] = self._lname.get()
        data['age'] = int(self._age.get())
        data['tuition'] = int(self._tuition.get())
        data['courses'] = self._courses.get()

        self.update_student(data)

    def update_student(self, data):
        """Makes post request"""
        requests.put("http://127.0.0.1:5000/school/update_student/" + str(self.id), json=data)
        self._close_cb()
