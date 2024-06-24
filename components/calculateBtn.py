import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class CalculateBtn(ttk.Button):
  def __init__(self, parent, 
               text="Calcular índices", 
               style="success.TButton",
               command=None
               ):
    super().__init__(parent, text=text, style=style, command=command)
    self.pack(expand=True, fill="x", padx=10, pady=10)