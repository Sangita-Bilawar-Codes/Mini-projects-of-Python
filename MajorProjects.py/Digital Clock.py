import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

# ✅ label pehle define
label = tk.Label(
    root,
    font=('Calibri', 30, 'italic'),
    bg='brown',
    fg='silver'
)
label.pack(anchor='center')

# ✅ function baad mein
def time():
    string = strftime('%H:%M:%S %p\n%D')
    label.config(text=string,)
    label.after(1000, time)
    

time()
root.mainloop()
