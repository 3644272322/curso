import tkinter as tk

# function

# crear la ventana
root = tk.Tk()
# configurar la ventana
root = title("paython-tkinter")
root = resizable(0, 0)
root = minsize(1000,700)

# elements
# label
label_num1 = tk.Label(root, text="Número 1:") 
label_num2 = tk.Label(root, text="Número 2:")

# textbox
text_num1 = tk.StringVar()
text_num2 = tk.StringVar()
# entry
entry_num1 = tk.entry()
entry_num2 = tk.entry()
# button
button_num1= tk.Button()
# positios
label_num1.grid(column=0, row=0)
label_num2.grid(column=0, row=1)
# inicializar la ventana
root = mainloop()