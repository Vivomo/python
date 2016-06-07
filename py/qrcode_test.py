import qrcode
import tkinter

url = 'temp.png'


def alert_qrcode(content):
    q = qrcode.main.QRCode()
    q.add_data(content)
    q.make()
    img = q.make_image()
    img.save(url)

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=400, height=400, bg='white')
    img2 = tkinter.PhotoImage(file=url)
    canvas.create_image(200, 200, image=img2)
    canvas.pack()
    root.mainloop()


while 1:
    inp = input('Please input some text:').strip()
    if inp.find('end') == 0:
        print('Process exited.')
        break
    else:
        alert_qrcode(inp)
