import qrcode

url = input("Enter URL to generate QR code: ").strip()
filename = input("Enter filename to save QR code (without extension): ").strip()

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)

qr.add_data(url)
qr.make(fit=True)

image = qr.make_image(fill_color='red', back_color='white')

output_file = f"{filename}.png"
image.save(output_file)

print(f"QR code generated and saved as {output_file}")
