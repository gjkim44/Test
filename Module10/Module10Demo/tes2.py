import tkinter as tk
from tkinter import ttk

class MathProcessor():
    @staticmethod
    def add_values(n1, n2): return n1 + n2

class IOProcessor():
    @staticmethod
    def write_results(n1, n2):
        text = str.format('The Sum of {n1} and {n2} is {result}\n',
                          n1=n1, n2=n2, result=MathProcessor.add_values(n1, n2))
        print(text)


window = tk.Tk()
window['padx'] = 10
window['pady'] = 10

lbl_data_entry = ttk.Label(window, text="Data Entry", font=("Arial", 16), anchor=tk.W)
lbl_data_entry.grid(row=1, column=1, sticky=tk.W)

lbl_first_name = ttk.Label(window, text="First Number ", width=20, anchor=tk.E)
lbl_first_name.grid(row=2, column=1, sticky=tk.E)
txt_first_number = ttk.Entry(window, width=50)
txt_first_number.grid(row=2, column=2)
txt_first_number.insert(0, "0.00")

lbl_second_name = ttk.Label(window, text="Second Number ", width=20, anchor=tk.E)
lbl_second_name.grid(row=3, column=1, sticky=tk.E)
txt_second_number = ttk.Entry(window, width=50)
txt_second_number.grid(row=3, column=2)
txt_second_number.insert(0, "0.00")

btn_show_data = ttk.Button(window, text="Show Data", width=20)
btn_show_data.grid(row=5, column=1, sticky=tk.E)
btn_show_data['command'] = lambda: IOProcessor.write_results(float(txt_first_number.get()),
                                                            float(txt_second_number.get()))

window.mainloop()

