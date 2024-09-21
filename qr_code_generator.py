import qrcode   
data = input("Enter the text/URL: ") # The data to be QR Code.
file_name = input("Enter the filename: ") # The name of the file to be saved with.

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(file_name)

print("Saved the QR Code image.")