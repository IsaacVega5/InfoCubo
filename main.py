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
    self.header.grid(row=0, column=0, sticky="ew")
    
    self.separator = ttk.Separator(self, orient=HORIZONTAL)
    self.separator.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
    
    self.select_file = comp.SelectFrom(self, 
                                       title="Seleccionar imagen", 
                                       placeholder="Ruta a la imagen")
    self.select_file.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
    
    self.process_nb = comp.ExportNotebook(self, action=self.on_change)
    self.process_nb.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
    
    self.processSelect = comp.ProcessSelector(self)
    self.processSelect.grid(row=4, column=0, sticky="ew", padx=10, pady=10)
    
    self.render_btn(0)
    
    self.log_text = comp.LogConsole(self)
    self.log_text.grid(row=6, column=0, sticky="ew", padx=10, pady=(10,0))
    
    self.progress = ttk.Progressbar(self, style="success.Horizontal.TProgressbar")
    self.progress.config(length=100, value=0)
    self.progress.grid(row=7, column=0, sticky="ew", padx=10, pady=(0,10))
  
  def render_btn (self, tab):
    if tab == 0:
      self.btn_out = comp.ExportBtn(self, action='calculate')
    elif tab == 1:
      self.btn_out = comp.ExportBtn(self, text="Exportar bandas", action='export')
    
    self.btn_out.grid(row=5, column=0, sticky="ew", padx=10, pady=10)
  
  def on_change(self, event):
    current_tab = self.process_nb.index("current")
    self.render_btn(current_tab)
    
  
if __name__ == "__main__":
  app = Main(root)
  app.mainloop()

