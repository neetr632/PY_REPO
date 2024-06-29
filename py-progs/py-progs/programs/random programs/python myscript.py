# Install the qrcode library (if not already installed)
# You can install it using pip: pip install qrcode[pil]

import qrcode

# Define the data you want to encode
data = "Hello, this is my QR code!"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # QR code version (1 to 40, higher is denser)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=40,  # Border size (adjust as needed)
)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create a QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
img.save("my_qr_code.png")
