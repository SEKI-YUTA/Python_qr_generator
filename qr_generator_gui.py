import os
import qrcode
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk

print(os.getcwd())
root = tkinter.Tk()
root.title('Demo App')
# root.geometry('480x360')
img = None
imgTk = None

filename_label = tkinter.Label(root, text="ファイル名")
filename_label.pack()
filename_field = tkinter.Entry(width=40)
filename_field.pack(fill='x', padx=30)
data_label = tkinter.Label(root, text="QRコードにするデータ")
data_label.pack()
data_field = tkinter.Entry(width=40)
data_field.pack(fill='x', padx=30)
image_canvas = tkinter.Canvas(
    width=220,
    height=220,
    bg='cyan'
)
image_canvas.pack()

def draw_qr(qr):
    global imgTk
    imgTk = ImageTk.PhotoImage(qr.resize((220,220)))
    image_canvas.create_image(110,110,image=imgTk, tag="QR code",anchor=tkinter.CENTER)

def generate_qr():
    global img
    input_val = data_field.get()
    generated_qr = qrcode.make(input_val)
    messagebox.showinfo('新規作成', 'QRコードを作成しました')
    img = generated_qr
    draw_qr(generated_qr)

def save_img():
    global img
    print(type(img))
    if img is None:
        messagebox.showinfo('エラー','画像を生成してください')
    elif filename_field.get() == "":
        messagebox.showinfo("エラー", "保存するファイル名を入力してください")
        return
    else:
        img.save('{0}.png'.format(filename_field.get()))
        messagebox.showinfo("新規作成の確認","{0}　のQRコードを保存しました".format(data_field.get()))


generate_button = tkinter.Button(text="生成", command=generate_qr)
generate_button.pack(fill='x',side='right',padx=20)
save_button = tkinter.Button(text="保存", command=save_img)
save_button.pack(fill='x', side='right',padx=20)

root.mainloop()