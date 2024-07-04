import tkinter as tk
from pandastable import Table, TableModel
import pandas as pd
from asociety.repository.database import engine
class PagedTable:
    def __init__(self, root, df):
        self.root = root
        self.df = df
        # Pagination parameters
        self.rows_per_page = 10
        self.current_page = 1
        self.total_pages = (len(df) + self.rows_per_page - 1) // self.rows_per_page
        
        # Create table
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill='both', expand=True)
        self.table = Table(self.frame, dataframe=self.get_page_data(), showtoolbar=True, showstatusbar=True)
        self.table.show()
        
        # Pagination controls
        self.controls = tk.Frame(self.root)
        self.controls.pack()
        self.prev_button = tk.Button(self.controls, text="Previous", command=self.previous_page)
        self.prev_button.pack(side=tk.LEFT)
        self.next_button = tk.Button(self.controls, text="Next", command=self.next_page)
        self.next_button.pack(side=tk.LEFT)
        
        self.update_controls()
    
    def get_page_data(self):
        start_row = (self.current_page - 1) * self.rows_per_page
        end_row = start_row + self.rows_per_page
        return self.df[start_row:end_row]
    
    def update_table(self):
        self.table.updateModel(TableModel(self.get_page_data()))
        self.table.redraw()
    
    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_table()
            self.update_controls()
    
    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_table()
            self.update_controls()
    
    def update_controls(self):
        self.prev_button.config(state=tk.NORMAL if self.current_page > 1 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if self.current_page < self.total_pages else tk.DISABLED)
