
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
        top_frame = self.top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=1)
        inner_panedwindow.add(bottom_frame, weight=1)


        self.table = Table(bottom_frame, showtoolbar=True, showstatusbar=True)
        self.table.show()
        self.table.bind("<ButtonRelease-1>", self.on_row_click)
        
        from asociety.repository.database import engine

        

        df = pd.read_sql_query("select * from personality", engine)
        self.table.model.df = df
        self.table.redraw()
 
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
            self.plot(result=per)

    def plot(self, result):
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        import matplotlib.pyplot as plt
        
        fig, axs = plt.subplots(3, 2)
        for i in range(0, 5):
            


            row = int(i / 2)
            col = i % 2
            from asociety.personality.personality_quiz import PersonalityResult
            pr = PersonalityResult(result=result)
            data = pr.E
            #axs[row, col].set_ylim([0, 100])
            axs[row, col].barh(data.keys(), data.values())
           
   
        axs[2,1].set_axis_off()    
        for ax in axs.flat:
            ax.set(xlabel='age', ylabel='score')
        fig.tight_layout()
        plt.show()
        return fig

