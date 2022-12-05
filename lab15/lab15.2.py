import tkinter as tk 

def calc():
    box1.delete("1.0", tk.END)
    f =  open('text.txt')
    ar = f.read().split('.')
    for i in range(len(ar)):
        words = ar[i].strip().split(' ')
        words.sort(key=lambda x: x.lower())
        box1.insert(tk.END,str(i) + ": ")
        str_words = ' '.join(words)
        box1.insert(tk.END,str_words + "\n")
        

win=tk.Tk()
fr = tk.Frame(master=win, width=600, height=100)
fr.pack() 
box1=tk.Text() 
Button=tk.Button(text='перевести',background='black',foreground='white',width=50,height=20, command=calc)


box1.pack() 
Button.pack()
win.mainloop()
