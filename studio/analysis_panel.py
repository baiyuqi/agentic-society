import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

class AnalysisPanel:
    def __init__(self, parent) -> None:
        pass
        self.main = parent = ttk.Frame(parent)   

        self.fig = fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        self.axes = fig.add_subplot(111)
        self.axes.plot(t, 2 * np.sin(2 * np.pi * t))

        self.canvas = canvas = FigureCanvasTkAgg(fig, master=parent)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, parent)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)


        canvas.mpl_connect("key_press_event", on_key_press)

    def setData(self, experiment_name, updateTree):
        from asociety.analysis.analysis import ExperimentSummary
        es = ExperimentSummary(experiment_name=experiment_name)
        data = es.statistics('education_num')
        self.axes.clear()
        data.plot(ax=self.axes)
      
        self.canvas.draw()
      