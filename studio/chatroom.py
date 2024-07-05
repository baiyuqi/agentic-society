
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
        top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=1)
        inner_panedwindow.add(bottom_frame, weight=1)

        top_panedwindow = ttk.PanedWindow(top_frame, orient=HORIZONTAL)
        top_left_frame = ttk.Frame(top_panedwindow, width=400, height=200,style='TFrame')
        top_right_frame = self.top_right_frame = ttk.Frame(top_panedwindow, width=400, height=200,style='TFrame')
        top_panedwindow.add(top_left_frame, weight=1)
        top_panedwindow.add(top_right_frame, weight=1)
        top_panedwindow.pack(fill=BOTH, expand=True)  # Pack the top_panedwindow

        # Create a scrolled text widget
        self.text_widget = scrolledtext.ScrolledText(top_left_frame, wrap=WORD, bg='#1E1E1E', fg='#DADADA', 
                                                     insertbackground='#DADADA', font=('Helvetica', 14),
                                                     selectbackground='#5A5A5A', selectforeground='#FFFFFF', 
                                                     relief=FLAT, padx=10, pady=10)

        self.text_widget.pack(expand=True, fill=BOTH)

        # Add some sample text
        sample_text = """Welcome to Chatroom!
        """
        self.text_widget.insert(END, sample_text)


      
        self.submit_button = ttk.Button(bottom_frame, text="select chatters" , command=self.select_chatters,style='TButton')
        self.submit_button.grid(row=1, column=0, columnspan=1, pady=10)

        self.submit_button = ttk.Button(bottom_frame, text="start chat", command=self.start_chat,style='TButton')
        self.submit_button.grid(row=1, column=2, columnspan=1, pady=10)
        self.submit_button = ttk.Button(bottom_frame, text="stop chat", command=self.stop_chat,style='TButton')
        self.submit_button.grid(row=1, column=4, columnspan=1, pady=10)

        self.submit_button = ttk.Button(bottom_frame, text="chat summary", command=self.chat_summary,style='TButton')
        self.submit_button.grid(row=1, column=6, columnspan=1, pady=10)

        self.submit_button = ttk.Button(bottom_frame, text="query friends", command=self.query_friends,style='TButton')
        self.submit_button.grid(row=1, column=8, columnspan=1, pady=10)
        self.tree = self.persona_table(top_right_frame)
    def fill_personas(self,data,fp):
        self.tree.delete(*self.tree.get_children())
        for person in fp:
            self.tree.insert("", "end", values=person)
        self.top_right_frame.update()
    def persona_table(self, parent):

        tree = ttk.Treeview(parent, columns=("id", "Name", "Age", "Occupation"), show='headings')
        tree.heading("id", text="id")
        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")
        tree.heading("Occupation", text="Occupation")

        # Set column widths
        tree.column("id", width=150)
        tree.column("Name", width=150)
        tree.column("Age", width=100)
        tree.column("Occupation", width=150)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        # Pack the Treeview and scrollbar
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        return tree

  
    def message(self, msg):
            self.text_widget.insert(END, '\n\n' + msg)
    def chat_summary(self): 
        from asociety.interaction.chatroom_manager import get_summary
        sum = get_summary(None)
    def query_friends(self): 
        from asociety.interaction.chatroom_manager import get_friends
        for p in self.personas:
            sum = get_friends(persona=p['persona'], nickname="chatter" + str(p['id']))

    def select_chatters(self):

        from asociety.interaction.chatroom_manager import select_personas
        self.personas, fp = select_personas(7)
        self.fill_personas(self.personas, fp)
    def stop_chat(self):
        self.run = False
    def start_chat(self):
        self.run = True;
        from asociety.interaction.chatroom_manager import create_graph
        graph = create_graph(self.personas, self.message)
        from IPython.display import Image, display

        try:
            display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
        except:
            # This requires some extra dependencies and is optional
            pass
        from langchain_core.messages import (
            HumanMessage,
        )
        events = graph.stream(
            {
                "messages": [
                    HumanMessage(
                        content="Let's talk about something interesting. Better first introduce yourself."
                        
                    )
                ],
            },
            # Maximum number of steps to take in the graph
            {"recursion_limit": 150},
        )
        def run():
            for s in events:
                if not self.run:
                    return;
                print(s)
                print("----")
        self.text_widget.delete(1.0, END)
        import threading
        # 启动一个新线程来执行耗时任务
        self.task_thread = threading.Thread(target=run)
        self.task_thread.start()

