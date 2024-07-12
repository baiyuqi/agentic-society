
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
        top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=1)
        inner_panedwindow.add(bottom_frame, weight=1)

        # Create a scrolled text widget
        self.text_widget = scrolledtext.ScrolledText(top_frame, wrap=WORD, bg='#1E1E1E', fg='#DADADA', 
                                                     insertbackground='#DADADA', font=('Helvetica', 14),
                                                     selectbackground='#5A5A5A', selectforeground='#FFFFFF', 
                                                     relief=FLAT, padx=10, pady=10)

        self.text_widget.pack(expand=True, fill=BOTH)

        # Add some sample text
        sample_text = """Welcome to Agentic Society!
        """
        self.text_widget.insert(END, sample_text)


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
        col_clicked = self.table.get_col_clicked(event)
        if row_clicked is not None and col_clicked is not None:
            # 处理点击事件
            print(f"Clicked row: {row_clicked}, column: {col_clicked}")
            print(f"Row data: {self.table.model.df.iloc[row_clicked]}")
           
            self.text_widget.delete(1.0, END)
            self.text_widget.insert(END, self.table.model.df.iloc[row_clicked][col_clicked])
