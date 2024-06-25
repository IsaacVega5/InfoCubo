import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from constants import PROCESS_METHODS

class ProcessSelector(ttk.LabelFrame):
  def __init__(self, parent):
    super().__init__(parent, padding=10)
    self.pack(fill=ttk.BOTH, expand=True, padx=10, pady=10)
    self.config(text=" Método de procesamiento ")
    self.process_method = 0
    self.create_widgets()
  
  def __call__(self):
    return self.process_method
  
  def create_widgets(self):
    self.label = ttk.Label(self, text="Seleccione el método de procesamiento:")
    self.label.pack(side=ttk.LEFT, padx=5, pady=5)
    values = PROCESS_METHODS
    self.selector = ttk.Menubutton(self,
                                   bootstyle="primary",
                                   text=values[0],
                                   width=10
                                  )
    self.selector.pack(side=ttk.RIGHT, padx=5, pady=5)
    
    self.menu = ttk.Menu(self.selector)
    self.selector["menu"] = self.menu
    for x in range(len(values)):
      self.menu.add_cascade(label=values[x], command= lambda x=x: self.on_option(x))

  def on_option(self, index):
    self.selector.configure(text=PROCESS_METHODS[index])
    self.process_method = index