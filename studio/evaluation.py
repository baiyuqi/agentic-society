
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



        
        self.submit_button = ttk.Button(bottom_frame, text="BHPS", command=self.bhps)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.submit_button = ttk.Button(bottom_frame, text="GSOEP", command=self.gsoep)
        self.submit_button.grid(row=1, column=2, columnspan=2, pady=10)
        self.submit_button = ttk.Button(bottom_frame, text="LLM", command=self.llm)
        self.submit_button.grid(row=1, column=4, columnspan=2, pady=10)
        self.submit_button = ttk.Button(bottom_frame, text="similarity", command=self.differences)
        self.submit_button.grid(row=1, column=6, columnspan=2, pady=10)
        self.table = Table(top_frame, showtoolbar=True, showstatusbar=True)
        self.table.model.df = self.table.model.df.head(0)
        self.table.show()


    def bhps(self):
        df = pd.read_csv('data/cross_section/age_mean_BHPS.csv')
        self.table.model.df = df
        self.table.redraw()
    def gsoep(self):
        df = pd.read_csv('data/cross_section/age_mean_GSOEP.csv')
        self.table.model.df = df
        self.table.redraw()
    def llm(self):
        df = pd.read_csv('data/cross_section/llm_glm4.csv')
        self.table.model.df = df
        self.table.redraw()
    def differences(self):
        df = pd.read_csv('data/cross_section/distances.csv')
        self.table.model.df = df
        self.table.redraw()


    def setData(self, item, updateTree):

        pass


            