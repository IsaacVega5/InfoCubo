import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import IntVar

class IndicesSelect(ttk.LabelFrame):
  def __init__(self, parent):
    super().__init__(parent, padding=10)
    self.pack(fill=ttk.BOTH, expand=True, padx=10, pady=0)
    self.config(text=" Índices a calcular ")
    self.ndvi = IntVar(value=1)
    self.pri = IntVar(value=1)
    self.savi = IntVar(value=1)
    self.mcari = IntVar(value=1)
    self.wbi = IntVar(value=1)
    self.rdvi = IntVar(value=1)
    self.evi = IntVar(value=1)
    self.ari_2 = IntVar(value=1)
    self.cri_2 = IntVar(value=1)
    self.create_widgets()
    
  def __call__(self):
    indices = {
      'ndvi': self.ndvi.get(),
      'pri': self.pri.get(),
      'savi': self.savi.get(),
      'mcari': self.mcari.get(),
      'wbi': self.wbi.get(),
      'rdvi': self.rdvi.get(),
      'evi': self.evi.get(),
      'ari_2': self.ari_2.get(),
      'cri_2': self.cri_2.get(),
    }
    return indices
  
  def create_widgets(self):
    width = 15
    self.ndvi_btn= ttk.Checkbutton(self, text="NDVI", 
                                   bootstyle = "success-round-toggle",
                                   variable=self.ndvi,
                                   width = width
                                   )
    self.ndvi_btn.grid(row=0, column=0, padx=5, pady=5)
    
    self.pri_btn= ttk.Checkbutton(self, text="PRI", 
                                  bootstyle = "success-round-toggle",
                                  variable=self.pri,
                                  width = width
                                  )
    self.pri_btn.grid(row=0, column=1, padx=5, pady=5)
    
    self.savi_btn= ttk.Checkbutton(self, text="SAVI", 
                                   bootstyle = "success-round-toggle",
                                   variable=self.savi,
                                   width = width
                                   )
    self.savi_btn.grid(row=0, column=2, padx=5, pady=5)
    
    self.mcari_btn= ttk.Checkbutton(self, text="MCARI", 
                                    bootstyle = "success-round-toggle",
                                    variable=self.mcari,
                                    width = width
                                    )
    self.mcari_btn.grid(row=1, column=0, padx=5, pady=5)
    
    self.wbi_btn= ttk.Checkbutton(self, text="WBI", 
                                  bootstyle = "success-round-toggle",
                                  variable=self.wbi,
                                  width = width
                                  )
    self.wbi_btn.grid(row=1, column=1, padx=5, pady=5)
    
    self.rdvi_btn= ttk.Checkbutton(self, text="RDVI", 
                                   bootstyle = "success-round-toggle",
                                   variable=self.rdvi,
                                   width = width
                                   )
    self.rdvi_btn.grid(row=1, column=2, padx=5, pady=5)
    
    self.evi_btn= ttk.Checkbutton(self, text="EVI", 
                                  bootstyle = "success-round-toggle",
                                  variable=self.evi,
                                  width = width
                                  )
    self.evi_btn.grid(row=2, column=0, padx=5, pady=5)
    
    self.ari_2_btn= ttk.Checkbutton(self, text="ARI2", 
                                    bootstyle = "success-round-toggle",
                                    variable=self.ari_2,
                                    width = width
                                    )
    self.ari_2_btn.grid(row=2, column=1, padx=5, pady=5)
    
    self.cri_2_btn= ttk.Checkbutton(self, text="CRI2", 
                                    bootstyle = "success-round-toggle",
                                    variable=self.cri_2,
                                    width = width
                                    )
    self.cri_2_btn.grid(row=2, column=2, padx=5, pady=5)