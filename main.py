import qrcode
userInput = input("qr data:")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(userInput)
qr.make(fit=True)
img = qr.make_image(fill_color="#FFFFFF", back_color="yellow")
print(type(img))
img.save('./qr.png')