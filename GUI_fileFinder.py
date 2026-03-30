import os
import time
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window(themename="darkly")
app.title("🔍 File Finder Pro")
app.geometry("700x500")

results = []

# --- Functions ---
def browse_folder():
    path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, path)

def search_files():
    global results
    results.clear()
    listbox.delete(0, tk.END)

    folder = folder_entry.get()
    keyword = keyword_entry.get().lower()
    file_type = type_entry.get().lower()

    start_time = time.time()

    for root, dirs, files in os.walk(folder):
        for file in files:
            if keyword in file.lower():
                if file_type and not file.endswith(file_type):
                    continue

                full_path = os.path.join(root, file)
                size = os.path.getsize(full_path)
                modified = os.path.getmtime(full_path)

                results.append((file, full_path, size, modified))

    sort_option = sort_var.get()

    if sort_option == "Name":
        results.sort(key=lambda x: x[0])
    elif sort_option == "Size":
        results.sort(key=lambda x: x[2])
    elif sort_option == "Date":
        results.sort(key=lambda x: x[3])

    for item in results:
        listbox.insert(tk.END, item[1])

    end_time = time.time()
    time_label.config(text=f"⏱ Time: {round(end_time - start_time, 2)}s")


# --- UI ---
ttk.Label(app, text="📂 Folder:").pack(pady=5)
folder_entry = ttk.Entry(app, width=60)
folder_entry.pack()

ttk.Button(app, text="Browse", command=browse_folder, bootstyle=PRIMARY).pack(pady=5)

ttk.Label(app, text="🔍 Keyword:").pack()
keyword_entry = ttk.Entry(app, width=40)
keyword_entry.pack()

ttk.Label(app, text="📄 File Type (e.g. .pdf):").pack()
type_entry = ttk.Entry(app, width=20)
type_entry.pack()

ttk.Label(app, text="🧠 Sort By:").pack()
sort_var = tk.StringVar(value="Name")
ttk.OptionMenu(app, sort_var, "Name", "Name", "Size", "Date").pack()

ttk.Button(app, text="🚀 Search", command=search_files, bootstyle=SUCCESS).pack(pady=10)

time_label = ttk.Label(app, text="⏱ Time: 0s")
time_label.pack()

listbox = tk.Listbox(app, width=90, height=15)
listbox.pack(pady=10)

app.mainloop()