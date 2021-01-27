import platform
import ctypes
import tkinter as tk
import tkinter.font as tkFont
import mystatistics

""" ------------------------------------
                Functions
------------------------------------ """

def save_data():
    with open('data','w',encoding='utf-8') as fo:
        fo.write(textbox1.get(1.0,'end-1c'))

def get_statistics():
    save_data()
    mystatistics.statistics('data')
    textbox2.configure(state='normal')
    textbox2.delete(1.0,'end')
    with open('result',encoding='utf-8') as fi:
        textbox2.insert(tk.INSERT,fi.read())
    textbox2.configure(state='disabled')

""" ------------------------------------
                Root
------------------------------------ """

if int(platform.release()) >= 8:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = tk.Tk()
root.title('Thống kê thành phần số liệu')
root.geometry('600x600')
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

""" ------------------------------------
                frame 1
------------------------------------ """

frame1 = tk.Frame(root)

frame1.rowconfigure(0,weight=1)
frame1.columnconfigure((0,2),weight=1)

frame1.grid(row=0,column=0,stick='news')

xscrollbar1 = tk.Scrollbar(frame1,orient='horizontal')
yscrollbar1 = tk.Scrollbar(frame1)
xscrollbar2 = tk.Scrollbar(frame1,orient='horizontal')
yscrollbar2 = tk.Scrollbar(frame1)

customFont = tkFont.Font(family='consolas',size=12)

textbox1 = tk.Text(
    frame1,
    wrap='none',
    font=customFont,
    undo=True,
    xscrollcommand=xscrollbar1.set,
    yscrollcommand=yscrollbar1.set
)
textbox2 = tk.Text(
    frame1,
    wrap='none',
    font=customFont,
    state='disabled',
    xscrollcommand=xscrollbar2.set,
    yscrollcommand=yscrollbar2.set
)

xscrollbar1.configure(command = textbox1.xview)
yscrollbar1.configure(command = textbox1.yview)
xscrollbar2.configure(command = textbox2.xview)
yscrollbar2.configure(command = textbox2.yview)

textbox1.grid(row=0,column=0,sticky='news')
xscrollbar1.grid(row=1,column=0,sticky='ew')
yscrollbar1.grid(row=0,column=1,sticky='ns')
textbox2.grid(row=0,column=2,sticky='news')
xscrollbar2.grid(row=1,column=2,sticky='ew')
yscrollbar2.grid(row=0,column=3,sticky='ns')

""" ------------------------------------
                frame 2
------------------------------------ """

frame2 = tk.Frame(root)

frame2.grid(row=1)

# get statistics
gstbutton = tk.Button(frame2,text='get statistics',command=get_statistics)
gstbutton.grid(ipadx=2,ipady=2)

""" ------------------------------------ """

root.mainloop()