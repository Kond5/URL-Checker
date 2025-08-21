import tkinter as tk
from tkinter import messagebox
import requests
import time


def check_website():
    site = entry.get().strip()
    if not site:
        messagebox.showwarning("Warning", "Please enter a website domain!")
        return


    for protocol in ["https://", "http://"]:
        url = protocol + site
        try:
            start = time.time()
            response = requests.get(url, timeout=5)
            end = time.time()
            load_time = round(end - start, 2)


            if response.status_code == 200:
                result.set(f"[✅] {url} is up\nResponse time: {load_time} s")
                return
            else:
                result.set(f"[❌] {url} returned {response.status_code}")
                return
        except:
            continue
    result.set(f"[❌] {site} Error! Check the url.")


# GUI
root = tk.Tk()
root.title("URL Checker v1.1")
root.geometry("400x250")
root.resizable(False, False)


label = tk.Label(root, text="Enter Website Domain:", font=("Arial", 12))
label.pack(pady=10)


entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=5)


check_btn = tk.Button(root, text="Check", font=("Arial", 12), command=check_website, bg="#4CAF50", fg="white")
check_btn.pack(pady=10)


result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 11), wraplength=350, justify="center")
result_label.pack(pady=20)


root.mainloop()
