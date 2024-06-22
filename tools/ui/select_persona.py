
from tkinter import *
from tkinter import ttk
from pandastable import Table, TableModel
from asociety.repository.database import engine
import pandas as pd
from tkinter import messagebox
from asociety.experiments.experiment_generator import PersonaSelector



class RandomSelect:
    def __init__(self, root, mode, callable):
        self.setData = callable
        self.personaSelector = PersonaSelector()
        self.mode = mode
        dialog = self.dialog = Toplevel(root)
        dialog.title("create persona randomly")
        dialog.geometry("400x300")
        self.root = root = dialog

        import tkinter as tk
        if(mode >0):
            # Label for ComboBox
            self.column_label = tk.Label(root, text="Select an option:")
            self.column_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

            self.column_var = tk.StringVar()
            self.column_box = ttk.Combobox(root, textvariable=self.column_var)
            self.column_box['values'] = tuple(self.personaSelector.columns())
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
        
        self.value_box['values'] = tuple(self.personaSelector.enum(selected_category))
       
        self.value_box.current(0)
    def create(self):

        if self.entry_var.get().isdigit():
                number = int(self.entry_var.get())
               
        else:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")
            return;
        if(self.mode == 0):
            personas = self.personaSelector.selectRandomly(number)
        if self.mode == 1:
            combo_value = self.column_var.get()
            personas = self.personaSelector.selectOnColumn(number)

            
        if self.mode == 2:
            combo_value = self.column_var.get()
            value_value = self.value_var.get()
            personas =self.personaSelector.selectByColumn(combo_value, value_value, number)
        self.setData(personas)
          

 
class SelectPersona:
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
        self.byrandom = Button(top_frame, text='all', command=self.all)

        self.byrandom.pack(padx=10,pady=10)
        self.byrandom = Button(top_frame, text='complete random', command=self.randomly)

        self.byrandom.pack(padx=10,pady=10)

        self.bycolumn = Button(top_frame, text='by column', command=self.by_column)

        self.bycolumn.pack(padx=10,pady=10)
        self.oncolmn = Button(top_frame, text='on column', command=self.on_column)

        self.oncolmn.pack(padx=10,pady=10)

           

        self.table = Table(bottom_frame, showtoolbar=True, showstatusbar=True)
        self.table.show()
    

    def all(self):
        from asociety.repository.database import engine
        data = pd.read_sql_query("select persona.* from persona left join personality on persona.id = personality.persona_id where personality.persona_id is null", engine)  
        self.table.model.df = data
        self.table.redraw()
    def randomly(self):
        RandomSelect(self.totop_frame, 0, self.setData)        
   
    def on_column(self):
        RandomSelect(self.totop_frame, 1, self.setData)
        
        
   
    def by_column(self):
        RandomSelect(self.totop_frame,2,self.setData)
    def setData(self, data):
        self.data = data
        self.table.model.df = data
        self.table.redraw()
class CreatePersonaGroup:
    def __init__(self, parent) -> None:
        inner_panedwindow = ttk.PanedWindow(parent, orient=VERTICAL)
        inner_panedwindow.pack(fill=BOTH, expand=True)

        # Create two frames to be added to the inner PanedWindow
        top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN)
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN)

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=5)
        inner_panedwindow.add(bottom_frame, weight=1)
        self.selector = SelectPersona(top_frame)




        # Label for Entry
        self.name_label = Label(bottom_frame, text="Enter Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        # Entry
        self.name_var = StringVar()
        self.name_entry = ttk.Entry(bottom_frame, textvariable=self.name_var)
        self.name_entry.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        # Label for Entry
        self.desc_label = Label(bottom_frame, text="Enter Description:")
        self.desc_label.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        # Entry
        self.desc_var = StringVar()
        self.desc_entry = ttk.Entry(bottom_frame, textvariable=self.desc_var)
        self.desc_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        self.submit_button = Button(bottom_frame, text="create", command=self.create)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)


    def create(self):
        df = self.selector.table.model.df
        from sqlalchemy.orm import Session

        with Session(engine) as session:
            import asociety.repository.experiment_rep as rep
            ent = rep.PersonaGroup()
            ent.name = self.name_var.get()
            ent.description = self.desc_var.get()
        
            ps = [str(row['id']) for i, row in df.iterrows()]
           
            ent.personas =  ','.join(ps)
          
            session.add(ent)
            session.commit()
 


       