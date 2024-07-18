from typing import Any
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ChannelSelector(ttk.Frame):
  def __init__(self, parent, action = None):
    super().__init__(parent)
    self.action = action
    self.create_widgets()
  
  def __call__(self):
    min = int(self.min_entry.get())
    max = int(self.max_entry.get())
    
    return (min, max)
  
  def create_widgets(self):
    self.min_label = ttk.Label(self, text="Rango de bandas:")
    self.min_label.pack(side=ttk.LEFT, padx=5, pady=5)
    self.min_entry = ttk.Entry(self, validate="focusout", validatecommand=(self.master.register(self.validate), '%P'))
    self.min_entry.pack(side=ttk.LEFT, padx=5, pady=5, fill=ttk.X, expand=True)
    self.label = ttk.Label(self, text="-", justify=CENTER, anchor="center")
    self.label.pack(side=ttk.LEFT, padx=5, pady=5)
    self.max_entry = ttk.Entry(self, validate="focusout", validatecommand=(self.master.register(self.validate), '%P'))
    self.max_entry.pack(side=ttk.LEFT, padx=5, pady=5, fill=ttk.X, expand=True)
    self.min_entry.insert(0, 0)
    self.max_entry.insert(0, 272)
    
  def validate(self, value):
    if value == "": return True
    if value.isnumeric() is False:
      return False
    if int(self.min_entry.get()) > int(self.max_entry.get()):
      return False
    return True