
from tkinter import *
from tkinter import ttk
from pandastable import Table, TableModel
from asociety.repository.database import engine
import pandas as pd
from tkinter import messagebox
from asociety.experiments.experiment_generator import QuestionSelector
class RandomSelect:
    def __init__(self, root, mode, callable,set):
        self.setData = callable
        self.questionSelector = QuestionSelector(set)
        self.mode = mode
        self.set = set
        dialog = self.dialog = Toplevel(root)
        dialog.title("create question randomly")
        dialog.geometry("400x300")
        self.root = root = dialog
  
        import tkinter as tk




        if(mode >0):
            # Label for ComboBox
            self.column_label = tk.Label(root, text="Select an option:")
            self.column_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

            self.column_var = tk.StringVar()
            self.column_box = ttk.Combobox(root, textvariable=self.column_var)
            self.column_box['values'] = tuple(self.questionSelector.columns())
            self.column_box.current(0)
            self.column_box.grid(row=0, column=1, padx=10, pady=5, sticky='w')
            if(mode > 1):
                self.column_var.trace('w', self.update_value)

                # Label for second ComboBox
                self.value_label = tk.Label(root, text="Select an item:")
                self.value_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

                # Second ComboBox
                self.value_var = tk.StringVar()
                self.value_box = ttk.Combobox(root, textvariable=self.value_var)
                self.value_box.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        # Update the second combo box initially

        # Label for Entry
        self.entry_label = tk.Label(root, text="Enter an integer:")
        self.entry_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        # Entry
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(root, textvariable=self.entry_var)
        self.entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        

        # Submit Button
        self.submit_button = tk.Button(root, text="create", command=self.create)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)
 
    def update_value(self, *args):
        selected_category = self.column_var.get()
        
        self.value_box['values'] = tuple(self.questionSelector.enum(selected_category))
       
        self.value_box.current(0)
    def create(self):

        if self.entry_var.get().isdigit():
                number = int(self.entry_var.get())
               
        else:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")
            return;
        if(self.mode == 0):
            personas = self.questionSelector.selectRandomly(number)
        if self.mode == 1:
            combo_value = self.column_var.get()
            personas = self.questionSelector.selectOnColumn(number)

            
        if self.mode == 2:
            combo_value = self.column_var.get()
            value_value = self.value_var.get()
            personas =self.questionSelector.selectByColumn(combo_value, value_value, number)
        self.setData(personas)
          

 
class SelectQuestion:
    def __init__(self, parent):

        paned_window = ttk.PanedWindow(parent, orient=VERTICAL)
        paned_window.pack(fill=BOTH, expand=True)
        
        # 创建上 Pane 的内容
        self.totop_frame = top_frame = ttk.Frame(paned_window)
        
        
        # 创建下 Pane 的内容
        bottom_frame = ttk.Frame(paned_window)
        
        
        # 将两个 Frame 添加到 PanedWindow
        paned_window.add(top_frame)
        paned_window.add(bottom_frame)

        
        self.set_label = Label(top_frame, text="Select an option:")
        self.set_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        self.set_var = StringVar()
        self.set_box = ttk.Combobox(top_frame, textvariable=self.set_var)
        self.set_box['values'] = self.question_set()
        self.set_box.current(0)
        self.set_box.grid(row=0, column=1, padx=10, pady=5, sticky='w')
   
        self.allbutton = Button(top_frame, text='complete random', command=self.all)

        self.allbutton.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.byrandom = Button(top_frame, text='complete random', command=self.randomly)

        self.byrandom.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        self.bycolumn = Button(top_frame, text='by column', command=self.by_column)

        self.bycolumn.grid(row=1, column=2, padx=10, pady=5, sticky='w')
        self.oncolmn = Button(top_frame, text='on column', command=self.on_column)

        self.oncolmn.grid(row=1, column=3, padx=10, pady=5, sticky='w')

           

        self.table = Table(bottom_frame, showtoolbar=True, showstatusbar=True)
        self.table.show()
    def question_set(self):
        from asociety.repository.database import engine
        with engine.connect() as con:
            from sqlalchemy import text

            rs = con.execute(text('SELECT distinct question_set FROM question'))
            result =[]
            for row in rs:
                result.append(row[0])
        return tuple(result)      

    def all(self):
        from asociety.repository.database import engine
        data = pd.read_sql_query("select * from question where question_set = '"  + self.set_var.get() + "'", engine)  
        self.table.model.df = data
        self.table.redraw()
    def randomly(self):
        set = self.set_var.get()
        RandomSelect(self.totop_frame, 0, self.setData, set)        
   
    def on_column(self):
        set = self.set_var.get()
        RandomSelect(self.totop_frame, 1, self.setData,set)
        
        
   
    def by_column(self):
        set = self.set_var.get()
        RandomSelect(self.totop_frame,2,self.setData,set)
    def setData(self, data):
        self.data = data
        self.table.model.df = data
        self.table.redraw()
