import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from components.indicesSelect import IndicesSelect
from components.channelsSelector import ChannelSelector

class ExportNotebook(ttk.Notebook):
  def __init__(self, parent, action = None):
    super().__init__(parent)
    self.action = action
    self.create_widgets()
    
    
  def create_widgets(self):
    self.indices = IndicesSelect(self)
    self.bandas = ChannelSelector(self)
    self.add(self.indices, text="Indices")
    self.add(self.bandas, text="Bandas")
    
    if self.action is not None: self.bind("<<NotebookTabChanged>>", self.action)
  
  