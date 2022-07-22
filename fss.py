# python-3.8.2 

import mss
import tkinter as tk
import tkinter.ttk as ttk

from threading import Thread
from time import time

class UI(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
            
        self.minsize(16384, 16384)
        self.frames = [] # last 60 captured frames
        self.capturing = True
            
        

        # Thread(target=self.capture_loop).start()
    
    def capture_loop(self):
        with mss.mss() as screen: 
            
            while self.capturing:
                img = screen.grab(screen.monitors[0])
                
                self.frames.append((img, time()))
                self.frames = self.frames[-60:]

    def screenshot(self):
        with mss.mss() as screen: 
            img = screen.grab(screen.monitors[0])

        self.frames.append(img)
        

                
if __name__ == "__main__":
    ui = UI()
    ui.mainloop()