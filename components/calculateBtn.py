import ttkbootstrap as ttk
from tkinter.filedialog import askdirectory
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import threading
import os

from classes.Process import Process


class CalculateBtn(ttk.Button):
  def __init__(self, parent, 
               text="Calcular índices", 
               style="success.TButton"):
    super().__init__(parent, text=text, style=style, command= self.on_click)
    self.pack(expand=True, fill="x", padx=10, pady=10)
    
    
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
  
  def output(self):
    out = askdirectory()
    if out is None: return
    return out
  
  def on_click(self):
    try:
      self.thread.cancel()
    except:
      pass
    self.thread = threading.Thread(target=self.calculate)
    self.thread.start()
    
  def calculate(self):
    if self.validate() is False: return
    output_path = self.output()
    if output_path is None: return
    file_path = self.master.select_file()
    console = self.master.log_text
    progress = self.master.progress
    
    indices = self.master.indices()
    
    console.clear()
    console.write("Cargando imagen...")
    progress.config(mode = "indeterminate", length=100, value=0)
    progress.start()
    
    process = Process(file_path).load_image()
    
    progress.stop()
    progress.config(mode = "determinate", maximum = process.shape()[0], value = 0)
    console.write("Calculando índices...")
    
    process.ram_process(indices, progress)
    saved_folder = process.save(output_path, indices)
    console.write("Índices calculados ✅ \n")
    console.write(f"Guardando resultados en {saved_folder}")
  
  