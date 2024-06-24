import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import components as comp


root = ttk.Window( title="InfoCubo", iconphoto = './assets/cube.png', themename="infocubo")
root.iconphoto = './assets/cube.png'


class Main(ttk.Frame):
  def __init__(self, parent):
    super().__init__(parent, padding=10)
    self.pack(fill=ttk.BOTH, expand=True)
    self.create_widgets()
    
    root.resizable(False, False)

  def create_widgets(self):
    self.header = comp.Header(self)
    
    
    self.separator = ttk.Separator(self, orient=HORIZONTAL)
    self.separator.pack(expand=True, fill="x", padx=10, pady=10)
    
    self.select_file = comp.SelectFrom(self, 
                                       title="Seleccionar imagen", 
                                       placeholder="c:/ruta/a/imagen")
    
    self.btn_calc = ttk.Button(self, text="Calcular índices", style="success.TButton")
    self.btn_calc.pack(expand=True, fill="x", padx=10, pady=10)

if __name__ == "__main__":
  app = Main(root)
  app.mainloop()
  
