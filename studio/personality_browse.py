
from tkinter import *
from tkinter import ttk
from pandastable import Table
import pandas as pd
from tkinter import scrolledtext
from asociety.generator.persona_generator import *

class PersonalityBrowser:
    def __init__(self, parent) -> None:
        self.main = inner_panedwindow = ttk.PanedWindow(parent, orient=VERTICAL)
        inner_panedwindow.pack(fill=BOTH, expand=True)

        # Create two frames to be added to the inner PanedWindow
        top_frame = self.top_frame = ttk.Frame(inner_panedwindow, width=400, height=500, relief=SUNKEN,style='TFrame')
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=2)
        inner_panedwindow.add(bottom_frame, weight=1)


        self.table = Table(bottom_frame, showtoolbar=True, showstatusbar=True)
        self.table.show()
        self.table.bind("<ButtonRelease-1>", self.on_row_click)
        
        from asociety.repository.database import engine

        

        df = pd.read_sql_query("select * from personality", engine)
        self.table.model.df = df
        self.table.redraw()
        self.plot_empty()
    def setData(self, item, updateTree):

        self.table.redraw()
    def on_row_click(self, event):
        # 获取点击的位置
        row_clicked = self.table.get_row_clicked(event)

        if row_clicked is not None:
            pjson = self.table.model.df.iloc[row_clicked]['personality_json']
            from asociety.personality.ipipneo.quiz import plot_results_by
            import json
            per = json.loads(pjson)
            self.plot_fill(result=per)

    def plot_empty(self):
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        import matplotlib.pyplot as plt
        
        self.fig, self.axs = plt.subplots(3, 2)
     
        self.axs[2,1].set_axis_off()    
        for ax in self.axs.flat:
            ax.set(xlabel='age', ylabel='score')
        self.fig.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.top_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def plot_fill(self, result):
        colors = ['orange','green','magenta','red','blue']
  
        from asociety.personality.personality_quiz import PersonalityResult
        pr = PersonalityResult(result=result)
        all = pr.all
        for i in range(0, 5):
            


            row = int(i / 2)
            col = i % 2
            
            data = all[i]
            #axs[row, col].set_ylim([0, 100])
            self.axs[row, col].cla()
            self.axs[row, col].barh(data.keys(), data.values(), color=colors[i])
           
   


        self.canvas.draw()

