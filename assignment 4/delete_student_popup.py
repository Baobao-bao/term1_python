import requests
import tkinter as tk
from tkinter import ttk, messagebox
import json

class DeleteStudentPopup(tk.Frame):
    """ Popup Frame to Add a Student """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        ttk.Label(self, text="ID Number").grid(row=1, column=1)
        self.id = ttk.Entry(self)
        self.id.grid(row=1, column=2)

        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=2, column=1)

    def _submit_cb(self):

        BASE_URL = "http://127.0.0.1:5000/school/student/"

        id = self.id.get()

        person = requests.get(f"http://127.0.0.1:5000/school/student/{id}")
        person_dict = json.loads(person.content.decode('utf-8'))
        if int(person_dict['id']) == int(id):
            print("Hello")
            messagebox.askyesno(title="Are you sure", message="Do you want to delete this person")
            requests.delete(BASE_URL + id + "/delete")
            messagebox.showinfo(title="Success", message="Person deleted")
            self._close_cb()
