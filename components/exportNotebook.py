import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from components.indicesSelect import IndicesSelect

class ExportNotebook(ttk.Notebook):
  def __init__(self, parent, action = None):
    super().__init__(parent)
    self.action = action
    self.create_widgets()
    
    
  def create_widgets(self):
    self.indices = IndicesSelect(self)
    self.bandas = ttk.Label(self, text="Exportar bandas")
    self.add(self.indices, text="Indices")
    self.add(self.bandas, text="Bandas")
    
    if self.action is not None: self.bind("<<NotebookTabChanged>>", self.action)
  
  