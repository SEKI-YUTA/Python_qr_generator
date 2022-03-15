import os
import qrcode
import tkinter
from tkinter import messagebox

print(os.getcwd())
root = tkinter.Tk()
root.title('Demo App')
root.geometry('480x120')

filename_label = tkinter.Label(root, text="ファイル名")
filename_label.pack()
filename_field = tkinter.Entry(width=40)
filename_field.pack(fill='x', padx=30)
data_label = tkinter.Label(root, text="QRコードにするデータ")
data_label.pack()
data_field = tkinter.Entry(width=40)
data_field.pack(fill='x', padx=30)
def click_button():
    input_val = data_field.get()
    img = qrcode.make(input_val)
    if filename_field.get() == "":
        messagebox.showinfo("エラー", "保存するファイル名を入力してください")
        return
    else:
        img.save('{0}.png'.format(filename_field.get()))
        messagebox.showinfo("新規作成の確認","{0}　のQRコードを生成しました".format(input_val))
button = tkinter.Button(text="生成", command=click_button)
button.pack()

root.mainloop()