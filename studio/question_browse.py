
from tkinter import *
from tkinter import ttk
from pandastable import Table, TableModel
from asociety.repository.database import engine
import pandas as pd
from tkinter import scrolledtext
from asociety.generator.persona_generator import *
from asociety.repository.database import engine
class QuestionBrowser:
    def __init__(self, parent) -> None:
        self.main = inner_panedwindow = ttk.PanedWindow(parent, orient=VERTICAL)
        inner_panedwindow.pack(fill=BOTH, expand=True)

        # Create two frames to be added to the inner PanedWindow
        top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=1)
        inner_panedwindow.add(bottom_frame, weight=1)


        buttom_pane = inner_panedwindow = ttk.PanedWindow(bottom_frame, orient=HORIZONTAL)
        left_bottom_frame = ttk.Frame(buttom_pane, width=400, height=200, relief=SUNKEN,style='TFrame')
        right_bottom_frame = ttk.Frame(buttom_pane, width=400, height=200, relief=SUNKEN,style='TFrame')

        # Add the frames to the inner PanedWindow
        buttom_pane.add(left_bottom_frame, weight=1)
        buttom_pane.add(right_bottom_frame, weight=1)
        buttom_pane.pack(fill=BOTH, expand=True)  # Pack the top_panedwindow

        self.settable = Table(left_bottom_frame, showtoolbar=True, showstatusbar=True)
  
        self.settable.model.df = pd.read_sql_query("select * from question_set limit 100", engine)
        self.settable.show()
        self.settable.bind("<ButtonRelease-1>", self.on_select_set)


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


        self.table = Table(right_bottom_frame, showtoolbar=True, showstatusbar=True)
        self.table.model.df = self.table.model.df.head(0)
        self.table.model.df = pd.read_sql_query("select * from question limit 100", engine)

        self.table.show()
        self.table.bind("<ButtonRelease-1>", self.on_select_question)
    def setData(self, item, updateTree):
  
        pass
    def on_select_question(self, event):
        # 获取点击的位置
        row_clicked = self.table.get_row_clicked(event)
        col_clicked = self.table.get_col_clicked(event)
        if row_clicked is not None and col_clicked is not None:
            # 处理点击事件
            print(f"Clicked row: {row_clicked}, column: {col_clicked}")
            print(f"Row data: {self.table.model.df.iloc[row_clicked]}")
           
            self.text_widget.delete(1.0, END)
            self.text_widget.insert(END, self.table.model.df.iloc[row_clicked][col_clicked])
    def on_select_set(self, event):
        # 获取点击的位置
        row_clicked = self.table.get_row_clicked(event)
        col_clicked = self.table.get_col_clicked(event)
        if row_clicked is not None and col_clicked is not None:
            # 处理点击事件
            print(f"Clicked row: {row_clicked}, column: {col_clicked}")
            print(f"Row data: {self.table.model.df.iloc[row_clicked]}")
            set_name = self.settable.model.df.iloc[row_clicked]['name']
            self.table.model.df = pd.read_sql_query("select * from question where question_set = '" + set_name + "' limit 100", engine)
            self.table.redraw()
    def setExperiment(self, ename):
        
        from asociety.repository.database import engine
        from sqlalchemy.orm import Session
        from asociety.repository.experiment_rep import ExperimentEntity
        with Session(engine) as session:
            self.experiment = session.query(ExperimentEntity).filter(ExperimentEntity.name==ename).first()

            df = pd.read_sql_query("select * from question_answer where experiment_name = '" + ename + "'", engine)
            self.table.model.df = df
            self.table.redraw()
        self.name_var.set(self.experiment.name)
        self.desc_var.set(self.experiment.description)
     