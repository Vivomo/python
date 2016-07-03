import tkinter

top = tkinter.Tk()
label = tkinter.Label(top, text='I Love you, susu!')
label.pack()
btn = tkinter.Button(top, text="QUIT", command=top.quit, bg='red', fg='white')
btn.pack(fill=tkinter.X, expand=1)
tkinter.mainloop()
