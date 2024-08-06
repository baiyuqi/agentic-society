
from tkinter import *
from tkinter import ttk
from pandastable import Table
import pandas as pd
from tkinter import scrolledtext
from asociety.generator.persona_generator import *

class EvaluationPanel:
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
        self.plot_empty()

    def ana(self):
            
        from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
        NavigationToolbar2Tk) 
        from asociety.personality.personality_analysis import  compute,get_personas_ana
 
        mdata = get_personas_ana()

        titles = ['openness' ,'conscientiousness' ,'extraversion', 'agreeableness', 'neuroticism','']

        for i in range(0, 5):
            x, y,yvals = compute(mdata[0],mdata[i + 1])


            row = int(i / 3)
            col = i % 3
            self.axs[row, col].cla()
            #axs[row, col].set_ylim([0, 100])
            self.axs[row, col].plot(x, y, '*')
            self.axs[row, col].plot(x,yvals,'r')
            self.axs[row, col].set(xlabel='age', ylabel='score')
            self.axs[row, col].set_title(titles[i])
        self.canvas.draw()

    def plot_empty(self):
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        import matplotlib.pyplot as plt
        titles = ['openness' ,'conscientiousness' ,'extraversion', 'agreeableness', 'neuroticism','']
        self.fig, self.axs = plt.subplots(2, 3)
     
        self.axs[1,2].set_axis_off()    
        for i, ax in enumerate(self.axs.flat):
           
            ax.set_title(titles[i])
        self.fig.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.top_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)



    def setData(self, item, updateTree):

        pass


            