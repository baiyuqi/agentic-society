
from tkinter import *
from tkinter import ttk
from pandastable import Table, TableModel
from asociety.repository.database import engine
import pandas as pd
from tkinter import scrolledtext
from asociety.generator.persona_generator import *
from asociety.repository.database import engine
class DataManager:
    def __init__(self, parent) -> None:
        self.main = inner_panedwindow = ttk.PanedWindow(parent, orient=VERTICAL)
        inner_panedwindow.pack(fill=BOTH, expand=True)

        # Create two frames to be added to the inner PanedWindow
        top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=1)
        inner_panedwindow.add(bottom_frame, weight=1)


        toppane = inner_panedwindow = ttk.PanedWindow(top_frame, orient=HORIZONTAL)
        left_top_frame = ttk.Frame(toppane, width=400, height=200, relief=SUNKEN,style='TFrame')
        right_top_frame = ttk.Frame(toppane, width=400, height=200, relief=SUNKEN,style='TFrame')

        # Add the frames to the inner PanedWindow
        toppane.add(left_top_frame, weight=1)
        toppane.add(right_top_frame, weight=1)
        toppane.pack(fill=BOTH, expand=True)  # Pack the top_panedwindow
        # Create a scrolled text widget
        self.text_widget = scrolledtext.ScrolledText(right_top_frame, wrap=WORD, bg='#1E1E1E', fg='#DADADA', 
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



        submit_button = ttk.Button(left_top_frame, text="delete selected" , command=self.delete_selected,style='TButton')
        submit_button.grid(row=1, column=0, columnspan=1, pady=10)
    def delete_selected(self):
        from tkinter import messagebox
        response = messagebox.askokcancel("Confirmation", "Do you want to delete it?")
        if not response:
            return

      
        row = self.table.getSelectedRowData()
        index = self.table.getSelectedRow()
        id = self.table.model.df.loc[index]['id']

        from sqlalchemy.orm import Session
        from sqlalchemy import text
        with Session(engine) as session:
            ps = session.execute(text('delete from ' + self.table_name + " where id = " + str(id)))
            session.commit()
        df = self.table.model.df.drop(index)
        df.reset_index(drop=True, inplace=True)

        self.table.updateModel(TableModel(df))
        self.table.redraw()
        self.updateTree()
    def setData(self, item, updateTree):
        self.appkey = item
        self.updateTree = updateTree
        if(item == 'persona'):
            self.table.model.df = pd.read_sql_query("select * from persona limit 100", engine)
           
        elif(item == 'question'):
            self.table.model.df = pd.read_sql_query("select * from question limit 100", engine)
           
        elif(item == 'persona group'):
            self.table.model.df = pd.read_sql_query("select * from persona_group limit 100", engine)
            self.table_name = 'persona_group'
        elif(item == 'question group'):
            self.table.model.df = pd.read_sql_query("select * from question_group limit 100", engine)
            self.table_name = 'question_group'
        elif(item == 'experimentlist'):
            self.table.model.df = pd.read_sql_query("select * from experiment limit 100", engine)
            self.table_name = 'experiment'
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
     