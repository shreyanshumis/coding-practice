import tkinter as tk
def destroy():
    button.destroy()
window = tk.Tk()
window.title("SH GUI")
label = tk.Label(window, text="Practicals")
label.pack()
button_ok = tk.Button(window, text="OK")
button_ok.pack(side=tk.LEFT)
button_cancel = tk.Button(window, text="Cancel")
button_cancel.pack(side=tk.LEFT)
button = tk.Button(window, text="Destroy", command=destroy)
button.pack()
window.mainloop()
