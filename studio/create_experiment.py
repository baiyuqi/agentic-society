
from tkinter import *
from tkinter import ttk
from pandastable import Table, TableModel
from asociety.repository.database import engine
import pandas as pd

from asociety.generator.persona_generator import *
from asociety.repository.database import engine
class SelectPersonaGroup:
    def __init__(self, root) -> None:
        import tkinter as tk
        self.pdf =  pd.read_sql_table(table_name='persona_group',con=engine) 
        self.qdf =  pd.read_sql_table(table_name='question_group',con=engine) 
        self.column_label = tk.Label(root, text="Select an option:")
        self.column_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        self.column_var = tk.StringVar()
        self.column_box = ttk.Combobox(root, textvariable=self.column_var)
        self.column_box['values'] = tuple(self.pdf['name'])
        self.column_box.current(0)
        self.column_box.grid(row=0, column=1, padx=10, pady=5, sticky='w')
      
        self.column_var.trace('w', self.update_value)

        # Label for second ComboBox
        self.value_label = tk.Label(root, text="Select an item:")
        self.value_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        # Second ComboBox
        self.value_var = tk.StringVar()
        self.value_box = ttk.Combobox(root, textvariable=self.value_var)
        self.value_box.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        self.value_box['values'] = tuple(self.qdf['name'])
    def update_value(self, *args):
        selected_category = self.column_var.get()
        
        
class CreateExperimentDialog:        
    def __init__(self, root, updateTree) -> None:
        self.updateTree = updateTree
        dialog = self.dialog = Toplevel(root)
        dialog.title('Create Experiment')
        dialog.geometry("800x600")
        self.dialog = dialog    



        # Create a Notebook widget


            
        inner_panedwindow = ttk.PanedWindow(dialog, orient=VERTICAL)
        inner_panedwindow.pack(fill=BOTH, expand=True)

        # Create two frames to be added to the inner PanedWindow
        top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN)
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN)

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=1)
        inner_panedwindow.add(bottom_frame, weight=1)
        self.table = Table(bottom_frame, showtoolbar=True, showstatusbar=True)
        self.table.show()
    
       

        self.selector = SelectPersonaGroup(top_frame)
       

        # Label for second ComboBox
        self.etype_label = Label(top_frame, text="Select quiz or per question:")
        self.etype_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        # Second ComboBox
        self.etype_var = StringVar()
        self.etype_box = ttk.Combobox(top_frame, textvariable=self.etype_var)
        self.etype_box.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        self.etype_box['values'] = ('quiz_sheet','per_question')

        # Label for Entry
        self.name_label = Label(top_frame, text="Enter Name:")
        self.name_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')

        # Entry
        self.name_var = StringVar()
        self.name_entry = ttk.Entry(top_frame, textvariable=self.name_var)
        self.name_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        # Label for Entry
        self.desc_label = Label(top_frame, text="Enter Description:")
        self.desc_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')

        # Entry
        self.desc_var = StringVar()
        self.desc_entry = ttk.Entry(top_frame, textvariable=self.desc_var)
        self.desc_entry.grid(row=4, column=1, padx=10, pady=5, sticky='w')

        self.create_button = Button(top_frame, text="create", command=self.create)
        self.create_button.grid(row=5, column=0, columnspan=1, pady=10)
        
        self.save_button = Button(top_frame, text="save", command=self.save)
        self.save_button.grid(row=5, column=2, columnspan=1, pady=10)
    def create_byquestion(self):
        from asociety.repository.database import engine
        name = self.selector.column_var.get()
        df = self.selector.pdf
    
        selectedp = df[df['name'].isin([name])]
        personas = selectedp.iloc[0,3]
        personas = personas.split(',')

        name = self.selector.value_var.get()
        df = self.selector.qdf
    
        selectedp = df[df['name'].isin([name])]
        questions = selectedp.iloc[0,3]
        questions = questions.split(',')
        personas = np.array(personas)
        personas = personas.astype(np.int32)
        questions = np.array(questions)
        questions = questions.astype(np.int32)
        pf = pd.DataFrame(data = personas, columns=['persona_id'])
        qf = pd.DataFrame(data = questions, columns=['question_id'])
        qas = pf.merge(qf, how='cross')
        qas['experiment_name'] = self.name_var.get()
        self.qas = qas
        self.table.model.df = qas
        self.table.redraw()
    def create_quiz(self):
        self.etype = 'quiz_sheet'
        from asociety.repository.database import engine
        name = self.selector.column_var.get()
        df = self.selector.pdf
      
        selectedp = df[df['name'].isin([name])]
        personas = selectedp.iloc[0,3]
        personas = personas.split(',')

        name = self.selector.value_var.get()
        from asociety.experiments.quiz_generator import QuizGenerator
        sheet = QuizGenerator(name).generateQuiz()


        personas = np.array(personas)
        personas = personas.astype(np.int32)
        pdf = pd.DataFrame(data = personas, columns=['persona_id'])

  


        pdf['experiment_name'] = self.name_var.get()


        sdf = pd.DataFrame(sheet, columns=['quiz_sheet'])
        qas = pdf.merge(sdf, how='cross')
        self.qas = qas
        self.table.model.df = qas
        self.table.redraw()
    def create(self):
        etype = self.etype_var.get()
        if(etype=='per_question'):
            self.create_byquestion()
        else:
            self.create_quiz()
       


        


      
    def save(self):
        from asociety.repository.database import engine
        from asociety.repository.experiment_rep import ExperimentEntity
        from sqlalchemy.orm import Session
        pname = self.selector.column_var.get()
        qname = self.selector.value_var.get()
        name = self.name_var.get()
        desc = self.desc_var.get()
        with Session(engine) as session:
            e = ExperimentEntity()
            e.name = name
            e.type = self.etype_var.get()
            e.description = desc
            e.persona_group = pname
            e.question_group = qname
            session.add(e)
            session.commit()
        if(self.etype == 'quiz_sheet'):
           self.qas.to_sql('quiz_answer', con=engine, if_exists='append')
        else:
           self.qas.to_sql('question_answer', con=engine, if_exists='append')
        self.updateTree()

    def sampling(self):
        pass
       
 