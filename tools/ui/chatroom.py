
from tkinter import *
from tkinter import ttk
from pandastable import Table, TableModel
from asociety.repository.database import engine
import pandas as pd
from tkinter import scrolledtext
from asociety.generator.persona_generator import *
from asociety.repository.database import engine
class Chatroom:
    def __init__(self, parent) -> None:
        self.main = inner_panedwindow = ttk.PanedWindow(parent, orient=VERTICAL)
        inner_panedwindow.pack(fill=BOTH, expand=True)

        # Create two frames to be added to the inner PanedWindow
        top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN)
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN)

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
        sample_text = """Welcome to Chatroom!
        """
        self.text_widget.insert(END, sample_text)

    def setData(self, item):
        if(item == 'persona'):
            self.table.model.df = pd.read_sql_query("select * from persona limit 100", engine)
           
        elif(item == 'question'):
            self.table.model.df = pd.read_sql_query("select * from question limit 100", engine)
           
        elif(item == 'persona group'):
            self.table.model.df = pd.read_sql_query("select * from persona_group limit 100", engine)
           
        elif(item == 'question group'):
            self.table.model.df = pd.read_sql_query("select * from question_group limit 100", engine)
            
        elif(item == 'experimentlist'):
            self.table.model.df = pd.read_sql_query("select * from experiment limit 100", engine)
           
        self.table.redraw()
    def message(self, msg):
            self.text_widget.insert(END, msg)
