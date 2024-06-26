
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


        
        self.submit_button = Button(bottom_frame, text="start chat", command=self.start_chat)
        self.submit_button.grid(row=2, column=0, columnspan=1, pady=10)

  
    def message(self, msg):
            self.text_widget.insert(END, '\n\n' + msg)
    def start_chat(self):
        from asociety.interaction.chatroom_manager import select_personas, create_graph
        personas = select_personas(3)
        graph = create_graph(personas, self.message)
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
                print(s)
                print("----")
        self.text_widget.delete(1.0, END)
        import threading
        # 启动一个新线程来执行耗时任务
        task_thread = threading.Thread(target=run)
        task_thread.start()

