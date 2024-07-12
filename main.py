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
                                       placeholder="Ruta a la imagen")
    
    self.indices = comp.IndicesSelect(self)
    self.processSelect = comp.ProcessSelector(self)
    
    self.btn_calc = comp.CalculateBtn(self)
    self.export_btn = ttk.Button(self, text="Exportar índices", style="primary.TButton", command= self.export)
    self.export_btn.pack(expand=True, fill="x", padx=10, pady=10)
    
    self.log_text = comp.LogConsole(self)
    
    self.progress = ttk.Progressbar(self, style="success.Horizontal.TProgressbar")
    self.progress.config(length=100, value=0)
    self.progress.pack(expand=True, fill="x", padx=10, pady=(0,10))
  
  def export(self):
    filepath = self.select_file()
    from classes.Process import Process
    img = Process(filepath)
    from tkinter.filedialog import askdirectory
    output_path = askdirectory()
    if output_path is None: return
    img.export_channels(output_path)
    
    
if __name__ == "__main__":
  app = Main(root)
  app.mainloop()

