import customtkinter as ctk
from settings import *
from tkinter import filedialog, Canvas

class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_fun):
        super().__init__(master=parent)

        # Configure the frame grid
        self.grid(column=0, columnspan=2, row=0, sticky='nsew') 
        self.import_func = import_fun

        ctk.CTkButton(self,
                      text= 'Open image',
                      fg_color= PURPLE,
                      hover_color= LIGHT_PURPLE,
                      command= self.open_dialog).pack(expand = True)
        

    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_func(path)

class ImageOutput(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(master= parent, background = BACKGROUND_COLOR, bd = 0, highlightthickness = 0, relief = 'ridge')
        self.grid(row= 0, column= 1, sticky= 'nsew', pady = 10, padx = 10)
        self.bind('<Configure>', resize_image)

class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, function):
        super().__init__(master= parent,
                         text= 'X',
                         text_color= WHITE,
                         fg_color= 'transparent',
                         width= 40,
                         height= 40,
                         hover_color= CLOSE_RED,
                         command= function)
        self.place(relx = 0.99, rely = 0.01, anchor = 'ne')

