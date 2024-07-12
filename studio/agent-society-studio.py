from tkinter import *
from tkinter import ttk
from studio.select_persona import CreatePersonaGroup
from studio.select_question import CreateQuestionGroup

from asociety.generator.persona_generator import *
from studio.persona_sampling import PersonaSamplingDialog
from studio.create_experiment import CreateExperimentDialog
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
        self.main = ttk.Frame(root,style='TFrame')   
        self.main.pack(fill=BOTH, expand=True)
        from studio.experiment_executor import ExperimentExecutorPanel

 
        self.PW = PW = ttk.PanedWindow(self.main, orient=HORIZONTAL)
        PW.pack(fill=BOTH, expand=True)

        self.left = ttk.Frame(PW, width=75, height=300, relief=SUNKEN,style='TFrame')
        self.right = ttk.Frame(PW, width=400, height=300, relief=SUNKEN,style='TFrame')

        PW.add(self.left, weight=0)
        PW.add(self.right, weight=4)
        self.executor = ExperimentExecutorPanel(self.right)
        from studio.analysis_panel import AnalysisPanel
        from studio.data_browse import DataBrowser
        from studio.data_manager import DataManager
        self.analsis = AnalysisPanel(self.right)
        self.browser = DataBrowser(self.right)
        self.manager = DataManager(self.right)
        self.treeView = self.tree(self.left)
        from studio.chatroom import Chatroom
        self.chatroom = Chatroom(self.right)
        from studio.personality_browse import PersonalityBrowser
        self.personality = PersonalityBrowser(self.right)
        from studio.personality_analysis import PersonalityAnalysis
        self.personality_analysis = PersonalityAnalysis(self.right)
        from studio.question_browse import QuestionBrowser
        self.questionbrowser = QuestionBrowser(self.right)

        panels = {"question": self.questionbrowser, "persona":self.browser,"persona group":self.manager,"question group":self.manager,"experimentlist":self.manager,"experiment":self.executor,"analysis":self.analsis,"chatroom":self.chatroom,'personality':self.personality,'personality-analysis':self.personality_analysis}
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

        
        tv.insert('', '3', 'analysislist', text='analysis')
        tv.insert('analysislist', '0', 'analysis-exp', text='experiments analysys')

        for i,  e in enumerate(es):
                tv.insert('analysis-exp', str(i), 'analysis_' + e.name, text=e.name)
        tv.insert('analysislist', '1', 'personality', text='personality')   
        tv.insert('analysislist', '2', 'personality-analysis', text='personality analysis')   
        tv.insert('', '4', 'chatroom', text='chatroom')
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
        panel.setData(appKey,self.updateTree)
        
       

if __name__ == "__main__":
    root = Tk()
       
    # Set style
    style = ttk.Style()
    style.theme_use('clam')  # Use 'clam' theme as base
    
    # Customizing the theme
    style.configure('TFrame', background='#E8E8E8')
    style.configure('TButton', font=('Helvetica', 12), background='#E8E8E8', foreground='black', borderwidth=0)
    style.map('TButton', background=[('active', '#CFCFCF')], relief=[('pressed', 'sunken'), ('!pressed', 'flat')])
    style.configure('TLabel', background='#E8E8E8', font=('Helvetica', 12), foreground='black')
    MainWindow(root)
    
    root.state('zoomed')
    
    root.mainloop()