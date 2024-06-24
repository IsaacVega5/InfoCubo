import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

class LogConsole(ttk.Frame):
  def __init__(self, parent):
    super().__init__(parent)
    self.pack(fill=ttk.BOTH, expand=True, padx=10, pady=(10,0))
    self.create_widgets()
  
  def create_widgets(self):
    self.console = ScrolledText(self, state="disabled", font=("Consolas", 10), height=5, vbar=False, width=50, padding=0)
    self.console.pack(expand=True, fill="both")
    
  def write(self, text):
    self.console.text.configure(state="normal")
    if len(self.console.text.get("1.0", END)) > 1:
      self.console.insert(END, "\n")
    self.console.insert(END, text)
    self.console.see(END)
    self.console.text.configure(state="disabled")
    
  def clear(self):
    self.console.delete("1.0", END)