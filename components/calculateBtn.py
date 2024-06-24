import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

class CalculateBtn(ttk.Button):
  def __init__(self, parent, 
               text="Calcular índices", 
               style="success.TButton"):
    super().__init__(parent, text=text, style=style, command=self.calculate)
    self.pack(expand=True, fill="x", padx=10, pady=10)
    
  def calculate(self):
    if self.validate() is False: return
    file_path = self.master.select_file()
    print(file_path)
    
  def validate(self):
    file_path = self.master.select_file()
    if file_path is None:
      Messagebox.show_error(
        parent=self.master, 
        message="No se ha seleccionado ninguna imagen",
        buttons=["Aceptar:primary"]
      )
      return False
    return True
    