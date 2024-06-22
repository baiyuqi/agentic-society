from tkinter import *
from tkinter import ttk
from tools.ui.select_persona import CreatePersonaGroup
from tools.ui.select_question import CreateQuestionGroup

from asociety.generator.persona_generator import *
from tools.ui.persona_sampling import PersonaSamplingDialog
from tools.ui.create_experiment import CreateExperimentDialog
from tkinter import font
class MainWindow:        
    def __init__(self, root) -> None:
        root.title('AgenticSociety')
        root.iconbitmap()   
        # Define the global font
        global_font = font.Font(family="Helvetica", size=12)

        # Configure all widgets to use the global font
        root.option_add("*Font", global_font)
        style = ttk.Style(root)
        style.configure("Treeview", font=("Helvetica", 12)) 
        style.configure("Treeview", rowheight=30) 
        style.configure('TNotebook.Tab', padding=[10, 5], width=20)
        self.menu(root)
        self.root = root    
        self.main = ttk.Frame(root)   
        self.main.pack(fill=BOTH, expand=True)
        from tools.ui.experiment_executor import ExperimentExecutorPanel

 
        self.PW = PW = ttk.PanedWindow(self.main, orient=HORIZONTAL)
        PW.pack(fill=BOTH, expand=True)

        self.left = ttk.Frame(PW, width=75, height=300, relief=SUNKEN)
        self.right = ttk.Frame(PW, width=400, height=300, relief=SUNKEN)

        PW.add(self.left, weight=0)
        PW.add(self.right, weight=4)
        self.executor = ExperimentExecutorPanel(self.right)
        from tools.ui.analysis_panel import AnalysisPanel
        from tools.ui.data_browse import DataBrowser
        self.analsis = AnalysisPanel(self.right)
        self.browser = DataBrowser(self.right)

        self.treeView = self.tree(self.left)

        panels = {"question": self.browser, "persona":self.browser,"persona group":self.browser,"question group":self.browser,"experimentlist":self.browser,"experiment":self.executor,"analysis":self.analsis}
        self.panels = panels

    def donothing(self):
        pass

    def sampling(self):
        inputDialog = PersonaSamplingDialog(self.root)
        self.root.wait_window(inputDialog.dialog)
    def create_experiment(self):
        inputDialog = CreateExperimentDialog(self.root,self.updateTree)
        self.root.wait_window(inputDialog.dialog)
    def create_persona_group(self):
        dialog = self.dialog = Toplevel(root)
        dialog.title('Create Persona Group')
        dialog.geometry("800x600")
        CreatePersonaGroup(dialog)
        
    def create_question_group(self):
        dialog = self.dialog = Toplevel(root)
        dialog.title('Create Question Group')
        dialog.geometry("800x600")
        CreateQuestionGroup(dialog)
    def menu(self,root):
        global_font = font.Font(family="Helvetica", size=20)
        menubar = Menu(root, borderwidth=20)
  
        root.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0,border=12)
        filemenu.add_command(label="sampling", command=self.sampling)
  
        filemenu.add_command(label="Close", command=self.donothing)

        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu, font=global_font)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="create persona goup", command=self.create_persona_group)
        editmenu.add_command(label="create question group", command=self.create_question_group)
        editmenu.add_separator()
        editmenu.add_command(label="create experiment", command=self.create_experiment)
        menubar.add_cascade(label="edit", menu=editmenu,font=global_font)
    def tree(self, frame):
        tv = ttk.Treeview(frame, style="Treeview")
        tv.pack()
        self.recreate(tv)
        tv.config(height=100)
        tv.bind("<<TreeviewSelect>>", self.treeSelect)
        return tv
    def updateTree(self):
        self.recreate(self.treeView)
        self.left.update()
    def recreate(self, tv):
        tv.delete(*tv.get_children())
        tv.insert('', '0', 'sampling', text='sampling')
        tv.insert('', '1', 'base', text='base')
        tv.insert('', '2', 'survey', text='survey')
        tv.insert('base', '0', 'persona', text='persona')
       

        tv.insert('base', '1', 'question', text='question')

        tv.insert('survey', '0', 'persona group', text='persona group')
        tv.insert('survey', '1', 'question group', text='question group')
        tv.insert('survey', '2', 'experimentlist', text='experiment')
        from asociety.repository.database import engine
        from sqlalchemy.orm import Session
        from asociety.repository.experiment_rep import ExperimentEntity
        with Session(engine) as session:
            es = session.query(ExperimentEntity).all()
            
            for i,  e in enumerate(es):
                tv.insert('experimentlist', str(i), 'experiment_' + e.name, text=e.name)

        tv.insert('', '3', 'chatroom', text='chatroom')
        
        tv.insert('', '4', 'analysislist', text='analysis')
        for i,  e in enumerate(es):
                tv.insert('analysislist', str(i), 'analysis_' + e.name, text=e.name)
       
    def treeSelect(self, event):
        from asociety.repository.database import engine
        items = self.treeView.selection()
        item = items[0]
        names = item.split("_")
        panelKey = names[0]
        appKey = panelKey
        if(len(names) == 2):
            exp = appKey= names[1]
        if panelKey not in self.panels:
            return
        panel = self.panels[panelKey]
        panels = set(self.panels.values())
        for p in panels:
            if(p == panel):
                p.main.pack(fill=BOTH, expand=True)
            else:
                p.main.pack_forget()
        panel.setData(appKey)
        
       

if __name__ == "__main__":
    root = Tk()

    MainWindow(root)
    
    root.state('zoomed')
    
    root.mainloop()