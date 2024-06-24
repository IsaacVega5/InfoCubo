import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

class LogConsole(ttk.Frame):
  def __init__(self, parent):
    super().__init__(parent, padding=10)
    self.pack(fill=ttk.BOTH, expand=True)
    self.create_widgets()
  
  def create_widgets(self):
    self.console = ScrolledText(self, state="normal", font=("Consolas", 10), height=10, vbar=False, width=50)
    self.console.pack(expand=True, fill="both")
    
  
  def write(self, text):
    if len(self.console.text.get("1.0", END)) > 1:
      self.console.insert(END, "\n")
    self.console.insert(END, text)
    self.console.see(END)
    
  def clear(self):
    self.console.delete("1.0", END)