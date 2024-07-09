from tkinter import *
import pyqrcode 
import png
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("QR Code Generator")
root.geometry('500x500')
root.configure(bg='#ffa700')

def generate_qr():
    #Filedialog
    input_path = filedialog.asksaveasfilename(title = "Save Image as ", filetype = (("PNG File", ".png"), ("All Files", "*.*")))

    if input_path:
        if input_path.endswith(".png"):
           #Create QR Code from entry box
            get_code = pyqrcode.create(entry_texts.get())
            #Save as PNG File
            get_code.png(input_path, scale=5)
        else:
            #add that .png to the end of the file name 
            input_path = f'{input_path}.png'
            
            #Create QR Code from entry box
            get_code = pyqrcode.create(entry_texts.get())
            
            #Save as PNG File
            get_code.png(input_path, scale=5)
        
        #Put QR Code on screen 
        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))
        
        #Add image to the label
        my_label.config(image = get_image)
        
        #Delete Entry box
        entry_texts.delete(0, END)
        
        #Flash up a finished message
        entry_texts.insert(0, "Finished!")
        

def clear_all():
    entry_texts.delete(0,END)
    my_label.config(image = '')

frame = Frame(root, bg = '#ffa700')
frame.pack(expand=True)


entry_texts  =  Entry(frame, font = ("Verdana", 18))
entry_texts.pack(pady = 20)

button1= Button(frame, text = "Create QR Code", command = generate_qr, font = ("Verdana", 10))
button1.pack(pady=20)

button2 = Button(frame, text= "Clear", command = clear_all, font = ("Verdana", 10))
button2.pack()

my_label = Label(frame, text = '')
my_label.pack(pady=20)

root.mainloop()