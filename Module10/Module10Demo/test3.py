import tkinter as tk
from tkinter import ttk

class MathProcessor():
    def add_values(n1, n2): return n1 + n2

    def subtract_values(n1, n2): return n1 - n2

    def multiply_values(n1, n2): return n1 * n2

    def divide_values(n1, n2): return n1 / n2

class IOProcessor():
    def write_results_to_textbox(n1, n2, textbox):
        textbox['state'] = 'normal'
        text = str.format('The Sum of {n1} and {n2} is {result}\n',
                          n1=n1, n2=n2, result=MathProcessor.add_values(n1,n2))
        text += str.format('The Difference of {n1} and {n2} is {result}\n',
                           n1=n1, n2=n2, result=MathProcessor.subtract_values(n1,n2))
        text += str.format('The Product of {n1} and {n2} is {result}\n',
                           n1=n1, n2=n2, result=MathProcessor.multiply_values(n1,n2))
        text += str.format('The Quotient of {n1} and {n2} is {result}\n',
                           n1=n1, n2=n2, result=MathProcessor.divide_values(n1,n2))
        textbox.delete(1.0, tk.END)
        textbox.insert(tk.END, text)
        textbox['state'] = 'disabled'



window = tk.Tk()
window['padx'] = 10
window['pady'] = 10

lbl_data_entry = ttk.Label(window, text="Data Entry", font=("Arial", 16), anchor=tk.W)
lbl_data_entry.grid(row=1, column=1, sticky=tk.W)

lbl_first_num = ttk.Label(window, text="First Number ", width=20, anchor=tk.E)
lbl_first_num.grid(row=2, column=1, sticky=tk.E)
txt_first_num = ttk.Entry(window, width=50)
txt_first_num.grid(row=2, column=2)
txt_first_num.insert(0, "0.00")

lbl_second_num = ttk.Label(window, text="Second Number ", width=20, anchor=tk.E)
lbl_second_num.grid(row=3, column=1, sticky=tk.E)
txt_second_num = ttk.Entry(window, width=50)
txt_second_num.grid(row=3, column=2)
txt_second_num.insert(0, "0.00")

btn_show_data = ttk.Button(window, text="Show Data", width=20)
btn_show_data.grid(row=5, column=1, sticky=tk.E)
btn_show_data['command'] = lambda: IOProcessor.write_results_to_textbox(float(txt_first_num.get()),
                                                                        float(txt_second_num.get()),
                                                                        mtx)
mtx = tk.Text(width=40,height=10)
mtx.grid(row=6, column=2, sticky=tk.W)

window.mainloop()
