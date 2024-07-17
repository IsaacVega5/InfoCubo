import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk, Image

class Header(ttk.Frame):
  def __init__(self, parent):
    super().__init__(parent, padding=10)
    self.create_widgets() 
    
  def create_widgets(self):
    logo = ImageTk.PhotoImage(Image.open("./assets/cube.png").resize((50, 50)))
    self.logo_label = ttk.Label(self, image=logo, compound="left")
    self.logo_label.image = logo
    self.logo_label.grid(row=0, column=0)
    
    self.title = ttk.Label(self, text="InfoCubo", font=("Helvetica", 16))
    self.title.grid(row=0, column=1)
    