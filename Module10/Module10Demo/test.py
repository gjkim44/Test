import tkinter as tk


window = tk.Tk()
window.title("Inventory Manager")
window.geometry("400x100+20+20")

test = tk.Label(window, text = "this is a test", width ="20")
test.grid(row=1,column=1)

button_sel = tk.Button(window, text= "Select Product Info")
button_sel.grid(row=2, column=1, sticky=tk.E)

window.mainloop()