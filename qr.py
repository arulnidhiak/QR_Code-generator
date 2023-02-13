import qrcode

# create qr code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# add data
qr.add_data('I LOVE YOU')
qr.make(fit=True)

# create image
img = qr.make_image(fill_color='black', back_color='white')

# save image to file
img.save('qrcode.png')