class CreateQuestionGroup:
    def __init__(self, parent) -> None:
        self.parent = parent
        inner_panedwindow = ttk.PanedWindow(parent, orient=VERTICAL)
        inner_panedwindow.pack(fill=BOTH, expand=True)

        # Create two frames to be added to the inner PanedWindow
        top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN)
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN)

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=5)
        inner_panedwindow.add(bottom_frame, weight=1)
        self.selector = SelectQuestion(top_frame)
 


   # Label for Entry
        self.name_label = Label(bottom_frame, text="Enter Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        # Entry
        self.name_var = StringVar()
        self.name_entry = ttk.Entry(bottom_frame, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        # Label for Entry
        self.desc_label = Label(bottom_frame, text="Enter Description:")
        self.desc_label.grid(row=0, column=2, padx=10, pady=5, sticky='w')

        # Entry
        self.desc_var = StringVar()
        self.desc_entry = ttk.Entry(bottom_frame, textvariable=self.desc_var)
        self.desc_entry.grid(row=0, column=3, padx=10, pady=5, sticky='w')

        self.submit_button = Button(bottom_frame, text="view sheet", command=self.view_sheet)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.submit_button = Button(bottom_frame, text="create", command=self.create)
        self.submit_button.grid(row=1, column=1, columnspan=2, pady=10)

    def view_sheet(self):
        sheet = self.create_sheet()
        dialog = self.dialog = Toplevel( self.parent)
        dialog.title('view sheet')
        dialog.geometry("800x600")
        from tkinter import scrolledtext
        text_widget = scrolledtext.ScrolledText(dialog, wrap=WORD, bg='#1E1E1E', fg='#DADADA', 
                                                     insertbackground='#DADADA', font=('Helvetica', 14),
                                                     selectbackground='#5A5A5A', selectforeground='#FFFFFF', 
                                                     relief=FLAT, padx=10, pady=10)

        text_widget.pack(expand=True, fill=BOTH)
        text_widget.insert(END, sheet)
    def create_sheet(self):
        df = self.selector.table.model.df
        import numpy as np
        length = len(df)
        n = length/20
        r = length%20
        if(r != 0):
            n = n+ 1
        rst = []
        subs = np.array_split(df, n)
        for sub in subs:
            s = self.create_sub_sheet(sub)
            rst.append(s)
        import json
        jsons = json.dumps(rst)
        return jsons
    def create_sub_sheet(self, df):
        sheet = ''
        i = 1
        
        for index, row in df.iterrows():
            sheet += '\n' + str(i) + '. ' +  row['question']
            sheet += '\nFollwing are options = choose from:\n'
            sheet += row['options']
            i = i + 1
        return sheet
        
    def create(self):
        df = self.selector.table.model.df
        from sqlalchemy.orm import Session

        with Session(engine) as session:
            import asociety.repository.experiment_rep as rep
            ent = rep.QuestionGroup()
            ent.name = self.name_var.get()
            ent.type = 'exam'
            ent.table = 'question'
            ent.description = self.desc_var.get()
  
           
            ps = [str(row['id']) for i, row in df.iterrows()]
            ent.question_set =  self.selector.set_var.get()
            ent.questions =  ','.join(ps)
            sheet = self.create_sheet()

            ent.quiz_sheet = sheet
          
            session.add(ent)
            session.commit()
 

import numpy as np
df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10,11,9,9,9,9], columns=['TEST'])
df_split = np.array_split(df, 3)
print(df_split)
