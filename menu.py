import customtkinter as ctk
from settings import *
from panels import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent, pos_vars, color_vars, effect_vars, export_image):
        super().__init__(master= parent,
                         segmented_button_selected_hover_color= LIGHT_PURPLE,
                         segmented_button_unselected_color= PURPLE,
                         segmented_button_unselected_hover_color= LIGHT_PURPLE,
                         segmented_button_selected_color= LIGHT_PURPLE)
        self.grid(row = 0, column = 0, sticky = 'nsew', pady = 10, padx = 10)

        #Tabs
        self.add('Position')
        self.add('Color')
        self.add('Effects')
        self.add('Export')

        #Widgets
        PositionFrame(self.tab('Position'), pos_vars)
        ColorFrame(self.tab('Color'), color_vars)
        EffectFrame(self.tab('Effects'), effect_vars)
        ExportFrame(self.tab('Export'), export_image)

class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(master= parent, fg_color= 'transparent')
        self.pack(expand = True, fill = 'both')

        SliderPanel(self, 'Rotation', pos_vars['rotate'], 0, 360)
        SliderPanel(self, 'Zoom', pos_vars['zoom'], 0, 200)
        Segmentedpanel(self, 'Invert', pos_vars['flip'], FLIP_OPTIONS)
        RevertButton(self,
                     (pos_vars['rotate'], ROTATE_DEFAULT),
                     (pos_vars['zoom'], ZOOM_DEFAULT),
                     (pos_vars['flip'], FLIP_OPTIONS[0]))

class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent, color_var):
        super().__init__(master= parent, fg_color= 'transparent')
        self.pack(expand = True, fill = 'both')

        SwitchPanel(self, (color_var['grayscale'],'B/W'), (color_var['invert'],'Invert'))
        SliderPanel(self, 'Brightness', color_var['brightness'], 0, 5)
        SliderPanel(self, 'Vibrance', color_var['vibrance'], 0, 5)
        RevertButton(self,
                     (color_var['brightness'], BRIGHTNESS_DEFAULT),
                     (color_var['grayscale'], GRAYSCALE_DEFAULT),
                     (color_var['invert'], INVERT_DEFAULT),
                     (color_var['vibrance'], VIBRANCE_DEFAULT))

class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent, effect_var):
        super().__init__(master= parent, fg_color= 'transparent')
        self.pack(expand = True, fill = 'both')

        DropDownPanel(self, effect_var['effect'], EFFECT_OPTIONS)
        SliderPanel(self, 'Blur', effect_var['blur'], 0, 30)
        SliderPanel(self, 'Contrast', effect_var['contrast'], 0, 10)
        RevertButton(self,
                     (effect_var['effect'], EFFECT_OPTIONS[0]),
                     (effect_var['blur'], BLUR_DEFAULT),
                     (effect_var['contrast'], CONTRAST_DEFAULT))
        
class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent, export_image):
        super().__init__(master= parent, fg_color= 'transparent')
        self.pack(expand = True, fill = 'both')

        #Data
        self.name_string = ctk.StringVar()
        self.file_string = ctk.StringVar(value= 'jpg')
        self.path_string = ctk.StringVar()

        #Widgets
        FileNamePanel(self, self.name_string, self.file_string)
        FilePathPanel(self, self.path_string)
        SaveButton(self, export_image, self.name_string, self.file_string, self.path_string)
