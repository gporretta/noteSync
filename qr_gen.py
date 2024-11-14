#!/usr/bin/env python3.11

import qrcode

def create_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,  # 21x21
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    
    img.save(file_name)
    print(f"QR code for '{data}' saved as {file_name}")

# Generate QR codes for "GREEN," "RED," and "BLUE"
create_qr_code("GREEN", "GREEN_qr.png")
create_qr_code("RED", "RED_qr.png")
create_qr_code("BLUE", "BLUE_qr.png")

