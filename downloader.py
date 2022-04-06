import requests
import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pathlib import Path

r = random
win = Tk()
win.geometry("700x350")
win.title("Minecraft Spigot Server Downloader")

Label(win, text="Download all spigot versions !", font='Aerial 17 bold italic').pack(pady=15)
Label(win, text="Please enter a real spigot version name. for Example: 1.12.2", font='Aerial 9 bold italic').pack()

text_entry = ttk.Entry(win)
text_entry.pack(pady=30)

def downloader():
    result = text_entry.get()
    path_to_file = 'spigot_' + result + '.jar'
    path = Path(path_to_file)

    if path.is_file():
        messagebox.showinfo("Message", "You already downloaded " + path_to_file + " version...")
    else:
        if type(result) == str:
            messagebox.showinfo("Message", "The version " + result + " is downloading...")
            remote_url = 'https://cdn.getbukkit.org/spigot/spigot-' + result + '.jar'
            randomValue = r.random()
            randomValue = 'spigot_' + result + '.jar'
            data = requests.get(remote_url)
            with open(randomValue, 'wb') as file:
                file.write(data.content)
        else:
            messagebox.showinfo("Message", "Need to be a string")

ttk.Button(win, text="Click for download", command=downloader).pack(pady=5)

Label(win, text="Minecraft Spigot Server Downloader coded by Mixeration / Hacı Mert Gökhan", font='Aerial 9').pack()
Label(win, text="All rights reserved", font='Aerial 9').pack(pady=5)

Label(win, text="Support: mixeration#5118 / mixeration@gmail.com", font='Aerial 9 bold').pack()
Label(win, text="Website: mixeration.github.io", font='Aerial 9 bold').pack()

win.mainloop()