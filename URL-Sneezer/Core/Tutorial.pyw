import tkinter as tk
import subprocess
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = "Core.pyw"
file_path = os.path.join(script_dir, filename)
def open_file():
    filepath = os.path.join(script_dir, "Core.pyw")
    try:
        subprocess.run(["xdg-open", filepath])
    except FileNotFoundError:
        try:
            subprocess.run(["open", filepath])
        except FileNotFoundError:
            subprocess.run(["start", "", filepath], shell=True)
            exit()
root = tk.Tk()
root.geometry("500x210")
root.configure(bg=("lightpink"))
root.title("Warning")
label = tk.Label(root, text=("To make the buttons work, you need to manually set up the bundle of URL's."))
label.configure(bg=("lightsalmon3"), borderwidth=0, width=70, height=6, fg=("lightpink"))
label.pack(padx=10, pady=10)
button = tk.Button(root, text=("Proceed"))
button.configure(bg=("lightsalmon3"),borderwidth=0, fg=("lightpink"),width=40, height=2, font=("Parchment"), command=open_file)
button.pack(padx=10,pady=10)
tk.mainloop()