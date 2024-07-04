import tkinter as tk
from tkinter import ttk

class TableWithWidgets:
    def __init__(self, root):
        self.root = root
        self.root.title("Table with Radio Buttons and Combo Boxes")
        
        self.tree = ttk.Treeview(root, columns=('A', 'B', 'C'), show='headings')
        self.tree.heading('A', text='Radio Button')
        self.tree.heading('B', text='Combo Box')
        self.tree.heading('C', text='Text')
        
        self.tree.grid(row=0, column=0, sticky='nsew')

        self.tree.bind('<ButtonRelease-1>', self.on_click)
        
        self.add_table_data()

    def add_table_data(self):
        for i in range(5):
            self.tree.insert('', 'end', values=('', '', 'Sample Text'))

        self.radio_vars = [tk.IntVar() for _ in range(5)]
        self.combo_boxes = []
        self.create_widgets()

    def create_widgets(self):
        for i, item in enumerate(self.tree.get_children()):
            # Create and place the radio button
            radio_button = ttk.Radiobutton(self.root, variable=self.radio_vars[i], value=i)
            self.tree.item(item, values=(radio_button, '', 'Sample Text'))
            radio_button.place(x=20, y=40 + i*20)  # Adjust x, y positions as needed

            # Create and place the combo box
            combo_box = ttk.Combobox(self.root, values=['Option 1', 'Option 2', 'Option 3'])
            combo_box.current(0)
            combo_box.place(x=120, y=40 + i*20)  # Adjust x, y positions as needed
            self.combo_boxes.append(combo_box)

    def on_click(self, event):
        # Handle click events if needed
        pass

if __name__ == "__main__":
    root = tk.Tk()
    table_with_widgets = TableWithWidgets(root)
    root.mainloop()
