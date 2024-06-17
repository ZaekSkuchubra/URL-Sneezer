import tkinter as tk
import os
import webbrowser
import subprocess
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = "Bundle.txt"
file_path = os.path.join(script_dir, filename)
def bundleCrash():
    with open(file_path, 'r') as file:
        content = file.readline()
        content2 = file.readline()
        content3 = file.readline()
        content4 = file.readline()
        content5 = file.readline()
        content6 = file.readline()
        content7 = file.readline()
        content8 = file.readline()
        content9 = file.readline()
        content10 = file.readline()
        url = content
        url1 = content2
        url2 = content3
        url3 = content4
        url4 = content5
        url5 = content6
        url6 = content7
        url7 = content8
        url8 = content9
        url9 = content10
        print(url,url1,url2,url3,url4,url5,url6,url7,url8,url9)
        webbrowser.open(url)
        webbrowser.open(url1)
        webbrowser.open(url2)
        webbrowser.open(url3)
        webbrowser.open(url4)
        webbrowser.open(url5)
        webbrowser.open(url6)
        webbrowser.open(url7)
        webbrowser.open(url8)
        webbrowser.open(url9)
def open_file():
    filepath = os.path.join(script_dir, "Bundle.txt")
    try:
        subprocess.run(["xdg-open", filepath])
    except FileNotFoundError:
        try:
            subprocess.run(["open", filepath])
        except FileNotFoundError:
            subprocess.run(["start", "", filepath], shell=True)
root = tk.Tk()
root.geometry("500x210")
root.configure(bg=("lightpink"))
root.title("URL Sneeze")

button = tk.Button(root)
button.configure(bg=("lightsalmon3"), text=("Click here to open link bundle"), command= bundleCrash, width=70, height=4, borderwidth=(0), font=("Parchment"))
button.pack(padx=10, pady=10)
button1 = tk.Button(root)
button1.configure(bg=("lightsalmon3"), text=("Click here to edit bundle"), width=70, height=4, borderwidth=(0), font=("Parchment"), command=open_file)
button1.pack(padx=10, pady=10)
tk.mainloop()