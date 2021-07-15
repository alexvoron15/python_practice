import tkinter as tk
import math
from tkinter.constants import END, INSERT


window = tk.Tk()
window.title("Claculator")
window.geometry("325x455")
window.resizable(False, False)
window.config(bg='#262626')
window.wait_visibility(window)
window.attributes('-alpha', 0.95)

screen = tk.Entry(window, justify = tk.RIGHT, font = ('Arial', 15))
screen.insert(0, '0')
screen.grid(row=0, column=0, columnspan=5, stick = 'we')

def add_numb(number):
  val = screen.get()
  if val[0]=='0' and len(val)==1:
    val=val[1:]
  screen.delete(0, tk.END)
  screen.insert(0, val + number)

def calculating():
  val = screen.get()
  if val[-1] in '+-*/':
    val = val+ val[:-1]
  elif val[-2:] == '/0':
    screen.delete(0, tk.END)
    screen.insert(0, 'На нуль ділити не можна!!!')
  else:
    screen.delete(0, tk.END)
    screen.insert(0, eval(val))

def add_op(operation):
  val = screen.get()
  if val[-1] in '+-*/':
    val = val[:-1]
  elif '+' or '-' or '*' or '/' in val:
    calculating()
    val = screen.get()
  screen.delete(0, tk.END)
  screen.insert(0, val+operation)  

def clr():
  print('So cleeny :3')
  screen.delete(0, tk.END)
  screen.insert(0,0)

def Del():
  txt = screen.get()[:-2]
  screen.delete(1,tk.END)
  screen.insert(1,txt)

def add_sin():
  calculating()
  val = screen.get()
  mat = math.sin(int(val))
  screen.delete(0, tk.END)
  screen.insert(0,mat)

def add_cos():
  calculating()
  val = screen.get()
  mat = math.cos(int(val))
  screen.delete(0, tk.END)
  screen.insert(0,mat)

def add_tan():
  calculating()
  val = screen.get()
  mat = math.tan(int(val))
  screen.delete(0, tk.END)
  screen.insert(0,mat)

def add_ctg():
  calculating()
  val = screen.get()
  mat = math.ctg(int(val))
  screen.delete(0, tk.END)
  screen.insert(0,mat)

def add_log():
  calculating()
  val = screen.get()
  mat = math.log(int(val))
  screen.delete(0, tk.END)
  screen.insert(0,mat)

def add_ln():
  calculating()
  val = screen.get()
  mat = math.log10(int(val))
  screen.delete(0, tk.END)
  screen.insert(0,mat)




#Numbers
tk.Button(text='1', font = ('Arial', 12), command=lambda: add_numb('1')).grid(row=1, column=0, stick='wens', padx=3, pady=3)
tk.Button(text='2', font = ('Arial', 12), command=lambda: add_numb('2')).grid(row=1, column=1, stick='wens', padx=3, pady=3)
tk.Button(text='3', font = ('Arial', 12), command=lambda: add_numb('3')).grid(row=1, column=2, stick='wens', padx=3, pady=3)
tk.Button(text='4', font = ('Arial', 12), command=lambda: add_numb('4')).grid(row=2, column=0, stick='wens', padx=3, pady=3)
tk.Button(text='5', font = ('Arial', 12), command=lambda: add_numb('5')).grid(row=2, column=1, stick='wens', padx=3, pady=3)
tk.Button(text='6', font = ('Arial', 12), command=lambda: add_numb('6')).grid(row=2, column=2, stick='wens', padx=3, pady=3)
tk.Button(text='7', font = ('Arial', 12), command=lambda: add_numb('7')).grid(row=3, column=0, stick='wens', padx=3, pady=3)
tk.Button(text='8', font = ('Arial', 12), command=lambda: add_numb('8')).grid(row=3, column=1, stick='wens', padx=3, pady=3)
tk.Button(text='9', font = ('Arial', 12), command=lambda: add_numb('9')).grid(row=3, column=2, stick='wens', padx=3, pady=3)
tk.Button(text='0', font = ('Arial', 12), command=lambda: add_numb('0')).grid(row=4, column=1, stick='wens', padx=3, pady=3)
tk.Button(text='.', font = ('Arial', 12), command=lambda: add_numb('.')).grid(row=4, column=0, stick='wens', padx=3, pady=3)

#operations
tk.Button(text = '=',  font = ('Arial', 12), bg = 'cyan', command = calculating).grid(row = 3, column  = 4, rowspan= 2, stick='wens', padx=3, pady=3)
tk.Button(text = '+',  font = ('Arial', 12), command = lambda: add_op('+')).grid(row = 1, column  = 3,stick='wens', padx=3, pady=3)
tk.Button(text = '-',  font = ('Arial', 12), command = lambda: add_op('-')).grid(row = 2, column  = 3,stick='wens', padx=3, pady=3)
tk.Button(text = '*',  font = ('Arial', 12), command = lambda: add_op('*')).grid(row = 3, column  = 3,stick='wens', padx=3, pady=3)
tk.Button(text = '/',  font = ('Arial', 12), command = lambda: add_op('/')).grid(row = 4, column  = 3,stick='wens', padx=3, pady=3)
tk.Button(text = '%',  font = ('Arial', 12), command = lambda: add_op('%')).grid(row = 4, column  = 2,stick='wens', padx=3, pady=3)
tk.Button(text='C',  font = ('Arial', 12), bg = 'red', command=lambda: clr()).grid(row=1, column=4, stick='wens', padx=3, pady=3)
tk.Button(text='Del',  font = ('Arial', 12), bg = 'orange', command=lambda: Del()).grid(row=2, column=4, stick='wens', padx=3, pady=3)
tk.Button(text = 'sin',  font = ('Arial', 12), command = lambda: add_sin()).grid(row = 5, column  = 0,stick='wens', padx=3, pady=3)
tk.Button(text = 'cos',  font = ('Arial', 12), command = lambda: add_cos()).grid(row = 5, column  = 1,stick='wens', padx=3, pady=3)
tk.Button(text = 'tan',  font = ('Arial', 12), command = lambda: add_tan()).grid(row = 5, column  = 2,stick='wens', padx=3, pady=3)
tk.Button(text = 'ctg',  font = ('Arial', 12), command = lambda: add_ctg()).grid(row = 5, column  = 3,stick='wens', padx=3, pady=3)
tk.Button(text = 'log',  font = ('Arial', 12), command = lambda: add_log()).grid(row = 5, column  = 4,stick='wens', padx=3, pady=3)
tk.Button(text = 'ln',  font = ('Arial', 12), command = lambda: add_ln()).grid(row = 6, column  = 4,stick='wens', padx=3, pady=3)

for i in range(10):
    window.grid_columnconfigure(i, minsize=65)
    window.grid_rowconfigure(i, minsize=65)

window.mainloop()
