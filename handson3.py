import tkinter as tk

def add():
    n1 = int(e1.get())
    n2 = int(e2.get())
    result.config(text= f"the sum of {n1} and {n2} is "+str (n1+n2))

def subtract():
    n1 = int(e1.get())
    n2 = int(e2.get())
    result.config(text= f"the difference of {n1} and {n2} is "+str (n1-n2))

def multiply():
    n1 = int(e1.get())
    n2 = int(e2.get())
    result.config(text= f"the product of {n1} and {n2} is "+str (n1*n2))

def divide():
    n1 = int(e1.get())
    n2 = int(e2.get())
    result.config(text= f"the quotient of {n1} and {n2} is "+str (n1/n2))

window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg= "lightgreen")

result = tk.Label(window, text ="Result is here : ")
result.grid(row= 0, column= 0, columnspan= 2, pady =15)


tk.Label(window, text= "Enter 1st number").grid(row=1, column=0, padx=10, pady=10)
e1 =tk.Entry(window)
e1.grid(row= 1, column=1, padx =10, pady =10)

tk.Label(window, text ="Enter 2nd number").grid(row=2, column=0, padx =10, pady=10)
e2= tk.Entry(window)
e2.grid(row= 2, column=1, padx=10, pady =10)

tk.Button(window, text ="add", command=add).grid(row=4, column=0, padx=5, pady=5)
tk.Button(window, text ="Substraction", command=subtract).grid(row=4, column =1, padx=5, pady=5)
tk.Button(window, text ="Multiplication",  command=multiply).grid (row=5,column = 0, padx=5, pady=5)
tk.Button(window, text = "Division", command= divide).grid (row =5,column =1, padx=5, pady=5)

window.mainloop()








