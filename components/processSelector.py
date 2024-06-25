import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip

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
                                   text=values[0][0],
                                   width=10
                                  )
    self.selector.pack(side=ttk.RIGHT, padx=5, pady=5)
    
    self.menu = ttk.Menu(self.selector)
    self.selector["menu"] = self.menu
    for x in range(len(values)):
      option = self.menu.add_cascade(label=values[x][0], command= lambda x=x: self.on_option(x))
    self.tooltip = ToolTip(self.selector, text=values[0][1], bootstyle="light")

  def on_option(self, index):
    self.selector.configure(text=PROCESS_METHODS[index][0])
    self.process_method = index
    self.tooltip = ToolTip(self.selector, text=PROCESS_METHODS[index][1], bootstyle="light")
    