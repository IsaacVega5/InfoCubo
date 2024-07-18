from PIL import Image
from spectral import get_rgb
import spectral.io.envi as envi
import numpy as np
import math
import os

from utils import get_name_from_path, remove_name_from_path, format_number

from constants import BANDAS, CHANNELS_DIRECT

class Process:
  def __init__(self, file_path):
    self.file_path = file_path
    self.hdr_file = remove_name_from_path(file_path) + get_name_from_path(file_path) + ".hdr"
    self.raw_img = envi.open(self.hdr_file, self.file_path)
  
  def __call__(self):
    return self.raw_img
    
  def load_image(self):
    raw_data = np.array(self.raw_img.load())
    self.raw_data = raw_data
    return self
  
  def shape(self):
    shape = self.raw_img.shape
    return shape
  
  def set_indices (self, indices, shape):
    if indices['ndvi'] == 1:
      self.ndvi_img = np.zeros((shape[0], shape[1]))
    if indices['pri'] == 1:
      self.pri_img = np.zeros((shape[0], shape[1]))
    if indices['savi'] == 1:
      self.savi_img = np.zeros((shape[0], shape[1]))
    if indices['mcari'] == 1:
      self.mcari_img = np.zeros((shape[0], shape[1]))
    if indices['wbi'] == 1:
      self.wbi_img = np.zeros((shape[0], shape[1]))
    if indices['rdvi'] == 1:
      self.rdvi_img = np.zeros((shape[0], shape[1]))
    if indices['evi'] == 1:
      self.evi_img = np.zeros((shape[0], shape[1]))
    if indices['ari_2'] == 1:
      self.ari_2_img = np.zeros((shape[0], shape[1]))
    if indices['cri_2'] == 1:
      self.cri_2_img = np.zeros((shape[0], shape[1]))
  
  def ram_process (self, indices, bar = None):
    self.set_indices(indices, self.shape())
    
    for i in range(self.raw_data.shape[0]):
      for j in range(self.raw_data.shape[1]):
        # Bandas
        r_450 = self.raw_data[i][j][BANDAS['r_450']]
        r_550 = self.raw_data[i][j][BANDAS['r_550']]
        r_570 = self.raw_data[i][j][BANDAS['r_570']]
        r_670 = self.raw_data[i][j][BANDAS['r_670']]
        r_700 = self.raw_data[i][j][BANDAS['r_700']]
        r_840 = self.raw_data[i][j][BANDAS['r_840']]
        r_900 = self.raw_data[i][j][BANDAS['r_900']]
        r_950 = self.raw_data[i][j][BANDAS['r_950']]
        
        if indices['ndvi'] == 1:
          self.ndvi_img[i][j] = (r_840 - r_670) / (r_840 + r_670)

        if indices['pri'] == 1:
          self.pri_img[i][j] = (r_550 - r_570) / (r_550 + r_570)

        if indices['savi'] == 1:
          self.savi_img[i][j] = ((r_840 - r_670) / (r_840 + r_670 + 0.5)) * (1 + 0.5)

        if indices['mcari'] == 1:
          self.mcari_img[i][j] = ((r_700 - r_670) - (0.2 * (r_700 - r_550))) * (r_700 / r_670)

        if indices['wbi'] == 1:
          self.wbi_img[i][j] = r_900 / r_950 if r_950 != 0 else 0

        if indices['rdvi'] == 1:
          self.rdvi_img[i][j] = (r_840 - r_670) / math.sqrt(r_840 + r_670)

        if indices['evi'] == 1:
          self.evi_img[i][j] = 2.5 * ( (r_840 - r_670) / r_840 + 6 * r_670 - 7.5 * r_450 + 1)

        if indices['ari_2'] == 1:
          self.ari_2_img[i][j] = r_840 * ((1 / r_550) - ( 1 / r_700))
          
        if indices['cri_2'] == 1:
          self.cri_2_img[i][j] = (1 / r_550) - (1 / r_700)
        
      if bar is not None:
        bar.step(1)

  def save (self, output_path, indices):
    file_path = self.file_path
    folder = output_path + "/results_" + get_name_from_path(file_path)
    if not os.path.exists(folder):
      os.makedirs(folder)
    
    if indices['ndvi'] == 1:
      ndvi_img = Image.fromarray(self.ndvi_img)
      ndvi_img.save(folder + "/" + get_name_from_path(file_path) + "_ndvi.tif")
    
    if indices['pri'] == 1:
      pri_img = Image.fromarray(self.pri_img)
      pri_img.save(folder + "/" + get_name_from_path(file_path) + "_pri.tif")
    
    if indices['savi'] == 1:
      savi_img = Image.fromarray(self.savi_img)
      savi_img.save(folder + "/" + get_name_from_path(file_path) + "_savi.tif")
    
    if indices['mcari'] == 1:
      mcari_img = Image.fromarray(self.mcari_img)
      mcari_img.save(folder + "/" + get_name_from_path(file_path) + "_mcari.tif")
    
    if indices['wbi'] == 1:
      wbi_img = Image.fromarray(self.wbi_img)
      wbi_img.save(folder + "/" + get_name_from_path(file_path) + "_wbi.tif")
    
    if indices['rdvi'] == 1:
      rdvi_img = Image.fromarray(self.rdvi_img)
      rdvi_img.save(folder + "/" + get_name_from_path(file_path) + "_rdvi.tif")
    
    if indices['evi'] == 1:
      evi_img = Image.fromarray(self.evi_img)
      evi_img.save(folder + "/" + get_name_from_path(file_path) + "_evi.tif")
    
    if indices['ari_2'] == 1:
      ari_2 = Image.fromarray(self.ari_2_img)
      ari_2.save(folder + "/" + get_name_from_path(file_path) + "_ari_2.tif")
    
    if indices['cri_2'] == 1:
      cri_2 = Image.fromarray(self.cri_2_img)
      cri_2.save(folder + "/" + get_name_from_path(file_path) + "_cri_2.tif")
    
    return folder
  
  def context_process (self, indices, bar = None):
    self.set_indices(indices, self.shape())
    
    for i in range(self.shape()[0]):
      for j in range(self.shape()[1]):
        # Bandas
        r_450 = self.raw_img[i,j][BANDAS['r_450']]
        r_550 = self.raw_img[i,j][BANDAS['r_550']]
        r_570 = self.raw_img[i,j][BANDAS['r_570']]
        r_670 = self.raw_img[i,j][BANDAS['r_670']]
        r_700 = self.raw_img[i,j][BANDAS['r_700']]
        r_840 = self.raw_img[i,j][BANDAS['r_840']]
        r_900 = self.raw_img[i,j][BANDAS['r_900']]
        r_950 = self.raw_img[i,j][BANDAS['r_950']]
        
        if indices['ndvi'] == 1:
          self.ndvi_img[i][j] = (r_840 - r_670) / (r_840 + r_670)

        if indices['pri'] == 1:
          self.pri_img[i][j] = (r_550 - r_570) / (r_550 + r_570)

        if indices['savi'] == 1:
          self.savi_img[i][j] = ((r_840 - r_670) / (r_840 + r_670 + 0.5)) * (1 + 0.5)

        if indices['mcari'] == 1:
          self.mcari_img[i][j] = ((r_700 - r_670) - (0.2 * (r_700 - r_550))) * (r_700 / r_670)

        if indices['wbi'] == 1:
          self.wbi_img[i][j] = r_900 / r_950 if r_950 != 0 else 0

        if indices['rdvi'] == 1:
          self.rdvi_img[i][j] = (r_840 - r_670) / math.sqrt(r_840 + r_670)

        if indices['evi'] == 1:
          self.evi_img[i][j] = 2.5 * ( (r_840 - r_670) / r_840 + 6 * r_670 - 7.5 * r_450 + 1)

        if indices['ari_2'] == 1:
          self.ari_2_img[i][j] = r_840 * ((1 / r_550) - ( 1 / r_700))
          
        if indices['cri_2'] == 1:
          self.cri_2_img[i][j] = (1 / r_550) - (1 / r_700)
          
      if bar is not None:
        bar.step(1)  

  def export_channels(self, folder, channels= (0, 273), bar = None):  
    folder = folder + "/channels" 
    if not os.path.exists(folder):
      os.makedirs(folder)
    
    for i in range(self.shape()[2]):
      if i < channels[0] or i > channels[1]: continue
      banda = self.raw_img.read_band(i)
      banda = Image.fromarray(banda)
      banda.save(f'{folder}/{format_number(i)}_{CHANNELS_DIRECT[i]}.tif')
      
      if bar is not None:
        bar.step(1)
    
    return folder