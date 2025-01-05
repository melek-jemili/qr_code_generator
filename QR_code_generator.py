import qrcode
from PIL import Image, ImageDraw
from qrcode.image.pil import PilImage
#function to generate QR code
def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
#imput text to generate QR code 
text = input("Enter the link of the website: ")
name = input("Enter the file name to save the QR code: ")
file_path=input("Enter the file path where to save the QR code: ")
file_name=file_path+name+".png"
generate_qr_code(text, file_name)
print(f"QR code generated successfully save in {name}.png !!")