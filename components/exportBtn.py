import ttkbootstrap as ttk
from tkinter.filedialog import askdirectory
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import threading
import time

from classes.Process import Process

class ExportBtn(ttk.Button):
  def __init__(self, parent, 
               text="Calcular índices", 
               style="success.TButton",
               action = 'calculate'):
    super().__init__(parent, text=text, style=style, command= self.on_click)
    self.action = action
    
  def validate(self):
    file_path = self.master.select_file()
    min, max = self.master.process_nb.bandas()
    if file_path is None:
      Messagebox.show_error(
        parent=self.master.master, 
        message="No se ha seleccionado ninguna imagen",
        buttons=["Aceptar:primary"]
      )
      return False
    
    if self.action == 'export' and min > max or min < 0 or min > 272 or max < 0 or max > 272: 
      Messagebox.show_error(
        parent=self.master.master, 
        message="Rango de bandas inválido",
        buttons=["Aceptar:primary"]
      )
      return False
    return True
  
  def output(self):
    out = askdirectory()
    if out is None or out == "": return
    return out
  
  def on_click(self):
    if self.validate() is False: return
    try:
      self.thread.cancel()
    except:
      pass
    self.thread = threading.Thread(target=self.to_export)
    self.thread.start()
  
  def to_export(self):
    
    filepath = self.master.select_file()
    output_path = self.output()
    if output_path is None: return
    
    if self.action == 'calculate': self.calculate(filepath, output_path)
    elif self.action == 'export': self.export_channels(filepath, output_path)
  
  def export_channels(self,filepath, output_path):
    min, max = self.master.process_nb.bandas()
    console = self.master.log_text
    init_time = time.time()
    
    console.clear()
    console.write("Exportando bandas...")
    
    img = Process(filepath)
    progress = self.master.progress
    progress.config(mode = "determinate", maximum = img.shape()[2], value = 0)
    
    path = img.export_channels(output_path, channels=(min, max), bar = progress)
    finish_time = time.time()
    
    console.write(f"Bandas exportadas en {round(finish_time - init_time, 2)}seg. \n")
    console.write(f"Resultados guardados en:\n{path}")
  
  def calculate(self, filepath, output_path):
    console = self.master.log_text
    progress = self.master.progress
    process_method = self.master.processSelect()
    indices = self.master.process_nb.indices()
    init_time = time.time()
    
    console.clear()
    console.write("Cargando imagen...")
    progress.config(mode = "indeterminate", length=100, value=0)
    progress.start()
    
    process = Process(filepath)
    if process_method == 0:
      process.load_image()
    
    progress.stop()
    progress.config(mode = "determinate", maximum = process.shape()[0], value = 0)
    console.write("Calculando índices...")
    
    if process_method == 0:
      process.ram_process(indices, progress)
    elif process_method == 1:
      process.direct_process(indices, progress)
    elif process_method == 2:
      process.no_iterative_process(indices)
      progress.step(process.shape()[0])
    
    saved_folder = process.save(output_path, indices)
    
    finish_time = time.time()
    console.write(f"Índices calculados en {round(finish_time - init_time, 2)}seg. \n")
    console.write(f"Resultados guardados en:\n{saved_folder}")
    
  
  