
from tkinter import *
from tkinter import ttk
from pandastable import Table
import pandas as pd
from tkinter import scrolledtext
from asociety.generator.persona_generator import *

class PersonalityAnalysis:
    def __init__(self, parent) -> None:
        self.main = inner_panedwindow = ttk.PanedWindow(parent, orient=VERTICAL)
        inner_panedwindow.pack(fill=BOTH, expand=True)

        # Create two frames to be added to the inner PanedWindow
        top_frame = self.top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=1)
        inner_panedwindow.add(bottom_frame, weight=1)



        
        self.submit_button = ttk.Button(bottom_frame, text="create", command=self.ana)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=10)

    def ana(self):
            
        from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
        NavigationToolbar2Tk) 
        from asociety.personality.personality_analysis import  get_personas_ana_figure
        fig = get_personas_ana_figure()




    def setData(self, item, updateTree):

        self.table.redraw()


            