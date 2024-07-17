import ttkbootstrap as ttk
from tkinter.filedialog import askdirectory
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import threading
import time

from classes.Process import Process


class CalculateBtn(ttk.Button):
  def __init__(self, parent, 
               text="Calcular índices", 
               style="success.TButton"):
    super().__init__(parent, text=text, style=style, command= self.on_click)
    
  def validate(self):
    file_path = self.master.select_file()
    if file_path is None:
      Messagebox.show_error(
        parent=self.master.master, 
        message="No se ha seleccionado ninguna imagen",
        buttons=["Aceptar:primary"]
      )
      return False
    return True
  
  def output(self):
    out = askdirectory()
    if out is None: return
    return out
  
  def on_click(self):
    if self.validate() is False: return
    try:
      self.thread.cancel()
    except:
      pass
    self.thread = threading.Thread(target=self.calculate)
    self.thread.start()
    
  def calculate(self):
    output_path = self.output()
    if output_path is None: return
    file_path = self.master.select_file()
    console = self.master.log_text
    progress = self.master.progress
    process_method = self.master.processSelect()
    indices = self.master.process_nb.indices()
    init_time = time.time()
    
    console.clear()
    console.write("Cargando imagen...")
    progress.config(mode = "indeterminate", length=100, value=0)
    progress.start()
    
    process = Process(file_path)
    if process_method == 0:
      process.load_image()
    
    progress.stop()
    progress.config(mode = "determinate", maximum = process.shape()[0], value = 0)
    console.write("Calculando índices...")
    
    if process_method == 0:
      process.ram_process(indices, progress)
    else:
      process.context_process(indices, progress)
    
    saved_folder = process.save(output_path, indices)
    
    finish_time = time.time()
    console.write(f"Índices calculados en {round(finish_time - init_time, 2)}seg. \n")
    console.write(f"Guardando resultados en:\n{saved_folder}")
    
  
  