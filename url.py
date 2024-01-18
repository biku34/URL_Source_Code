import requests
import tkinter as tk
from tkinter import scrolledtext

def html_source(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        html = res.text
        return html
    except requests.exceptions.RequestException as e:
        return f"Error : {e}"
    
def show_html():
    url=entry.get()
    ht_source = html_source(url)
    
    if "Error : " in ht_source:
        result.config(state=tk.NORMAL)
        result.delete(1.0,tk.END)
        result.insert(tk.END, ht_source)
        result.config(state=tk.DISABLED)
    else:
        result.config(state=tk.NORMAL)
        result.delete(1.0,tk.END)
        result.insert(tk.END,f"HTML Source Code for {url}:\n\n{ht_source}")
        result.config(state=tk.DISABLED)

root = tk.Tk()
root.title("HTML Source Code Viewer")

root.geometry("690x750")
root.resizable(False,False)
root.configure(bg="yellow")

custom_font = ("Monotype Corsiva",12)
label = tk.Label(root , text = "HTML SOURCE CODE VIEWER!",font = custom_font)
label.grid(row=0,column=1 , padx =15 ,pady=15)

label = tk.Label(root , text="Enter URL : ")
label.grid(row=1 , column =0 , padx = 15 , pady= 15)

entry = tk.Entry(root, width=60)
entry.grid(row=1, column=1, padx=15, pady=15)

button = tk.Button(root, text="Get HTML Source" , command=show_html)
button.grid(row=1, column=2, padx=10, pady=10)

result =scrolledtext.ScrolledText(root , wrap=tk.WORD , width =80 , height =100)
result.grid(row=2,column=0,columnspan=3,padx=15,pady=15)
result.config(state=tk.DISABLED)

root.mainloop()
