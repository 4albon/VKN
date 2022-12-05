import tkinter as tk 
import json

def act():
    with open('dic.json', 'r',encoding="utf-8") as json_file:
        tr = json.load(json_file)
    box1.delete("1.0", tk.END)
    try:
        box1.insert("1.0",tr[entry2.get()]) 
    except:
        box1.insert("1.0",'слово не найдено')

win=tk.Tk()
fr = tk.Frame(master=win, width=630, height=400)
fr.pack() 

L=tk.Label(text='Доброго дня!')
# entry = tk.Entry(foreground="green", background="grey", width=50)
box1=tk.Text() 
entry2 = tk.Entry(foreground="white", background="grey", width=50)
Button=tk.Button(text='перевести',background='black',foreground='white',width=50,height=20, command=act)



L.pack()
box1.pack() 
entry2.pack()
Button.pack()
win.mainloop()