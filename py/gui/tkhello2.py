import tkinter

top = tkinter.Tk()
label = tkinter.Label(top, text='I Love you, susu!')
label.pack()
btn = tkinter.Button(top, text="I love you", command=top.quit)
btn.pack()
tkinter.mainloop()
