import qrcode

# Define the command to run the Python script
command = "python myscript.py"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the command as data to the QR code
qr.add_data(command)
qr.make(fit=True)

# Create a QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
img.save("launch_script_qr_code.png")
