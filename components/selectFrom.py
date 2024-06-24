import tkinter as tk
from tkinter.filedialog import askopenfilename
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SelectFrom(ttk.Frame):
  def __init__(self, parent, 
               placeholder = "No hay archivos seleccionados.",
               type = "file",
               title = "Seleccionar archivo",
               ):
    
    super().__init__(parent, padding=10)
    self.pack(fill=ttk.BOTH, expand=True)
    self.title = title
    self.path = None
    self.create_widgets(placeholder)
  
  def create_widgets(self, placeholder):
    self.title_label = ttk.Label(self, text=self.title)
    self.title_label.grid(row=0, column=0, columnspan=2, sticky=EW)
    
    self.path_entry = ttk.Entry(self, width=50)
    self.path_entry.insert(0, placeholder)
    self.path_entry.configure(state="readonly")
    self.path_entry.grid(row=1, column=0, sticky=EW)
    
    self.select_button = ttk.Button(self, 
                                    text="Seleccionar", 
                                    padding=5,
                                    command=self.select_from,
                                    style="primary.TButton")
    self.select_button.grid(row=1, column=1, sticky=EW, padx=(5,0))
    
  def __call__(self):
    return self.path
  
  def select_from(self):
    file_path = askopenfilename(title=self.title)
    if file_path == "" or file_path is None: return
    
    self.path_entry.configure(state="normal")
    self.path_entry.delete(0, tk.END)
    self.path_entry.insert(0, file_path)
    self.path_entry.configure(state="readonly")
    
    self.path = self.path_entry.get()