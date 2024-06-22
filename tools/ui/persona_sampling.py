
from tkinter import *
from tkinter import ttk
from pandastable import Table, TableModel
from asociety.repository.database import engine
import pandas as pd

from asociety.generator.persona_generator import *
from asociety.repository.persina_rep import PersonaRepository
class PersonaSamplingDialog:
    def __init__(self, root):

        dialog = self.dialog = Toplevel(root)
        dialog.title("persona samping")
        dialog.geometry("800x600")
        self.dialog = dialog    
        paned_window = ttk.PanedWindow(dialog, orient=VERTICAL)
        paned_window.pack(fill=BOTH, expand=True)
        
        # 创建上 Pane 的内容
        top_frame = ttk.Frame(paned_window)
        
        
        # 创建下 Pane 的内容
        bottom_frame = ttk.Frame(paned_window)
        
        
        # 将两个 Frame 添加到 PanedWindow
        paned_window.add(top_frame)
        paned_window.add(bottom_frame)

        self.myLabel = Label(top_frame, text='Enter number to sampling')
        self.myLabel.pack()

        self.myEntryBox = Entry(top_frame)
        self.myEntryBox.pack(padx=10,pady=10)

        self.mySubmitButton = Button(top_frame, text='Submit', command=self.asncsampling)

        self.mySubmitButton.pack(padx=10,pady=10)
        self.progressbar = ttk.Progressbar(top_frame,mode="indeterminate")
        self.progressbar.pack(fill='x',padx=10,pady=10)
        self.table = Table(bottom_frame, showtoolbar=True, showstatusbar=True)
    
        
        
   
    def asncsampling(self):
        import threading
        # 启动一个新线程来执行耗时任务
        task_thread = threading.Thread(target=self.dosampling)
        task_thread.start()
        self.progressbar.start()

    def dosampling(self):
        
        number = int(self.myEntryBox.get())
        generator:PersonaGenerator = PersonaGeneratorFactory.create()
        samples = generator.sampling(number)
        df = pd.DataFrame(samples)
        self.table.model.df = df
        self.table.show()
        self.table.redraw()

        rep: PersonaRepository = PersonaRepository()
        rep.savePersonas(samples)
        self.progressbar.stop()