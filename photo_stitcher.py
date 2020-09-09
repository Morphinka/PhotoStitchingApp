import tkinter as Tkinter
from tkinter import filedialog
from pathlib import Path
import cv2
import numpy as np

listfile = []

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):

        #button = Tkinter.Button(self,text=u"directory",command=self.OnButtonClick)
        #here is the third button to run the script, the command isn't right
        button2 = Tkinter.Button(self,text=u"Run script",command=self.OnButtonClick2)
        #button.pack(side='bottom',padx=15,pady=15) 
        button2.pack(side='bottom',padx=15,pady=15) 

    #def OnButtonClick(self):
        #x = filedialog.askdirectory(title='Please select data directory')
        #print(x)   
        
    def OnButtonClick2(self):
        x = filedialog.askdirectory(title='Please select data directory')
        image = []
        entries = Path(x)
        x0 = []
        y0 = []
        images = []
        
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
            
        big_image = np.concatenate(rows_array)
           
        #print(big_image)

        main_picture = cv2.imwrite('25_sztuk/output.jpg', big_image)
        
        
    
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()  
      

