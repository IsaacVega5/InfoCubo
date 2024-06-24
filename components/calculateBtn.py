import ttkbootstrap as ttk
from tkinter.filedialog import askdirectory
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import threading
import os
from PIL import Image
from spectral import get_rgb
import spectral.io.envi as envi
import numpy as np
import math

from utils import remove_name_from_path, get_name_from_path

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
    if hasattr(self, 'thread') and self.thread.is_alive():
      self.thread.cancel()
    self.thread = threading.Thread(target=self.calculate)
    self.thread.start()
    
  def calculate(self):
    if self.validate() is False: return
    output_path = self.output()
    if output_path is None: return
    file_path = self.master.select_file()
    console = self.master.log_text
    progress = self.master.progress
    
    console.clear()
    console.write("Cargando imagen...")
    progress.config(mode = "indeterminate", length=100, value=0)
    progress.start()
    hdr_file = remove_name_from_path(file_path) + get_name_from_path(file_path) + ".hdr"
    raw_img = envi.open(hdr_file, file_path)
    raw_data = np.array(raw_img.load())
    del hdr_file, raw_img
    
    ndvi_img = np.zeros((raw_data.shape[0], raw_data.shape[1]))
    pri_img = np.zeros((raw_data.shape[0], raw_data.shape[1]))
    savi_img = np.zeros((raw_data.shape[0], raw_data.shape[1]))
    mcari_img = np.zeros((raw_data.shape[0], raw_data.shape[1]))
    wbi_img = np.zeros((raw_data.shape[0], raw_data.shape[1]))
    rdvi_img = np.zeros((raw_data.shape[0], raw_data.shape[1]))
    evi_img = np.zeros((raw_data.shape[0], raw_data.shape[1]))
    ari_2_img = np.zeros((raw_data.shape[0], raw_data.shape[1]))
    cri_2_img = np.zeros((raw_data.shape[0], raw_data.shape[1]))
    
    progress.stop()
    progress.config(mode = "determinate", maximum = raw_data.shape[0], value = 0)
    console.write("Calculando índices...")
    for i in range(raw_data.shape[0]):
      for j in range(raw_data.shape[1]):
        # Bandas
        r_450 = raw_data[i][j][23]
        r_550 = raw_data[i][j][68]
        r_570 = raw_data[i][j][77]
        r_670 = raw_data[i][j][122]
        r_700 = raw_data[i][j][135]
        r_840 = raw_data[i][j][199]
        r_900 = raw_data[i][j][226]
        r_950 = raw_data[i][j][248]
        
        ndvi = (r_840 - r_670) / (r_840 + r_670)
        pri = (r_550 - r_570) / (r_550 + r_570)
        savi = ((r_840 - r_670) / (r_840 + r_670 + 0.5)) * (1 + 0.5)
        mcari = ((r_700 - r_670) - (0.2 * (r_700 - r_550))) * (r_700 / r_670)
        wbi = r_900 / r_950
        rdvi = (r_840 - r_670) / math.sqrt(r_840 + r_670)
        evi = 2.5 * ( (r_840 - r_670) / r_840 + 6 * r_670 - 7.5 * r_450 + 1)
        ari_2 = r_840 * ((1 / r_550) - ( 1 / r_700))
        cri_2 = (1 / r_550) - (1 / r_700)
        
        ndvi_img[i][j] = ndvi
        pri_img[i][j] = pri
        savi_img[i][j] = savi
        mcari_img[i][j] = mcari
        wbi_img[i][j] = wbi
        rdvi_img[i][j] = rdvi
        evi_img[i][j] = evi
        ari_2_img[i][j] = ari_2
        cri_2_img[i][j] = cri_2
      progress.step(1)

    folder = output_path + "/results_" + get_name_from_path(file_path)
    if not os.path.exists(folder):
      os.makedirs(folder)
    
    ndvi_img = Image.fromarray(ndvi_img)
    ndvi_img.save(folder + "/" + get_name_from_path(file_path) + "_ndvi.tif")
    
    pri_img = Image.fromarray(pri_img)
    pri_img.save(folder + "/" + get_name_from_path(file_path) + "_pri.tif")
    
    savi_img = Image.fromarray(savi_img)
    savi_img.save(folder + "/" + get_name_from_path(file_path) + "_savi.tif")
    
    mcari_img = Image.fromarray(mcari_img)
    mcari_img.save(folder + "/" + get_name_from_path(file_path) + "_mcari.tif")
    
    wbi_img = Image.fromarray(wbi_img)
    wbi_img.save(folder + "/" + get_name_from_path(file_path) + "_wbi.tif")
    
    rdvi_img = Image.fromarray(rdvi_img)
    rdvi_img.save(folder + "/" + get_name_from_path(file_path) + "_rdvi.tif")
    
    evi_img = Image.fromarray(evi_img)
    evi_img.save(folder + "/" + get_name_from_path(file_path) + "_evi.tif")
    
    ari_2 = Image.fromarray(ari_2_img)
    ari_2.save(folder + "/" + get_name_from_path(file_path) + "_ari_2.tif")
    
    cri_2 = Image.fromarray(cri_2_img)
    cri_2.save(folder + "/" + get_name_from_path(file_path) + "_cri_2.tif")
    
    console.write("Índices calculados ✅\n" + str(folder + "/" + get_name_from_path(file_path) +"/"))
    return