import tkinter as Tkinter
from tkinter import filedialog
from pathlib import Path
import cv2
import numpy as np
from tkinter import messagebox, HORIZONTAL
from tkinter.ttk import Progressbar


listfile = []

class simpleapp_tk(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.initialize()
        self.progress = Progressbar(self, orient=HORIZONTAL,length=100,  mode='determinate')
        
        
    def initialize(self):
        button = Tkinter.Button(self,text=u"Run script",command=self.OnButtonClick)
        button.grid(row=0)
        
        
    def OnButtonClick(self):
        folder_selected = filedialog.askdirectory(title='Please select data directory')
        
        self.progress.grid(row=1)
        self.update()
        
        image = []
        entries = Path(folder_selected)
        x0 = []
        y0 = []
        images = []
        
        self.progress['value'] = 20
        self.update_idletasks()
        
        for entry in entries.iterdir():
            if (entry.name[-4:] == ".jpg" and entry.name != "output.jpg"):
                print(entry.name)
                i = entry.name[:-4]
                split = i.split("_")
                x = split[0]
                y = split[1]
                x = int(x)
                y = int(y)
                print(x, y)
                
                images.append((x, y, cv2.imread(str(entry.absolute()), -1)))
                
                x0.append(x) 
                y0.append(y)
                
        self.progress['value'] = 50
        self.update_idletasks()
                
        images.sort()
        
        x_max = max(x0)
        y_max = max(y0)
        rows_array = []
            
        for i in range(y_max):
            images_array = images[i*x_max:x_max+i*x_max]
            images_to_concatenate = []
            for x, y, image in images_array:
                images_to_concatenate.append(image)
            rows_array.append(np.concatenate(images_to_concatenate[:], axis=1))
            
        self.progress['value'] = 90
        self.update_idletasks()
            
        big_image = np.concatenate(rows_array)
        
        main_picture = cv2.imwrite(folder_selected + '/output.jpg', big_image)
        
        self.progress['value'] = 100
        self.update_idletasks()
        
        messagebox.showinfo("Information","Stitched photo is in the chosen directory ;)")
                
        self.destroy()
        
                      
if __name__ == "__main__":
    app = simpleapp_tk()
    app.title('my application')
    app.mainloop()  
      

